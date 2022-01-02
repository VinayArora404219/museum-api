# Museum API 

Museum API allows you to easily get objects from the museum api through python objects
without needing you to send requests to its api endpoints using requests module.

# **Installation**
**To install the package, execute** 
```commandline
pip3 install -i https://test.pypi.org/simple/ museum-api-package==0.0.9
```

# **Usage**

```
from museum_api import MuseumAPI
m = MuseumAPI()
```

## **Usage examples:**

To fetch all the object ids of all the objects available on Museum API:
```
# fetches all the object ids from Museum API.
object_ids = m.get_all_object_ids()
```
variable object_ids will not be set to:
```
    {
	"total": 471581,
	"objectIDs": [
		1,
		2,
		3,
		4,
		5,
		6,
		7,
		8,
		9,
		10,
		// more results ...
	]
}
```

To fetch the details of an object for particular object id:

```
# fetches all the object ids from Museum API.
object_data = m.get_object_for_id(45734)
```
object_data will be set to:
```
    {
    "objectID": 45734,
    "isHighlight": false,
    "accessionNumber": "36.100.45",
    "accessionYear": "1936",
    "isPublicDomain": true,
    "primaryImage": "https://images.metmuseum.org/CRDImages/as/original/DP251139.jpg",
    "primaryImageSmall": "https://images.metmuseum.org/CRDImages/as/web-large/DP251139.jpg",
    "additionalImages": [
        "https://images.metmuseum.org/CRDImages/as/original/DP251138.jpg",
        "https://images.metmuseum.org/CRDImages/as/original/DP251120.jpg"
    ],
    "constituents": [
        {
            "constituentID": 11986,
            "role": "Artist",
            "name": "Kiyohara Yukinobu",
            "constituentULAN_URL": "http://vocab.getty.edu/page/ulan/500034433",
            "constituentWikidata_URL": "https://www.wikidata.org/wiki/Q11560527",
            "gender": "Female"
        }
    ],
    "department": "Asian Art",
    "objectName": "Hanging scroll",
    "title": "Quail and Millet",
    "culture": "Japan",
    "period": "Edo period (1615–1868)",
    "dynasty": "",
    "reign": "",
    "portfolio": "",
    "artistRole": "Artist",
    "artistPrefix": "",
    "artistDisplayName": "Kiyohara Yukinobu",
    "artistDisplayBio": "Japanese, 1643–1682",
    "artistSuffix": "",
    "artistAlphaSort": "Kiyohara Yukinobu",
    "artistNationality": "Japanese",
    "artistBeginDate": "1643",
    "artistEndDate": "1682",
    "artistGender": "Female",
    "artistWikidata_URL": "https://www.wikidata.org/wiki/Q11560527",
    "artistULAN_URL": "http://vocab.getty.edu/page/ulan/500034433",
    "objectDate": "late 17th century",
    "objectBeginDate": 1667,
    "objectEndDate": 1682,
    "medium": "Hanging scroll; ink and color on silk",
    "dimensions": "46 5/8 x 18 3/4 in. (118.4 x 47.6 cm)",
    "measurements": [
        {
            "elementName": "Overall",
            "elementDescription": null,
            "elementMeasurements": {
                "Height": 118.4,
                "Width": 47.6
            }
        }
    ],
    "creditLine": "The Howard Mansfield Collection, Purchase, Rogers Fund, 1936",
    "geographyType": "",
    "city": "",
    "state": "",
    "county": "",
    "country": "",
    "region": "",
    "subregion": "",
    "locale": "",
    "locus": "",
    "excavation": "",
    "river": "",
    "classification": "Paintings",
    "rightsAndReproduction": "",
    "linkResource": "",
    "metadataDate": "2020-09-14T12:26:37.48Z",
    "repository": "Metropolitan Museum of Art, New York, NY",
    "objectURL": "https://www.metmuseum.org/art/collection/search/45734",
    "tags": [
        {
            "term": "Birds",
            "AAT_URL": "http://vocab.getty.edu/page/aat/300266506",
            "Wikidata_URL": "https://www.wikidata.org/wiki/Q5113"
        }
    ],
    "objectWikidata_URL": "https://www.wikidata.org/wiki/Q29910832",
    "isTimelineWork": false,
    "GalleryNumber": ""
}
```


**Test**

Run tests with:
```
    python3 tests/test_museumapi.py
    python3 tests/test_utils.py
```

# LICENSE
***
[MIT](LICENSE)








