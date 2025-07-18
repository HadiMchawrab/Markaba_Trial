import scrapy



class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class DubizzleItem(scrapy.Item):
    # ——— Core identifiers ———
    ad_id                = scrapy.Field()  # Dubizzle’s ID (e.g. “110465826”)
    url                  = scrapy.Field()
    website              = scrapy.Field()  # “dubizzle”

    # ——— JSON-LD fields ———
    name                 = scrapy.Field()  # JSON-LD “name”
    sku                  = scrapy.Field()  # JSON-LD “sku”
    description          = scrapy.Field()
    image_urls           = scrapy.Field()  # list of JSON-LD “image” URLs
    price                = scrapy.Field()
    currency             = scrapy.Field()  # “SAR”
    price_valid_until    = scrapy.Field()  # ISO timestamp from offers.priceValidUntil


    # ——— Basic info & specs ———
    title                = scrapy.Field()
    brand                = scrapy.Field()
    model                = scrapy.Field()
    trim                 = scrapy.Field()

    year                 = scrapy.Field()
    mileage              = scrapy.Field()  # from mileageFromOdometer.value
    mileage_unit         = scrapy.Field()  # from mileageFromOdometer.unitCode
    fuel_type            = scrapy.Field()
    transmission_type    = scrapy.Field()
    body_type            = scrapy.Field()
    condition            = scrapy.Field()  # e.g. “used”/“new”
    new_used             = scrapy.Field()  # same as condition
    color                = scrapy.Field()
    source               = scrapy.Field()

    # ——— Usage & ownership ———
    kilometers           = scrapy.Field()  # duplicate of mileage
    doors                = scrapy.Field()
    seats                = scrapy.Field()
    owners               = scrapy.Field()
    interior             = scrapy.Field()
    air_con              = scrapy.Field()
    ownership_type       = scrapy.Field()  # “freehold” / “non-freehold”

    # ——— Price breakdown ———

    price_type           = scrapy.Field()  # “price” / “rental”

    # ——— Seller & agency ———
    seller               = scrapy.Field()  # e.g. “OLX user”
    seller_type          = scrapy.Field()  # “private” / “business”
    seller_verified      = scrapy.Field()  # yes/no
    seller_id            = scrapy.Field()
    agency_id            = scrapy.Field()
    agency_name          = scrapy.Field()
    is_agent             = scrapy.Field()  # from dataLayer

    # ——— Location ———
    location_city        = scrapy.Field()  # “Riyadh”
    location_region      = scrapy.Field()  # e.g. governorate/neighborhood
    loc_id               = scrapy.Field()  # “2-74”
    loc_name             = scrapy.Field()  # same as city
    loc_breadcrumb       = scrapy.Field()  # raw “;0-1;1-62;2-74;”
    loc_1_id             = scrapy.Field()
    loc_1_name           = scrapy.Field()
    loc_2_id             = scrapy.Field()
    loc_2_name           = scrapy.Field()

    # ——— Category & page meta ———
    category_1_id        = scrapy.Field()
    category_1_name      = scrapy.Field()
    category_2_id        = scrapy.Field()
    category_2_name      = scrapy.Field()
    page_type            = scrapy.Field()  # “offerdetail”
    website_section      = scrapy.Field()  # “main_site”

    # ——— Media & extras ———
    image_url            = scrapy.Field()  # first/thumb
    number_of_images     = scrapy.Field()  # count of photos
    has_video            = scrapy.Field()  # yes/no
    has_panorama         = scrapy.Field()  # yes/no
    deliverable          = scrapy.Field()  # yes/no
    delivery_option      = scrapy.Field()  # raw value if any

    # ——— Timing ———
    post_date            = scrapy.Field()  # from JSON-LD or dataLayer
    date_scraped = scrapy.Field()

