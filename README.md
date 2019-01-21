# West Cork Vegetables

For my Data Centric Development project I will be creating a resource for vegetable gardeners in West Cork, Ireland, where I live.

There are many great organic vegetable growers in West Cork, some who operate on a commercial basis selling in farmers' markets or to independent shops or to restaurants or supermarkets; some who grow primarily for their own use and for their families' but sell of excess to the local wholefood shop for example; and others who grow purely for their own households and for the wonderful satisfaction in growing their own food, the feeling of vibrant life energy that comes from crunching into a freshly-dug carrot, the exuberant mouth-feel of a ripe cherry tomato lightly plucked from its cane.

So I would like to begin collating a database of vegetables that people grow in West Cork, which can be augmented by contributions from any West Cork vegetable gardeners.

For each vegetable grown, the database will store its common names, its Linnaean name, its category (leafy, root, bulb etc.), its ideal soil type (clay, sandy, loamy etc.) and moisture content (wet, dry, medium), time to sow indoors, time to plant out, time to sow outdoors, comments, tips, lists of suppliers and photographs.

Users will be able to click to display lists of vegetables filtered by different properties, e.g. "All vegetables that you sow before April in clay soil".

Registered users will be automatically approved as editors and as such will be able to edit records and add new records.   Only the database administrator will be able to delete records.

## UX
 
### User stories

- Taidhgh, new to vegetable gardening, has some time off work in April and would like to know what he can plant straightaway and get a quick crop from.

He should be able to see a list of all vegetables in the database together with a well-signposted hierarchical drop-down menu allowing him to filter his request by the above criteria and so show just the records which meet the criteria.

- Siobhan, just finished an intensive horticulture course, has just moved to West Cork with the intention of starting a business growing vegetables for restaurants.   She wants to see what other people are growing, generally get a feel of the West Cork organic growing scene, and in particular find out who's supplying good-quality seed garlic.

She should be able to display a list of all suppliers of garlic listed, i.e. a view which presents the contents of the "suppliers" field of the "garlic" record in an easily readable form

## Features

The app will be coded in Python using Flask and a MongoDB instance hosted at mLab, and deployed to Heroku.

There should be a standard view for a list of records of any length, and a different view for a single record.   Only in the single record view will the photograph and comments be displayed, for instance.   There will be a third view for lists of single fields, which we will call the field view.

## Development

I have started by beginning this README and by instantiating a database at mLab called wc-veg.   I have created two collections, "categories" and "vegetables".   I have created a single record in each collection.

I am sure that as I develop the app many ideas will occur to me for features to implement, and I will evaluate all such ideas according to their estimated usefulness and ease of implementation, allowing the app to take shape "organically".

At some point I will then consider critically whether it fulfils the original concept, whether it satisfies the project requirements, whether any functionality ought to be removed or changed and whether any new functionality is needed.

I will now continue by setting up the Python/Flask scaffolding for a database app and get basic "Hello World" functionality working. 
