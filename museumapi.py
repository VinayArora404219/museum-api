import logging
import requests
import sys

logging.basicConfig(filename='main.log', filemode='w', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.DEBUG)


class MuseumAPI:
    def __init__(self, headers=None):
        """
        :param headers: dictionary containing headers
        :return
        """
        self.headers = headers
        self.base_url = 'https://collectionapi.metmuseum.org/public/collection/v1/'

    def __fetch_response(self, endpoint, headers=None):
        """
        :param endpoint: api endpoint
        :param headers: headers to be sent in request
        :return:
        """
        response = None
        url = self.base_url + endpoint
        if headers is None:
            headers = self.headers
        try:
            response = requests.get(url, headers=headers)
        except (requests.ConnectionError, requests.Timeout) as e:
            logging.exception("Connection error or Request Timed Out: {}".format(e.args[-1]))
            sys.exit(1)
        except requests.HTTPError as httpError:
            logging.exception("HTTP Error. Status Code: {}. Error: {}".format(response.status_code, httpError.args[-1]))
            sys.exit(1)
        finally:
            logging.info("Response Status: {}".format(response.status_code))
            return response

    def get_all_objects(self):
        """
        fetches all the objects from the museum api.

        :return: a dictionary with following keys -:
        * total: int
            count of number of objects fetched from museum api
        * objectIds: list
            list of all the object ids fetched from in museum
        """
        endpoint = 'objects'
        return self.__fetch_response(endpoint).json()

    def get_object_for_id(self, object_id):
        """
        fetches an object with specified object_id from museum api.

        :param object_id: object_id of the object to fetch data from museum api
        :return: dictionary containing object detail with the following keys
        * objectID:  int
            Identifying number for each artwork (unique, can be used as key field)	437133
        * isHighlight: boolean
            When "true" indicates a popular and important artwork in the collection	Vincent van Gogh's
            "Wheat Field with Cypresses"
        * accessionNumber: string
            Identifying number for each artwork (not always unique)	"67.241"
        * accessionYear: string
            Year the artwork was acquired.	"1921"
        * isPublicDomain: boolean
            When "true" indicates an artwork in the Public Domain	Vincent van Gogh's "Wheat Field with Cypresses"
        * primaryImage: string
            URL to the primary image of an object in JPEG format
            "https://images.metmuseum.org/CRDImages/ep/original/DT1567.jpg"
        * primaryImageSmall: string
            URL to the lower-res primary image of an object in JPEG format
            "https://images.metmuseum.org/CRDImages/ep/web-large/DT1567.jpg"
        * additionalImages: array
            An array containing URLs to the additional images of an object in JPEG format	[
            "https://images.metmuseum.org/CRDImages/ep/original/LC-EP_1993_132_suppl_CH-004.jpg",
             "https://images.metmuseum.org/CRDImages/ep/original/LC-EP_1993_132_suppl_CH-003.jpg",
              "https://images.metmuseum.org/CRDImages/ep/original/LC-EP_1993_132_suppl_CH-002.jpg",
               "https://images.metmuseum.org/CRDImages/ep/original/LC-EP_1993_132_suppl_CH-001.jpg"
               ]
        * constituents: array
            An array containing the constituents associated with an object, with the constituent's role
            , name, ULAN URL, Wikidata URL, and gender, when available (currently contains female designations only).
            [
            {"constituentID": 161708,
            "role": "Artist",
            "name": "Louise Bourgeois",
            "constituentULAN_URL": "http://vocab.getty.edu/page/ulan/500057350",
            "constituentWikidata_URL": "https://www.wikidata.org/wiki/Q159409","gender": "Female"
            }
            ]
        * department: string
            Indicates The Met's curatorial department responsible for the artwork	"Egyptian Art"
        * objectName: string
            Describes the physical type of the object	"Dress", "Painting", "Photograph", or "Vase"
        * title: string
            Title, identifying phrase, or name given to a work of art	"Wheat Field with Cypresses"
        * culture: string
            Information about the culture, or people from which an object was created	"Afghan", "British",
             "North African"
        * period: string
            Time or time period when an object was created	"Ming dynasty (1368-1644)", "Middle Bronze Age"
        * dynasty: string
            Dynasty (a succession of rulers of the same line or family) under which an object was created
            "Kingdom of Benin", "Dynasty 12"
        * reign: string
            Reign of a monarch or ruler under which an object was created	"Amenhotep III", "Darius I", "Louis XVI"
        * portfolio: string
            A set of works created as a group or published as a series.	"Birds of America",
            "The Hudson River Portfolio",
             "Speculum Romanae Magnificentiae"
        * artistRole: string
            Role of the artist related to the type of artwork or object that was created	"Artist for Painting",
             "Designer for Dress"
        * artistPrefix: string
            Describes the extent of creation or describes an attribution qualifier to the information given in the
            artistRole field	"In the Style of", "Possibly by", "Written in French by"
        * artistDisplayName: string
            Artist name in the correct order for display	"Vincent van Gogh"
        * artistDisplayBio: string
            Nationality and life dates of an artist, also includes birth and death city when known.	"Dutch,
             Zundert 1853–1890 Auvers-sur-Oise"
        * artistSuffix: string
            Used to record complex information that qualifies the role of a constituent, e.g. extent of participation
            by the Constituent (verso only, and followers)	"verso only"
        * artistAlphaSort: string
            Used to sort artist names alphabetically. Last Name, First Name, Middle Name, Suffix, and Honorific fields,
            in that order.	"Gogh, Vincent van"
        * artistNationality: string
            National, geopolitical, cultural, or ethnic origins or affiliation of the creator or institution that made
            the artwork	"Spanish"; "Dutch"; "French, born Romania"
        * artistBeginDate: string
            Year the artist was born	"1840"
        * artistEndDate: string
            Year the artist died	"1926"
        * artistGender: string
            Gender of the artist (currently contains female designations only)	"female"
        * artistWikidata_URL: string
            Wikidata URL for the artist	"https://www.wikidata.org/wiki/Q694774"
        * artistULAN_URL: string
            ULAN URL for the artist	"https://vocab.getty.edu/page/ulan/500003169"
        * objectDate: string
            Year, a span of years, or a phrase that describes the specific or approximate date when an artwork was
            designed or created	"1865–67", "19th century", "ca. 1796"
        * objectBeginDate: int
            Machine readable date indicating the year the artwork was started to be created	1867, 1100, -900
        * objectEndDate: int
            Machine readable date indicating the year the artwork was completed (may be the same year or different
            year than the objectBeginDate)	1888, 1100, -850
        * medium: string
            Refers to the materials that were used to create the artwork	"Oil on canvas", "Watercolor", "Gold"
        * dimensions: string
            Size of the artwork or object	"16 x 20 in. (40.6 x 50.8 cm)"
        * dimensionsParsed: float
            Size of the artwork or object in centimeters, parsed
            [
            {
                "element":"Sheet",
                "dimensionType":"Height",
                "dimension":51
            },
            {
                "element":"Plate",
                "dimensionType":"Height",
                "dimension":47.5},
                {
                    "element":"Sheet",
                    "dimensionType":"Width",
                    "dimension":72.8
                },
                {
                    "element":"Plate",
                    "dimensionType":"Width",
                    "dimension":62.5
                }
            ]
        * measurements: array
            Array of elements, each with a name, description, and set of measurements. Spatial measurements are in
            centimeters; weights are in kg.	[
            {
            "elementName": "Overall",
            "elementDescription": "Temple proper",
            "elementMeasurements": { "Height": 640.0813, "Length": 1249.6825, "Width": 640.0813 } } ]
        * creditLine: string
            Text acknowledging the source or origin of the artwork and the year the object was acquired by the museum.
            "Robert Lehman Collection, 1975"
        * geographyType: string
            Qualifying information that describes the relationship of the place catalogued in the geography fields to
            the object that is being catalogued	"Made in", "From", "Attributed to"
        * city: string
            City where the artwork was created	"New York", "Paris", "Tokyo"
        * state: string
            State or province where the artwork was created, may sometimes overlap with County
            "Alamance", "Derbyshire", "Brooklyn"
        * county: string
            County where the artwork was created, may sometimes overlap with State	"Orange County",
            "Staffordshire", "Brooklyn"
        * country: string
            Country where the artwork was created or found	"China", "France", "India"
        * region: string
            Geographic location more specific than country, but more specific than subregion, where the artwork was
            created or found (frequently null)	"Bohemia", "Midwest", "Southern"
        * subregion: string
            Geographic location more specific than Region, but less specific than Locale, where the artwork was created
             or found (frequently null)	"Malqata", "Deir el-Bahri", "Valley of the Kings"
        * locale: string
            Geographic location more specific than subregion, but more specific than locus, where the artwork was found
             (frequently null)	"Tomb of Perneb", "Temple of Hatshepsut", "Palace of Ramesses II"
        * locus: string
            Geographic location that is less specific than locale, but more specific than excavation, where the artwork
            was found (frequently null)	"1st chamber W. wall"; "Burial C 2, In coffin"; "Pit 477"
        * excavation: string
            The name of an excavation. The excavation field usually includes dates of excavation.	"MMA excavations,
            1923–24"; "Khashaba excavations, 1910–11"; "Carnarvon excavations, 1912"
        * river: string
            River is a natural watercourse, usually freshwater, flowing toward an ocean, a lake, a sea or another river
             related to the origins of an artwork (frequently null)	"Mississippi River", "Nile River", "River Thames"
        * classification: string
            General term describing the artwork type.	"Basketry", "Ceramics", "Paintings"
        * rightsAndReproduction: string
            Credit line for artworks still under copyright.	"© 2018 Estate of Pablo Picasso / Artists Rights Society
            (ARS), New York"
        * linkResource: string
            URL to object's page on metmuseum.org	"https://www.metmuseum.org/art/collection/search/547802"
        * metadataDate: datetime
            Date metadata was last updated	2018-10-17T10:24:43.197Z
        * repository: string
            "Metropolitan Museum of Art, New York, NY"
        * objectURL: string
            URL to object's page on metmuseum.org	"https://www.metmuseum.org/art/collection/search/547802"
        * tags: array
            An array of subject keyword tags associated with the object and their respective AAT URL
            [
                {
                    "term": "Abstraction",
                    "AAT_URL": "http://vocab.getty.edu/page/aat/300056508",
                    "Wikidata_URL": "https://www.wikidata.org/wiki/Q162150"
                }
            ]
        * objectWikidata_URL: string
            Wikidata URL for the object	"https://www.wikidata.org/wiki/Q432253"
        * isTimelineWork: boolean
            Whether the object is on the Timeline of Art History website	true
        * GalleryNumber: string
            Gallery number, where available	"131"
        """

        endpoint = "objects/" + str(object_id)
        return self.__fetch_response(endpoint).json()
