import React, { useState, useEffect, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { FaTrophy } from 'react-icons/fa';
import API_BASE_URL from '../../config/api';
import '../../styles/TopContributors.css';

const TopContributors = ({ filters }) => {
  const [contributors, setContributors] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchContributors = useCallback(async () => {
    setLoading(true);
    
    try {
      // Prepare search filters for backend
      const searchFilters = {
        // Only include websites if some are selected
        websites: filters.websites && filters.websites.length > 0 ? filters.websites : null
      };

      // Remove null/undefined values
      const cleanFilters = Object.fromEntries(
        Object.entries(searchFilters).filter(([_, v]) => v != null)
      );

      console.log('TopContributors - Sending filters:', cleanFilters); // Debug log

      // Use POST to send filters in request body
      const response = await fetch(`${API_BASE_URL}/api/analytics/contributors?limit=20`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: Object.keys(cleanFilters).length > 0 ? JSON.stringify(cleanFilters) : JSON.stringify({})
      });
      
      if (!response.ok) {
        throw new Error('Failed to fetch contributors');
      }
      
      const data = await response.json();
      setContributors(data.contributors || []);
    } catch (err) {
      console.error('Error fetching contributors:', err);
      setContributors([]);
    } finally {
      setLoading(false);
    }
  }, [filters]);

  useEffect(() => {
    fetchContributors();
  }, [fetchContributors]);

  if (loading) {
    return (
      <div className="top-contributors">
        <h2 style={{ color: '#fff' }}><FaTrophy style={{ marginRight: 8, color: '#bfa100' }} />Top Contributors</h2>
        <div className="loading-contributors">
          <div className="loading-spinner"></div>
          <p>Calculating contributor statistics...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="top-contributors">
      <div className="contributors-header">
        <h2 style={{ color: '#fff' }}><FaTrophy style={{ marginRight: 8, color: '#bfa100' }} />Top Contributors</h2>
        <p className="contributors-subtitle">
          Sellers with the most listings
        </p>
      </div>

      {contributors.length === 0 ? (
        <div className="no-contributors">
          <p>No contributor data available for the selected filters.</p>
          {filters.websites && filters.websites.length > 0 && (
            <p>Filtered by: {filters.websites.join(', ')}</p>
          )}
        </div>
      ) : (
        <>
          {filters.websites && filters.websites.length > 0 && (
            <div className="contributors-filter-info">
              <p>Showing contributors from: <strong>{filters.websites.join(', ')}</strong></p>
            </div>
          )}
          <div className="contributors-grid">
            {contributors.map((contributor, index) => (
              <Link
                key={contributor.seller_id || contributor.seller_name}
                to={`/analytics/contributor/${encodeURIComponent(contributor.seller_name)}?type=${contributor.contributor_type || (contributor.agency_name ? 'agency' : 'seller')}`}
                className="contributor-card"
              >
                <div className="contributor-rank">
                  #{index + 1}
                </div>
                
                <div className="contributor-info">
                  <span className="contributor-name-small">
                    {contributor.seller_name}
                  </span>
                  {contributor.website && (
                    <div className="contributor-website">{contributor.website}</div>
                  )}
                  <div className="contributor-type">
                    {contributor.contributor_type === 'agency' ? 'Agency' : 'Individual Seller'}
                  </div>
                  
                  <div className="contributor-listings">
                    <span className="listings-label">Total Listings:</span>
                    <span className="listings-value">{contributor.total_listings}</span>
                  </div>
                </div>
                
                <div className="contributor-arrow">
                  →
                </div>
              </Link>
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default TopContributors; 