class OpenSooqItem(scrapy.Item):

    ad_id                = scrapy.Field()
    url                  = scrapy.Field()
    website              = scrapy.Field()
    name                 = scrapy.Field()
    title                = scrapy.Field()
    price                = scrapy.Field()

    currency                = scrapy.Field()
    brand                  = scrapy.Field()
    model              = scrapy.Field()
    year                 = scrapy.Field()
    trim                = scrapy.Field()

    mileage                = scrapy.Field()
    mileage_unit                  = scrapy.Field()
    fuel_type              = scrapy.Field()
    transmission_type                 = scrapy.Field()


    condition                = scrapy.Field()
    color                  = scrapy.Field()
    location_city                = scrapy.Field()

    location_region                = scrapy.Field()
    image_url                  = scrapy.Field()


    date_scraped                = scrapy.Field()

    engine_size                 = scrapy.Field()
    body_type            = scrapy.Field()
    payment_method       = scrapy.Field()

    seats                = scrapy.Field()
    interior_color       = scrapy.Field()

    source               = scrapy.Field()
    paint_quality        = scrapy.Field()
    body_condition       = scrapy.Field()
    category             = scrapy.Field()
    subcategory          = scrapy.Field()

    interior_options     = scrapy.Field()
    exterior_options     = scrapy.Field()
    technology_options   = scrapy.Field()

    description         = scrapy.Field()

    seller              = scrapy.Field()
    seller_type          = scrapy.Field()
    seller_url           = scrapy.Field()
    seller_id            = scrapy.Field()
    is_shop               = scrapy.Field()
    is_pro_buyer        = scrapy.Field()
    seller_verified      = scrapy.Field()
    rating_avg          = scrapy.Field()
    number_of_ratings   = scrapy.Field()
    seller_joined          = scrapy.Field()
    response_time         = scrapy.Field()




     # ——— Timing ———
    post_date            = scrapy.Field()  # from JSON-LD or dataLayer
    date_scraped         = scrapy.Field()

    image_url            = scrapy.Field()  # first/thumb
    number_of_images     = scrapy.Field()  # count of photos
    has_video            = scrapy.Field()  # yes/no
    has_panorama         = scrapy.Field()  # yes/no
    price_valid_until    = scrapy.Field()  # ISO timestamp from serp['listings']['meta'][1]
    listing_status       = scrapy.Field()
    user_target_type = scrapy.Field() #Free/Sponsored
    post_map      = scrapy.Field()



class CarSwitchItem(scrapy.Item):
    # ——— Core identifiers ———
    ad_id              = scrapy.Field()  # unique listing ID
    url                = scrapy.Field()  # listing URL
    website            = scrapy.Field()  # e.g. "CarSwitch"

    # ——— Listing basics ———
    title              = scrapy.Field()  # listing title
    price              = scrapy.Field()  # numeric price
    currency           = scrapy.Field()  # currency code, e.g. "AED"

    # ——— Vehicle specs ———
    brand              = scrapy.Field()
    model              = scrapy.Field()
    year               = scrapy.Field()  # int
    trim               = scrapy.Field()

    mileage            = scrapy.Field()  # int
    mileage_unit       = scrapy.Field()  # e.g. "km", "mi"
    fuel_type          = scrapy.Field()
    transmission_type  = scrapy.Field()
    body_type          = scrapy.Field()
    condition          = scrapy.Field()  # e.g. "used"/"new"
    color              = scrapy.Field()

    # ——— Seller info ———
    seller             = scrapy.Field()  # seller name
    seller_type        = scrapy.Field()  # "private" vs "dealer"

    # ——— Location ———
    location_city      = scrapy.Field()
    location_region    = scrapy.Field()

    # ——— Media & timing ———
    image_url          = scrapy.Field()  # primary image URL
    number_of_images   = scrapy.Field()  # int count of images
    post_date          = scrapy.Field()  # datetime of listing
    date_scraped       = scrapy.Field()  # datetime when scraped


    # --- Extra Features ---
    secondary_id = scrapy.Field()
    regional_specs = scrapy.Field()
    uuid = scrapy.Field()
    cylinders = scrapy.Field()
    engine_size = scrapy.Field()
    asking_price = scrapy.Field()
    is_paid = scrapy.Field()
    is_featured = scrapy.Field()
    drive_type = scrapy.Field()
    variant = scrapy.Field()
    seats =scrapy.Field()
    listing_rank = scrapy.Field()
    status = scrapy.Field()
    zoho_car_id = scrapy.Field()

    overall_condition = scrapy.Field()
    is_accidented = scrapy.Field()
    accident_detail = scrapy.Field()
    air_bags_condition = scrapy.Field()
    chassis_condition = scrapy.Field()
    engine_condition = scrapy.Field()
    gear_box_condition = scrapy.Field()
    service_history = scrapy.Field()
    service_history_verified = scrapy.Field()
    crossed_price = scrapy.Field()
    last_price = scrapy.Field()

    original_success_fee = scrapy.Field()
    final_success_fee = scrapy.Field()
    success_fee_type = scrapy.Field()
    success_fee_promo_code = scrapy.Field()
    price_dropped_badge = scrapy.Field()
    price_dropped_badge_expiration = scrapy.Field()
    alloy_rims = scrapy.Field()
    rim_size = scrapy.Field()
    roof_type = scrapy.Field()
    no_of_keys = scrapy.Field()
    currently_financed = scrapy.Field()
    bank_name = scrapy.Field()
    cash_buyer_only = scrapy.Field()
    warranty = scrapy.Field()
    warranty_expiration_date = scrapy.Field()
    warranty_mileage_limit = scrapy.Field()
    service_contract = scrapy.Field()
    service_contract_verified = scrapy.Field()
    classified_web_link = scrapy.Field()
    special_about_car = scrapy.Field()
    registration_city_name = scrapy.Field()

    cappasity_link = scrapy.Field()
    first_owner = scrapy.Field()
    fair_value_override = scrapy.Field()
    inspection_started_by = scrapy.Field()
    seller_nationality = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    # warranty_detail = scrapy.Field() FUTURE
    #emi_detail = scrapy.Field(). FUTURE
    buyer_services = scrapy.Field()
    # fair_value_object = scrapy.Field()
    show_all_details = scrapy.Field()


    #fair_value_car = scrapy.Field(). FUTURE
    fair_value_computation_id = scrapy.Field()
    fair_value = scrapy.Field()
    confidence = scrapy.Field()
    explanation_en = scrapy.Field()
    explanation_ar = scrapy.Field()
    #recent_transactions = scrapy.Field()
    min_fair_value = scrapy.Field()
    max_fair_value = scrapy.Field()



class SyarahItem():

     # ——— Core identifiers ———
    ad_id              = scrapy.Field()  # unique listing ID
    url                = scrapy.Field()  # listing URL
    website            = scrapy.Field()  # e.g. "CarSwitch"

    # ——— Listing basics ———
    title              = scrapy.Field()  # listing title
    price              = scrapy.Field()  # numeric price
    currency           = scrapy.Field()  # currency code, e.g. "AED"

    # ——— Vehicle specs ———
    brand              = scrapy.Field()
    model              = scrapy.Field()
    year               = scrapy.Field()  # int
    trim               = scrapy.Field()

    mileage            = scrapy.Field()  # int
    mileage_unit       = scrapy.Field()  # e.g. "km", "mi"
    fuel_type          = scrapy.Field()
    transmission_type  = scrapy.Field()
    body_type          = scrapy.Field()
    condition          = scrapy.Field()  # e.g. "used"/"new"
    color              = scrapy.Field()

    # ——— Seller info ———
    seller             = scrapy.Field()  # seller name
    seller_type        = scrapy.Field()  # "private" vs "dealer"

    # ——— Location ———
    location_city      = scrapy.Field()
    location_region    = scrapy.Field()

    # ——— Media & timing ———
    image_url          = scrapy.Field()  # primary image URL
    number_of_images   = scrapy.Field()  # int count of images
    post_date          = scrapy.Field()  # datetime of listing
    date_scraped       = scrapy.Field()  # datetime when scraped


    is_sold            = scrapy.Field()
    is_deleted         = scrapy.Field()
    is_preowned        = scrapy.Field()

    interior_color     = scrapy.Field()
    source             = scrapy.Field()
    cylinders          = scrapy.Field()
    engine_size        = scrapy.Field()
    drive_type         = scrapy.Field()
    number_of_keys     = scrapy.Field()
    seats              = scrapy.Field()
    engine_type        = scrapy.Field()







