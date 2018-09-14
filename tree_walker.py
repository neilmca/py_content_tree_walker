#! /usr/bin/env python

import requests
import os
import json
import datetime
import sys
import getopt

import warnings
warnings.filterwarnings("ignore")

#README
# Need to have the requests module installed
# Use VirtualEnv
# 1. python -m virtualenv env
# 2. (Activate the environment) env\Scripts\activate
# 3. install requests pip install requests

#Example calls
#python tree_walker.py -a <api_key> -i news/business -t > business_t.json
#python tree_walker.py -a <api_key> -i news/business -c > business_c.json

TEST_CONTENT_JSON = {
    "results": [
        {
            "title": "Business",
            "summary": "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
            "type": "IDX",
            "lastUpdated": "2018-09-13T12:37:05+00:00",
            "firstCreated": "2010-03-09T09:46:51+00:00",
            "firstPublished": "2010-07-06T07:34:26+00:00",
            "lastPublished": "2018-09-13T12:37:12+00:00",
            "changeQueueId": "127463484",
            "changeQueueTimestamp": "2018-09-13T12:37:05+00:00",
            "groups": [
                {
                    "type": "container-top-stories",
                    "title": "Top Stories",
                    "items": [
                        {
                            "assetId": "45506322",
                            "assetUri": "/news/business-45506322",
                            "firstCreated": "2018-09-13T06:17:01+00:00",
                            "hasShortForm": True,
                            "headline": "John Lewis half-year profits slump 99%",
                            "includeComments": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T09:02:19+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103405163": {
                                            "height": 432,
                                            "width": 768,
                                            "href": "http://c.files.bbci.co.uk/8D36/production/_103405163_9yniarol.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "John Lewis store",
                                            "copyrightHolder": "Reuters",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "prominence": "standard",
                            "relatedGroups": [
                                {
                                    "type": "index",
                                    "items": [
                                        {
                                            "assetId": "45509122",
                                            "assetUri": "/news/business-45509122",
                                            "firstCreated": "2018-09-13T12:26:19+00:00",
                                            "headline": "Is 'Never knowingly undersold' killing John Lewis?",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-13T12:26:19+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "John Lewis Partnership is under pressure to question the slogan that arguably defines its business model.",
                                            "type": "STY"
                                        },
                                        {
                                            "assetId": "45506500",
                                            "assetUri": "/news/business-45506500",
                                            "firstCreated": "2018-09-13T10:13:16+00:00",
                                            "hasShortForm": True,
                                            "headline": "John Lewis boss rejects Raab Brexit jibe",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-13T10:13:16+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "The Brexit secretary says it is a mistake for businesses that \"aren't doing so well\" to blame Brexit.",
                                            "type": "STY"
                                        },
                                        {
                                            "assetId": "45507743",
                                            "assetUri": "/news/business-45507743",
                                            "firstCreated": "2018-09-13T11:01:02+00:00",
                                            "headline": "Discount matching undermined profits says John Lewis's Charlie Mayfield",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-13T11:01:02+00:00",
                                            "mediaType": "Video",
                                            "overtypedHeadline": "Discount matching 'undermined profits'",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "John Lewis's Charlie Mayfield tells the BBC matching rivals' deep discounting wiped out profits.",
                                            "type": "MAP"
                                        }
                                    ]
                                }
                            ],
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "fff",
                            "type": "STY"
                        },
                        {
                            "assetId": "45504521",
                            "assetUri": "/news/business-45504521",
                            "byline": {
                                "name": "By Simon Jack",
                                "persons": [
                                    {
                                        "name": "Simon Jack",
                                        "correspondentId": "simonjack",
                                        "url": "/news/correspondents/simonjack",
                                        "function": "Business editor",
                                        "thumbnail": "http://c.files.bbci.co.uk/11D8C/production/_103300137_sj.jpg",
                                        "twitterName": "BBCSimonJack",
                                        "originCode": "CPSPRODPB"
                                    }
                                ],
                                "title": "Business editor"
                            },
                            "firstCreated": "2018-09-13T04:08:08+00:00",
                            "hasShortForm": True,
                            "headline": "Gordon Brown warns about next crisis",
                            "includeComments": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T04:08:08+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103407905": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/C71A/production/_103407905_brown_crop.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Gordon Brown",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "prominence": "standard",
                            "relatedGroups": [
                                {
                                    "type": "index",
                                    "items": [
                                        {
                                            "assetId": "45502084",
                                            "assetUri": "/news/business-45502084",
                                            "firstCreated": "2018-09-12T16:03:58+00:00",
                                            "hasShortForm": True,
                                            "headline": "Hammond: Financial crisis 'shock' continues",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-12T16:03:58+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "The UK's chancellor admits peoples' incomes are suffering, but sees \"light at the end of the tunnel\".",
                                            "type": "STY"
                                        },
                                        {
                                            "assetId": "45491533",
                                            "assetUri": "/news/business-45491533",
                                            "firstCreated": "2018-09-12T04:00:44+00:00",
                                            "headline": "Carney warns against complacency",
                                            "includeComments": True,
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-12T04:00:44+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "The Governor of the Bank of England tells the BBC there are four risks to financial stability.",
                                            "type": "CSP"
                                        }
                                    ]
                                }
                            ],
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The former prime minister tells the BBC that the world is sleepwalking into another financial crisis.",
                            "type": "CSP"
                        },
                        {
                            "assetId": "45449121",
                            "assetUri": "/news/live/business-45449121",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "C04C872673DC044C8185E6CF867033AD",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45449127_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45449127_HighWeb",
                                    "highweb": "bbc.cps.asset.45449127_HighWeb",
                                    "mobile": "bbc.cps.asset.45449127_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-09-07T11:25:41+00:00",
                            "headline": "Business Live: Lira jumps on rate rise",
                            "isLive": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-07T11:25:41+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103411735": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/D1CF/production/_103411735_turkishlira.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Turkish lira",
                                            "copyrightHolder": "Reuters",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "prominence": "standard",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Turkish currency rebounds after the central bank defies President Erdogan and lifts interest rates.",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45508563",
                            "assetUri": "/news/business-45508563",
                            "firstCreated": "2018-09-13T11:03:02+00:00",
                            "hasShortForm": True,
                            "headline": "Bank holds rates amid Brexit uncertainty",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T12:09:12+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103407089": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/17F16/production/_103407089_gettyimages-154742233.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Bank of England",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Policymakers at the Bank of England vote 9-0 to leave rates at 0.75% after last month's increase.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45510553",
                            "assetUri": "/news/business-45510553",
                            "byline": {
                                "name": "By Bill Wilson",
                                "persons": [
                                    {
                                        "name": "Bill Wilson",
                                        "function": "Business reporter, BBC News",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter, BBC News"
                            },
                            "firstCreated": "2018-09-13T12:05:12+00:00",
                            "hasShortForm": True,
                            "headline": "Premier League signs Coca-Cola as sponsor",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T12:05:12+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103152509": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/1619D/production/_103152509_gettyimages-932072196.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Man holding Coca-Cola branded football",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "England's top football league signs a three-and-a-half-year agreement with Coke, which starts in January.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45508672",
                            "assetUri": "/news/world-europe-45508672",
                            "firstCreated": "2018-09-13T11:23:25+00:00",
                            "hasShortForm": True,
                            "headline": "Turkey bans foreign tender for home sales",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T12:23:03+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103409260": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/1892/production/_103409260_gettyimages-1024421868.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Turkish Lira currency in Istanbul, Turkey, 27 August 2018",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Europe",
                                "id": "99123",
                                "uri": "/news/world/europe",
                                "urlIdentifier": "/news/world/europe"
                            },
                            "summary": "Property contracts must now be agreed in lira as President Erdogan moves to revive the currency.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45506492",
                            "assetUri": "/news/business-45506492",
                            "firstCreated": "2018-09-13T06:28:09+00:00",
                            "hasShortForm": True,
                            "headline": "Morrisons sales soar as revival continues",
                            "includeComments": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T07:06:03+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103405275": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/DFA2/production/_103405275_morrisons.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Morrisons",
                                            "copyrightHolder": "Reuters",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The UK's fourth-biggest supermarket reports its best quarterly sales increase for almost a decade.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45506500",
                            "assetUri": "/news/business-45506500",
                            "firstCreated": "2018-09-13T10:13:16+00:00",
                            "hasShortForm": True,
                            "headline": "John Lewis boss rejects Raab Brexit jibe",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T10:13:16+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103405776": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/108A6/production/_103405776_raab.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Dominic Raab",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The Brexit secretary says it is a mistake for businesses that \"aren't doing so well\" to blame Brexit.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45498235",
                            "assetUri": "/news/business-45498235",
                            "byline": {
                                "name": "By Simon Jack",
                                "persons": [
                                    {
                                        "name": "Simon Jack",
                                        "correspondentId": "simonjack",
                                        "url": "/news/correspondents/simonjack",
                                        "function": "Business editor",
                                        "thumbnail": "http://c.files.bbci.co.uk/11D8C/production/_103300137_sj.jpg",
                                        "twitterName": "BBCSimonJack",
                                        "originCode": "CPSPRODPB"
                                    }
                                ],
                                "title": "Business editor"
                            },
                            "firstCreated": "2018-09-13T06:12:26+00:00",
                            "hasShortForm": True,
                            "headline": "Bob Diamond defends risk-taking banks",
                            "includeComments": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T06:12:26+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103392092": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/7165/production/_103392092_bobdiamond.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Bob Diamond",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                    "categoryName": "Analysis"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Former Barclays boss Bob Diamond says risk-averse banks can't create jobs and economic growth.",
                            "type": "CSP"
                        },
                        {
                            "assetId": "45508162",
                            "assetUri": "/news/technology-45508162",
                            "firstCreated": "2018-09-13T09:47:22+00:00",
                            "hasShortForm": True,
                            "headline": "Huawei promises foldable phone within year",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T09:47:22+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103407278": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/154E6/production/_103407278_gettyimages-1027412410.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Huawei has not yet released any firm details about its foldable device",
                                            "altText": "A Huawei phone in front of the company logo",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Technology",
                                "id": "99113",
                                "uri": "/news/technology",
                                "urlIdentifier": "/news/technology"
                            },
                            "summary": "The chief executive of the Chinese firm has said it is developing a device with a fold-out screen.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45505522",
                            "assetUri": "/news/world-asia-china-45505522",
                            "firstCreated": "2018-09-13T05:34:46+00:00",
                            "hasShortForm": True,
                            "headline": "Dead rat in soup costs restaurant $190m",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T05:34:46+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103404576": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/107D4/production/_103404576_raterswr.png",
                                            "originCode": "cpsprodpb",
                                            "caption": "The dead rat was fished out a pot of boiling broth",
                                            "altText": "Rat found in hotpot",
                                            "copyrightHolder": "Weibo",
                                            "allowSyndication": False
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "China",
                                "id": "101361",
                                "uri": "/news/world/asia/china",
                                "urlIdentifier": "/news/world/asia/china"
                            },
                            "summary": "A pregnant woman in China found the boiled rat in her dish after she had taken a few bites.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45502465",
                            "assetUri": "/news/technology-45502465",
                            "byline": {
                                "name": "By Leo Kelion",
                                "persons": [
                                    {
                                        "name": "Leo Kelion",
                                        "function": "Technology desk editor",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Technology desk editor"
                            },
                            "firstCreated": "2018-09-12T17:17:30+00:00",
                            "hasShortForm": True,
                            "headline": "Apple unveils iPhone XS and new Watch",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T20:24:06+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103401824": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/A73A/production/_103401824_33ca92d3-9cc3-4459-ba64-5e68883f21fd.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Two iPhone XS phones",
                                            "copyrightHolder": "Apple",
                                            "allowSyndication": False
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Technology",
                                "id": "99113",
                                "uri": "/news/technology",
                                "urlIdentifier": "/news/technology"
                            },
                            "summary": "Three new iPhone models are revealed plus a fall-detecting smartwatch.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45500384",
                            "assetUri": "/news/business-45500384",
                            "firstCreated": "2018-09-12T14:42:21+00:00",
                            "hasShortForm": True,
                            "headline": "RBS bailout 'unlikely to be recouped'",
                            "includeComments": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T14:42:21+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103397928": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/14423/production/_103397928_rbsmoneygettyimages-864993966-1.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "RBS cash machines",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Chairman Sir Howard Davies says the bank was rescued to save the financial system, not as an investment.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45502084",
                            "assetUri": "/news/business-45502084",
                            "firstCreated": "2018-09-12T16:03:58+00:00",
                            "hasShortForm": True,
                            "headline": "Hammond: Financial crisis 'shock' continues",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T16:03:58+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103402319": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/164B8/production/_103402319_mediaitem103399867.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Philip Hammond",
                                            "copyrightHolder": "Reuters",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The UK's chancellor admits peoples' incomes are suffering, but sees \"light at the end of the tunnel\".",
                            "type": "STY"
                        },
                        {
                            "assetId": "45505232",
                            "assetUri": "/news/business-45505232",
                            "firstCreated": "2018-09-13T05:15:26+00:00",
                            "hasShortForm": True,
                            "headline": "Dairy giant Fonterra posts first loss",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T05:15:26+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103404385": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/E3E4/production/_103404385_gettyimages-1032378322-1.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Cow eating grass on a dairy farm",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The New Zealand co-operative said it let down farmers with overly optimistic financial forecasts.",
                            "type": "STY"
                        }
                    ],
                    "semanticGroupName": "Top Stories"
                },
                {
                    "type": "single-section-digest",
                    "title": "News event promotion - Topic cluster",
                    "strapline": {
                        "name": "Business Live archive"
                    },
                    "items": [
                        {
                            "assetId": "45448971",
                            "assetUri": "/news/live/business-45448971",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "A92A42338226EC49A171FA2025CC6A3A",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45448977_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45448977_HighWeb",
                                    "highweb": "bbc.cps.asset.45448977_HighWeb",
                                    "mobile": "bbc.cps.asset.45448977_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-09-07T11:19:41+00:00",
                            "headline": "Business Live: US stocks fall",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-07T11:19:41+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103401791": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/4CFE/production/_103401791_gettyimages-1027897154-2.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "US trader",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Wednesday 12 September",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Wall Street slips as hopes over a breakthrough on US-China trade are overshadowed by fears about tougher tech regulation.",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45448411",
                            "assetUri": "/news/live/business-45448411",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "4A4E0CAEB4D4B142B60742A197F6C6B8",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45448412_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45448412_HighWeb",
                                    "highweb": "bbc.cps.asset.45448412_HighWeb",
                                    "mobile": "bbc.cps.asset.45448412_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-09-07T11:11:56+00:00",
                            "headline": "Business Live: US stocks climb",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-07T11:11:56+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103386472": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/6B4C/production/_103386472_gettyimages-1027897172-1.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "US traders",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Tuesday 11 September",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Wall Street boosted by energy companies and technology stocks, but trade war fears linger.",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45444511",
                            "assetUri": "/news/live/business-45444511",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "8D50366EEF17EC44B9476821CE8C6ECF",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45444517_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45444517_HighWeb",
                                    "highweb": "bbc.cps.asset.45444517_HighWeb",
                                    "mobile": "bbc.cps.asset.45444517_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-09-07T10:41:39+00:00",
                            "headline": "Business Live: US stocks mixed at close",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-07T10:41:39+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103367176": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/10668/production/_103367176_gettyimages-1027897146.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "US trader",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Monday 10 September",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The S&P and Nasdaq close higher, but the Dow Jones lags.",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45369144",
                            "assetUri": "/news/live/business-45369144",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "2EE0FABDF6A7CA458D57C01155AD9D8F",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45369145_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45369145_HighWeb",
                                    "highweb": "bbc.cps.asset.45369145_HighWeb",
                                    "mobile": "bbc.cps.asset.45369145_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-09-05T04:28:15+00:00",
                            "headline": "Business Live: US stocks hit by Trump threat",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-05T04:28:15+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103341053": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/88C6/production/_103341053_gettyimages-1027286354.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Donald Trump",
                                            "copyrightHolder": "Mark Wilson",
                                            "allowSyndication": False
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Friday 7 September",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The US President's warning sends Wall St lower; Tesla shares sink",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45368971",
                            "assetUri": "/news/live/business-45368971",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "69AC1ADEFBFDCE49B36700863C01466B",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45369142_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45369142_HighWeb",
                                    "highweb": "bbc.cps.asset.45369142_HighWeb",
                                    "mobile": "bbc.cps.asset.45369142_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-09-05T04:28:02+00:00",
                            "headline": "Business Live: Tech stocks drag on Wall Street",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-05T04:28:02+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103320565": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/DCB6/production/_103320565_gettyimages-1026614196.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Twitter logo",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Thursday 6 September",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Shares in social media firms continue to fall amid fears of tougher regulation, with Twitter down almost 6%.",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45368965",
                            "assetUri": "/news/live/business-45368965",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "A5F26F2D287C0A45926EA7B816014431",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45368966_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45368966_HighWeb",
                                    "highweb": "bbc.cps.asset.45368966_HighWeb",
                                    "mobile": "bbc.cps.asset.45368966_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-09-04T01:22:09+00:00",
                            "headline": "Business Live: Pound picks up speed",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-04T01:22:09+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "102874328": {
                                            "height": 945,
                                            "width": 1680,
                                            "href": "http://c.files.bbci.co.uk/141AB/production/_102874328_euro.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Pound/Euro",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Tuesday 4 September",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Sterling climbs against the euro and shrugs off losses against the dollar.",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45368962",
                            "assetUri": "/news/live/business-45368962",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "11632FD2A0F17340AD555243B6F866CD",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45368963_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45368963_HighWeb",
                                    "highweb": "bbc.cps.asset.45368963_HighWeb",
                                    "mobile": "bbc.cps.asset.45368963_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-09-03T04:49:58+00:00",
                            "headline": "Business Live: FTSE up, pound down",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-03T04:49:58+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103273391": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/4B89/production/_103273391_gettyimages-860933824.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Sterling coins",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Monday 3 September",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "fffff",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45321926",
                            "assetUri": "/news/live/business-45321926",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "77589B4B4771C342B5DE4969072A6EE5",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45321927_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45321927_HighWeb",
                                    "highweb": "bbc.cps.asset.45321927_HighWeb",
                                    "mobile": "bbc.cps.asset.45321927_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-08-31T00:40:00+00:00",
                            "headline": "Business Live: FTSE falters",
                            "language": "en-gb",
                            "lastUpdated": "2018-08-31T00:40:00+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103241923": {
                                            "height": 945,
                                            "width": 1680,
                                            "href": "http://c.files.bbci.co.uk/8092/production/_103241923_gettyimages-1001077662.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Canary Wharf",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Friday 31 August",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Investors have welcomed Whitbread's sale of Costa, but the wider market is lower.",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45319881",
                            "assetUri": "/news/live/business-45319881",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "1F20F1167040A543A7EC99B900288FEA",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45321922_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45321922_HighWeb",
                                    "highweb": "bbc.cps.asset.45321922_HighWeb",
                                    "mobile": "bbc.cps.asset.45321922_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-08-30T04:16:39+00:00",
                            "headline": "Apple 'to unveil new iPhone models'",
                            "language": "en-gb",
                            "lastUpdated": "2018-08-30T04:16:39+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "102777561": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/40C1/production/_102777561_hi048428260.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "In this file photo taken on September 22, 2017 an Apple logo is seen on the outside of an Apple store in San Francisco, California.",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Thursday 30 August",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Apple is to hold an event on 12 September where it is expected to unveil new iPhone models, Reuters reports.",
                            "type": "LIV"
                        },
                        {
                            "assetId": "45220717",
                            "assetUri": "/news/live/business-45220717",
                            "commentary": {
                                "order": "descending",
                                "assetUUID": "FB23ED1D23A0DD458E834A258379F805",
                                "channels": {
                                    "enhancedmobile": "bbc.cps.asset.45220724_EnhancedMobile",
                                    "desktop": "bbc.cps.asset.45220724_HighWeb",
                                    "highweb": "bbc.cps.asset.45220724_HighWeb",
                                    "mobile": "bbc.cps.asset.45220724_EnhancedMobile"
                                }
                            },
                            "firstCreated": "2018-08-17T08:22:49+00:00",
                            "headline": "US dollar falls on Fed comments",
                            "language": "en-gb",
                            "lastUpdated": "2018-08-17T08:22:49+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103163372": {
                                            "height": 432,
                                            "width": 768,
                                            "href": "http://c.files.bbci.co.uk/6AC8/production/_103163372_jnn6nih3.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "US dollars",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Business Live: Friday 24 August",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The US currency slips on Fed head Jerome Powell comments",
                            "type": "LIV"
                        }
                    ],
                    "semanticGroupName": "News event promotion"
                },
                {
                    "type": "av-stories-now",
                    "title": "Watch/Listen",
                    "strapline": {
                        "name": "Watch/Listen"
                    },
                    "items": [
                        {
                            "assetId": "45507743",
                            "assetUri": "/news/business-45507743",
                            "firstCreated": "2018-09-13T11:01:02+00:00",
                            "headline": "Discount matching undermined profits says John Lewis's Charlie Mayfield",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T11:01:02+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103406499": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/18484/production/_103406499_p06l1qfr.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Charlie Mayfield",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": False
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45507744": {
                                            "externalId": "p06l1p14",
                                            "caption": "Sir Charlie Mayfield on the challenges facing John Lewis",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Discount matching 'undermined profits'",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "John Lewis's Charlie Mayfield tells the BBC matching rivals' deep discounting wiped out profits.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45504585",
                            "assetUri": "/news/uk-politics-45504585",
                            "firstCreated": "2018-09-13T05:37:19+00:00",
                            "headline": "How the bubble burst",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T05:37:19+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103406725": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/CE18/production/_103406725_banker.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Mannequin with sign saying eat the bankers",
                                            "altText": "Mannequin with sign saying eat the bankers",
                                            "copyrightHolder": "AGENCY",
                                            "allowSyndication": False
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45506242": {
                                            "externalId": "p06l0cbj",
                                            "caption": "Financial crisis: What's happened in the last 10 years?",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "UK Politics",
                                "id": "99207",
                                "uri": "/news/politics",
                                "urlIdentifier": "/news/politics"
                            },
                            "summary": "Ten years ago the collapse of an American investment bank changed British life forever.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45496454",
                            "assetUri": "/sport/football/45496454",
                            "firstCreated": "2018-09-13T06:00:17+00:00",
                            "headline": "The 17-year-old dressing football's biggest names",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T06:00:17+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103396045": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/D335/production/_103396045_p06kyx3v.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Sam Morgan AKA SM Creps",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45496455": {
                                            "externalId": "p06kyswj",
                                            "caption": "The 17-year-old dressing football's biggest names",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "section": {
                                "name": "Football",
                                "id": "100830",
                                "uri": "/sport/football",
                                "urlIdentifier": "/news/football"
                            },
                            "site": {
                                "name": "BBC Sport",
                                "code": "sport-v6",
                                "urlIdentifier": "/sport"
                            },
                            "summary": "Sam Morgan is 17 and a personal shopper for some of football's biggest names, including Paul Pogba, and Kevin de Bruyne.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45500664",
                            "assetUri": "/news/business-45500664",
                            "firstCreated": "2018-09-13T07:11:40+00:00",
                            "headline": "Barclay's ex-boss: Banks must take risks",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-13T07:11:40+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103405659": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/175A2/production/_103405659_mediaitem103405814.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Bob Diamond",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45500665": {
                                            "externalId": "p06kz69n",
                                            "caption": "Barclays' former boss Bob Diamond defends the bank",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "In a wide-ranging interview Bob Diamond talks of risk, market rigging and why RBS is worse than Barclays.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45499828",
                            "assetUri": "/news/business-45499828",
                            "firstCreated": "2018-09-12T14:14:02+00:00",
                            "headline": "'I earned more as a student than I do now'",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T14:14:02+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103398234": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/A919/production/_103398234_p06kzfns.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Carol-Ann Costello",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45499829": {
                                            "externalId": "p06kzdpv",
                                            "caption": "'I earned more as a student than I have since'",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Thirty-somethings' salaries are the worst affected by the 2008 financial crisis.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45489064",
                            "assetUri": "/news/business-45489064",
                            "firstCreated": "2018-09-11T23:19:42+00:00",
                            "headline": "Who was to blame for the financial crisis?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-11T23:19:42+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103392956": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/10189/production/_103392956_p06kyh5t.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Animated characters",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45497056": {
                                            "externalId": "p06kygbl",
                                            "caption": "Who was to blame for the financial crisis?",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Explainer",
                                    "categoryName": "Explainer"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "BBC Business editor Simon Jack explores who could have been to blame for the global financial crisis.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45491531",
                            "assetUri": "/news/business-45491531",
                            "firstCreated": "2018-09-12T04:00:23+00:00",
                            "headline": "Carney: Can't rule out another crisis",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T04:00:23+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103386948": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/14BE8/production/_103386948_p06kxhjm.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Mark Carney",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": False
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45491532": {
                                            "externalId": "p06kxhc0",
                                            "caption": "Bank of England governor Mark Carney says history shows no one can rule out another crisis",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The Bank of England governor says history shows that another financial crisis could occur.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45396884",
                            "assetUri": "/news/business-45396884",
                            "firstCreated": "2018-09-10T23:13:17+00:00",
                            "headline": "Using tools made me feel like a superwoman",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-10T23:13:17+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103372526": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/F43F/production/_103372526_p06ktwgx.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Judaline Cassidy",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": False
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45396885": {
                                            "externalId": "p06k4y1j",
                                            "caption": "'Using tools gave me a sense of empowerment, almost like I became a superwoman'",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "One woman in New York is trying to encourage more girls to join the construction industry.",
                            "type": "MAP"
                        }
                    ],
                    "semanticGroupName": "Watch/Listen"
                },
                {
                    "type": "also-in-news",
                    "title": "Also in the news",
                    "strapline": {
                        "name": "Also in the news"
                    },
                    "items": [
                        {
                            "assetId": "45488402",
                            "assetUri": "/news/business-45488402",
                            "byline": {
                                "name": "By Chris Johnston",
                                "persons": [
                                    {
                                        "name": "Chris Johnston",
                                        "function": "Business reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter, BBC News"
                            },
                            "firstCreated": "2018-09-12T11:32:31+00:00",
                            "hasShortForm": True,
                            "headline": "Tesco takes on Aldi and Lidl with Jack's",
                            "includeComments": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T11:32:31+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103393745": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/D5D3/production/_103393745_tesco.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Tesco store",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The UK's biggest supermarket aims to attack the rise of the German chains with its own discount brand.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45482460",
                            "assetUri": "/news/business-45482460",
                            "byline": {
                                "name": "By Chris Johnston",
                                "persons": [
                                    {
                                        "name": "Chris Johnston",
                                        "function": "Business reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter, BBC News"
                            },
                            "firstCreated": "2018-09-11T15:22:09+00:00",
                            "hasShortForm": True,
                            "headline": "How JD Sports became a 5bn company",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-11T15:22:09+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103382202": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/4F04/production/_103382202_jd.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "JD Sports store",
                                            "copyrightHolder": "Newscast",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Record profits for the sports fashion retailer means it is knocking on the door of the FTSE 100.",
                            "type": "STY"
                        }
                    ],
                    "semanticGroupName": "Also in the news"
                },
                {
                    "type": "correspondent-promotion-now",
                    "title": "Correspondent promo",
                    "strapline": {
                        "name": "Our Experts"
                    },
                    "items": [
                        {
                            "links": {
                                "enhancedmobile": "/forge-pal/news/ssi/correspondent-promo/kamalahmed.inc",
                                "mobile": "/forge-pal/news/ssi/correspondent-promo/kamalahmed.inc"
                            },
                            "options": {},
                            "title": "Kamal Ahmed blog importer",
                            "type": "INCLUDE"
                        },
                        {
                            "links": {
                                "enhancedmobile": "/forge-pal/news/ssi/correspondent-promo/simonjack.inc",
                                "mobile": "/forge-pal/news/ssi/correspondent-promo/simonjack.inc"
                            },
                            "options": {},
                            "title": "Simon Jack blog importer",
                            "type": "INCLUDE"
                        },
                        {
                            "links": {
                                "enhancedmobile": "/forge-pal/news/ssi/correspondent-promo/karishmavaswani.inc",
                                "mobile": "/forge-pal/news/ssi/correspondent-promo/karishmavaswani.inc"
                            },
                            "options": {},
                            "title": "Karishma Vaswani importer",
                            "type": "INCLUDE"
                        }
                    ],
                    "semanticGroupName": "Correspondent promo"
                },
                {
                    "type": "featured-site-top-stories",
                    "title": "Other site promotion",
                    "strapline": {
                        "name": "Special reports"
                    },
                    "items": [
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2018-08-13T08:05:26+00:00",
                            "lastUpdated": "2018-08-13T08:05:26+00:00",
                            "links": {
                                "desktop": "http://www.bbc.co.uk/news/business-11428889",
                                "highweb": "http://www.bbc.co.uk/news/business-11428889"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "92611496": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/10F23/production/_92611496_thinkstockphotos-517406978.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "ROBOT HAND AND HUMAN HAND",
                                            "copyrightHolder": "Thinkstock",
                                            "allowSyndication": False
                                        }
                                    },
                                    "index-thumbnail": {
                                        "92611216": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://c.files.bbci.co.uk/EF1B/production/_92611216_thinkstockphotos-467029002.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Robot hand and human hand touching",
                                            "copyrightHolder": "Thinkstock",
                                            "allowSyndication": False
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "Innovation stories from around the world",
                            "title": "Technology of Business",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2018-08-13T08:04:25+00:00",
                            "lastUpdated": "2018-08-13T08:04:25+00:00",
                            "links": {
                                "enhancedmobile": "http://www.bbc.co.uk/news/mobile/business-22449886",
                                "desktop": "http://www.bbc.co.uk/news/business-22449886",
                                "highweb": "http://www.bbc.co.uk/news/business-22449886",
                                "mobile": "http://www.bbc.co.uk/news/mobile/business-22449886"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "102725059": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/1734C/production/_102725059_img_2507full.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Rune Sovndah co-founded Fantastic Services almost a decade ago",
                                            "altText": "Rune Sovndah",
                                            "copyrightHolder": "FS",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "Successful entrepreneurs look back on the key stages of their lives",
                            "title": "The Boss",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2018-01-04T16:55:47+00:00",
                            "lastUpdated": "2018-01-04T16:55:47+00:00",
                            "links": {
                                "desktop": "http://www.bbc.co.uk/news/business-38507481",
                                "highweb": "http://www.bbc.co.uk/news/business-38507481"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "92981295": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/E752/production/_92981295_gettyimages-73171491.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Shipping containers waiting to be loaded at Tilbury Docks in Essex",
                                            "copyrightHolder": "Getty Images"
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "How it is changing the world around us",
                            "title": "Global Trade",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2018-09-12T08:20:11+00:00",
                            "lastUpdated": "2018-09-12T08:20:11+00:00",
                            "links": {
                                "desktop": "https://www.bbc.co.uk/news/business-45489065",
                                "highweb": "https://www.bbc.co.uk/news/business-45489065"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "103391688": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/15A2B/production/_103391688_gettyimages-890698790.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Young man with smartphone against yellow background",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "Global innovations in wireless connectivity",
                            "title": "Connected World",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2018-08-13T08:06:18+00:00",
                            "lastUpdated": "2018-08-13T08:06:18+00:00",
                            "links": {
                                "desktop": "http://www.bbc.co.uk/news/business/business_of_sport/",
                                "highweb": "http://www.bbc.co.uk/news/business/business_of_sport/"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "92448052": {
                                            "height": 945,
                                            "width": 1680,
                                            "href": "http://c.files.bbci.co.uk/61FC/production/_92448052_mediaitem92448051.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Messi of Barcelona in action v Sevilla FC",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "Another perspective on sport",
                            "title": "Business of Sport",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2018-08-21T11:49:17+00:00",
                            "lastUpdated": "2018-08-21T11:49:17+00:00",
                            "links": {
                                "desktop": "http://news.bbc.co.uk/1/hi/in_depth/business/aerospace/",
                                "highweb": "http://news.bbc.co.uk/1/hi/in_depth/business/aerospace/"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "102561337": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/11E64/production/_102561337_1gettyimages-1000179032.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "A visitor tries on a Striker II helmet mounted display at the BAE Systems showroom during the Farnborough Airshow",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    },
                                    "index-thumbnail": {
                                        "102561339": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://c.files.bbci.co.uk/16C84/production/_102561339_1gettyimages-1000179032.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "A visitor tries on a Striker II helmet mounted display at the BAE Systems showroom during the Farnborough Airshow",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "The latest news and analysis in aerospace & defence",
                            "title": "Aerospace & Defence",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2018-01-04T16:57:22+00:00",
                            "lastUpdated": "2018-01-04T16:57:22+00:00",
                            "links": {
                                "desktop": "http://news.bbc.co.uk/1/hi/in_depth/business/2009/carmakers/default.stm",
                                "highweb": "http://news.bbc.co.uk/1/hi/in_depth/business/2009/carmakers/default.stm"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "77958343": {
                                            "height": 432,
                                            "width": 768,
                                            "href": "http://news.bbcimg.co.uk/media/images/77958000/jpg/_77958343_77958342.jpg",
                                            "originCode": "mcs",
                                            "altText": "The new Volkswagen XL Sport is presented during the Volkswagen Group Night prior to the Paris Motor Show",
                                            "copyrightHolder": "European Photopress Agency"
                                        }
                                    },
                                    "index-thumbnail": {
                                        "77958345": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://news.bbcimg.co.uk/media/images/77958000/jpg/_77958345_77958342.jpg",
                                            "originCode": "mcs",
                                            "altText": "The new Volkswagen XL Sport is presented during the Volkswagen Group Night prior to the Paris Motor Show",
                                            "copyrightHolder": "European Photopress Agency"
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "The latest news and analysis from the motoring world",
                            "title": "Global Car Industry",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2015-06-23T15:55:10+00:00",
                            "lastUpdated": "2015-06-23T15:55:10+00:00",
                            "links": {
                                "desktop": "http://www.bbc.co.uk/news/business-15521824",
                                "highweb": "http://www.bbc.co.uk/news/business-15521824"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "70436024": {
                                            "height": 432,
                                            "width": 768,
                                            "href": "http://news.bbcimg.co.uk/media/images/70436000/jpg/_70436024_70436023.jpg",
                                            "originCode": "mcs",
                                            "altText": "Light bulbs",
                                            "copyrightHolder": "Getty Images"
                                        }
                                    },
                                    "index-thumbnail": {
                                        "70436022": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://news.bbcimg.co.uk/media/images/70436000/jpg/_70436022_70436020.jpg",
                                            "originCode": "mcs",
                                            "altText": "Light bulbs",
                                            "copyrightHolder": "Getty Images"
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "The latest news and analysis about the future and cost of power",
                            "title": "Energy",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2015-09-15T13:35:56+00:00",
                            "lastUpdated": "2015-09-15T13:35:56+00:00",
                            "links": {
                                "desktop": "http://www.bbc.co.uk/news/business-33256209",
                                "highweb": "http://www.bbc.co.uk/news/business-33256209"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "85555917": {
                                            "height": 334,
                                            "width": 594,
                                            "href": "http://c.files.bbci.co.uk/11913/production/_85555917_85555916.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Canada v Fiji rugby union 2015",
                                            "copyrightHolder": "Getty Images"
                                        }
                                    },
                                    "index-thumbnail": {
                                        "85555919": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://c.files.bbci.co.uk/16733/production/_85555919_85555916.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Canada v Fiji rugby union 2015",
                                            "copyrightHolder": "Getty Images"
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "The finances, economics and development of rugby union.",
                            "title": "Business of Rugby",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2015-10-15T09:30:22+00:00",
                            "lastUpdated": "2015-10-15T09:30:22+00:00",
                            "links": {
                                "enhancedmobile": "http://www.bbc.co.uk/news/mobile/business-32224205",
                                "desktop": "http://www.bbc.co.uk/news/business-32224205",
                                "highweb": "http://www.bbc.co.uk/news/business-32224205",
                                "mobile": "http://www.bbc.co.uk/news/mobile/business-32224205"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "86040603": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/778C/production/_86040603_img_2541.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Whitney Wolfe founded Bumble after leaving her previous dating app start-up Tinder",
                                            "altText": "Whitney Wolfe standing in front of patterned wallpaper",
                                            "copyrightHolder": "BBC"
                                        }
                                    },
                                    "index-thumbnail": {
                                        "86134352": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://c.files.bbci.co.uk/62FF/production/_86134352_img_2541.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Whitney Wolfe founded Bumble after leaving her previous dating app start-up Tinder",
                                            "altText": "Whitney Wolfe standing in front of patterned wallpaper",
                                            "copyrightHolder": "BBC"
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "The people and firms shaking up business with new technology",
                            "title": "The Digital Disruptors",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2015-10-20T15:54:58+00:00",
                            "lastUpdated": "2015-10-20T15:54:58+00:00",
                            "links": {
                                "enhancedmobile": "http://www.bbc.co.uk/news/mobile/business-29617902",
                                "desktop": "http://www.bbc.co.uk/news/business-29617902",
                                "highweb": "http://www.bbc.co.uk/news/business-29617902",
                                "mobile": "http://www.bbc.co.uk/news/mobile/business-29617902"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "86230454": {
                                            "height": 371,
                                            "width": 660,
                                            "href": "http://c.files.bbci.co.uk/B15B/production/_86230454_bar1.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "A barman in Seoul",
                                            "copyrightHolder": "BBC"
                                        }
                                    },
                                    "index-thumbnail": {
                                        "77958345": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://news.bbcimg.co.uk/media/images/77958000/jpg/_77958345_77958342.jpg",
                                            "originCode": "mcs",
                                            "altText": "The new Volkswagen XL Sport is presented during the Volkswagen Group Night prior to the Paris Motor Show",
                                            "copyrightHolder": "European Photopress Agency"
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "How to achieve business success",
                            "title": "How to succeed in",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2015-09-14T07:24:46+00:00",
                            "lastUpdated": "2015-09-14T07:24:46+00:00",
                            "links": {
                                "desktop": "http://www.bbc.co.uk/news/technology-33978561",
                                "highweb": "http://www.bbc.co.uk/news/technology-33978561"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "85530918": {
                                            "height": 351,
                                            "width": 624,
                                            "href": "http://c.files.bbci.co.uk/13FEF/production/_85530918_85530917.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Intelligent Machines",
                                            "copyrightHolder": "BBC"
                                        }
                                    },
                                    "index-thumbnail": {
                                        "85530920": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://c.files.bbci.co.uk/0B57/production/_85530920_85530917.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Intelligent Machines",
                                            "copyrightHolder": "BBC"
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "The dawn of artificial intelligence",
                            "title": "Intelligent Machines",
                            "type": "LINK"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Text",
                            "firstCreated": "2015-01-27T09:19:49+00:00",
                            "lastUpdated": "2015-01-27T09:19:49+00:00",
                            "links": {
                                "desktop": "http://www.bbc.co.uk/news/business-30384697",
                                "highweb": "http://www.bbc.co.uk/news/business-30384697"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "80542600": {
                                            "height": 450,
                                            "width": 800,
                                            "href": "http://news.bbcimg.co.uk/media/images/80542000/jpg/_80542600_airbus_-_concept_plane_-_side_back_view_right.jpg",
                                            "originCode": "mcs",
                                            "altText": "Airbus concept plane",
                                            "copyrightHolder": "Airbus"
                                        }
                                    },
                                    "index-thumbnail": {
                                        "80542602": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://news.bbcimg.co.uk/media/images/80542000/jpg/_80542602_airbus_-_concept_plane_-_side_back_view_right.jpg",
                                            "originCode": "mcs",
                                            "altText": "Airbus concept plane",
                                            "copyrightHolder": "Airbus"
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "summary": "Features and videos on the future of mobility",
                            "title": "Tomorrow's Transport",
                            "type": "LINK"
                        }
                    ],
                    "semanticGroupName": "Other site promotion"
                },
                {
                    "type": "feature-main",
                    "title": "Features",
                    "strapline": {
                        "name": "Features & Analysis"
                    },
                    "items": [
                        {
                            "assetId": "45485255",
                            "assetUri": "/news/business-45485255",
                            "byline": {
                                "name": "By Jonathan Josephs",
                                "persons": [
                                    {
                                        "name": "Jonathan Josephs",
                                        "function": "Business reporter, BBC News",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter, BBC News"
                            },
                            "firstCreated": "2018-09-12T23:18:28+00:00",
                            "headline": "The UK's growing tech trade ties with Israel",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T23:18:28+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103393144": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/AC6B/production/_103393144_hi048470912.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "A Tevva Motors lorry",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "As the UK looks at developing more trade deals outside the EU after Brexit, its increasing ties with Israel could provide the model.",
                            "type": "STY"
                        },
                        {
                            "assetTypeCode": "PRO",
                            "contentType": "Feature",
                            "firstCreated": "2018-09-11T13:47:33+00:00",
                            "lastUpdated": "2018-09-11T13:47:33+00:00",
                            "links": {
                                "desktop": "https://www.bbc.co.uk/news/resources/idt-sh/The_lost_decade",
                                "highweb": "https://www.bbc.co.uk/news/resources/idt-sh/The_lost_decade"
                            },
                            "media": {
                                "images": {
                                    "index": {
                                        "103386372": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/6AE8/production/_103386372_skyline_getty.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "London skyline",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {},
                            "title": "The financial crisis: The lost decade",
                            "type": "LINK"
                        },
                        {
                            "assetId": "44968514",
                            "assetUri": "/news/business-44968514",
                            "byline": {
                                "name": "By Chris Baraniuk",
                                "persons": [
                                    {
                                        "name": "Chris Baraniuk",
                                        "function": "Technology reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter"
                            },
                            "firstCreated": "2018-09-11T23:34:00+00:00",
                            "headline": "Who's winning the global race to offer superfast 5G?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-11T23:34:00+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103386543": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/8708/production/_103386543_gettyimages-932866170.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "5G was showcased in a variety of ways during this year's Winter Olympics",
                                            "altText": "Ice skaters racing",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Who's winning the race to offer superfast 5G?",
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "China, the US and the UK are all vying to dominate the market for next-generation mobile networks.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45371502",
                            "assetUri": "/news/business-45371502",
                            "byline": {
                                "name": "By Lucy Hooker",
                                "persons": [
                                    {
                                        "name": "Lucy Hooker",
                                        "function": "Business reporter, BBC News",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter, BBC News"
                            },
                            "firstCreated": "2018-09-11T23:23:30+00:00",
                            "headline": "Why 12 is the magic number when it comes to composting",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-11T23:23:30+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103272158": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/14C87/production/_103272158_finishedcompost-1.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Hands holding compost",
                                            "copyrightHolder": "Jenny Grant",
                                            "allowSyndication": False
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "The magic number when it comes to composting",
                            "overtypedSummary": "  ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "More and more packaging is claiming to be \"biodegradable\" or \"compostable\", but what does that really mean?",
                            "type": "STY"
                        },
                        {
                            "assetId": "45481996",
                            "assetUri": "/news/business-45481996",
                            "byline": {
                                "name": "By Sean Coughlan",
                                "persons": [
                                    {
                                        "name": "Sean Coughlan",
                                        "function": "BBC News education and family correspondent",
                                        "twitterName": "seanjcoughlan",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "BBC News education and family correspondent"
                            },
                            "firstCreated": "2018-09-11T23:36:45+00:00",
                            "headline": "Which universities will really impress the boss?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-11T23:36:45+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103381932": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/5D6E/production/_103381932_graduation2.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Graduation",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Which is the best university name in the world to put on a job application?",
                            "type": "STY"
                        },
                        {
                            "assetId": "45470799",
                            "assetUri": "/news/business-45470799",
                            "byline": {
                                "name": "By Padraig Belton",
                                "persons": [
                                    {
                                        "name": "Padraig Belton",
                                        "function": "Business reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Technology of Business reporter"
                            },
                            "firstCreated": "2018-09-10T23:03:37+00:00",
                            "headline": "'A new bladder made from my cells gave me my life back'",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-10T23:03:37+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103367069": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/1774C/production/_103367069_lukemassella.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Luke Massella has to undergo surgery multiple times as a boy",
                                            "altText": "Luke Massella as a boy with his parents",
                                            "copyrightHolder": "Massella Family",
                                            "allowSyndication": False
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "'A bladder made from my cells gave me my life back'",
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Specialised printers are helping to create organic replacement body parts more quickly and safely.",
                            "type": "STY"
                        },
                        {
                            "assetId": "44846317",
                            "assetUri": "/news/business-44846317",
                            "byline": {
                                "name": "By Tamasin Ford",
                                "persons": [
                                    {
                                        "name": "Tamasin Ford",
                                        "function": "BBC News, Buutuo, Liberia",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Accra, Ghana"
                            },
                            "firstCreated": "2018-09-10T23:08:50+00:00",
                            "headline": "The entrepreneur behind Ghana's future inventors",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-10T23:08:50+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "102565898": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/15F00/production/_102565898_15-year-oldprincessmakafui-right2.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Princess Makafui and her friend use the science kit",
                                            "altText": "Princess Makafui and her friend use the science kit",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Charles Ofori Antimpem is the inventor of a science set which is the size and price of a textbook which he now hopes to share with children across Africa.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45395216",
                            "assetUri": "/news/business-45395216",
                            "byline": {
                                "name": "By Anne Cassidy",
                                "persons": [
                                    {
                                        "name": "Anne Cassidy",
                                        "function": "Business reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter"
                            },
                            "firstCreated": "2018-09-09T23:14:14+00:00",
                            "headline": "The dad who feeds his son burgers almost every day",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-09T23:14:14+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103315943": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/8887/production/_103315943_beyondmeat_ethanbrown_beyondburger.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Ethan Brown",
                                            "copyrightHolder": "Beyond Meat",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "A profile of Ethan Brown, the founder and boss of best-selling vegan burger company Beyond Meat.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45419105",
                            "assetUri": "/news/business-45419105",
                            "byline": {
                                "name": "By Suzanne Bearne",
                                "persons": [
                                    {
                                        "name": "Suzanne Bearne",
                                        "function": "Business reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Technology of Business reporter"
                            },
                            "firstCreated": "2018-09-06T23:00:10+00:00",
                            "headline": "Are 'swipe left' dating apps bad for our mental health?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-06T23:00:10+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103318088": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/15811/production/_103318088_gettyimages-871189020.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Too many rejections on dating apps can lower our self-esteem, psychologists say",
                                            "altText": "Sad girl listening to music on her phone",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Dating apps are hugely popular around the world, but some think they're making many of us unhappy.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45421621",
                            "assetUri": "/news/education-45421621",
                            "byline": {
                                "name": "By Sean Coughlan",
                                "persons": [
                                    {
                                        "name": "Sean Coughlan",
                                        "correspondentId": "seancoughlan",
                                        "url": "/news/correspondents/seancoughlan",
                                        "function": "BBC News education and family correspondent",
                                        "thumbnail": "http://c.files.bbci.co.uk/1784/production/_103102060_seanclip.jpg",
                                        "twitterName": "seanjcoughlan",
                                        "originCode": "CPSPRODPB"
                                    }
                                ],
                                "title": "BBC News education and family correspondent"
                            },
                            "firstCreated": "2018-09-07T00:36:25+00:00",
                            "headline": "Is the tuition fees 'illusion' about to unravel?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-07T00:36:25+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "96778978": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/157B3/production/_96778978_seminar976.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "seminar",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    },
                                    "index-thumbnail": {
                                        "103318975": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://c.files.bbci.co.uk/E27D/production/_103318975_seminar976.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "seminar",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                    "categoryName": "Analysis"
                                }
                            },
                            "section": {
                                "name": "Family & Education",
                                "id": "99105",
                                "uri": "/news/education",
                                "urlIdentifier": "/news/education"
                            },
                            "summary": "If student loans are added to the deficit, there will be tough questions about tuition fees' real cost.",
                            "type": "CSP"
                        },
                        {
                            "assetId": "45424537",
                            "assetUri": "/news/world-africa-45424537",
                            "byline": {
                                "name": "By Damilola Ade-Odiachi",
                                "persons": [
                                    {
                                        "name": "Damilola Ade-Odiachi",
                                        "function": "Business reporter, Africa",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "BBC Africa Business reporter"
                            },
                            "firstCreated": "2018-09-07T13:26:37+00:00",
                            "headline": "Nigeria, the phone company and the $2bn tax bill",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-07T13:26:37+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103288906": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/EE3C/production/_103288906_gettyimages-81952755.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "MTN, Africa's largest mobile phone company, has had several financial disputes with Nigeria",
                                            "altText": "Man standing in front of an MTN billboard",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Africa",
                                "id": "99121",
                                "uri": "/news/world/africa",
                                "urlIdentifier": "/news/world/africa"
                            },
                            "summary": "The telecommunications giant was hit with a multi-billion dollar tax bill by Nigerian regulators.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45330898",
                            "assetUri": "/news/business-45330898",
                            "byline": {
                                "name": "By Pedro C Garcia",
                                "persons": [
                                    {
                                        "name": "Pedro C Garcia",
                                        "function": "Business reporter, Lisbon",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter, Lisbon"
                            },
                            "firstCreated": "2018-09-05T23:00:01+00:00",
                            "headline": "Are golden visas losing their sparkle?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-05T23:00:01+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103285828": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/143AA/production/_103285828_index-photo.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "An EU passport and euro notes",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "As Portugal's golden visa scheme faces calls to be axed, do such initiatives that offer residency to foreign nationals do more harm than good?",
                            "type": "STY"
                        },
                        {
                            "assetId": "45273584",
                            "assetUri": "/news/business-45273584",
                            "byline": {
                                "name": "By Mary-Ann Russon",
                                "persons": [
                                    {
                                        "name": "Mary-Ann Russon",
                                        "function": "Technology Reporter, BBC News",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Technology of Business reporter"
                            },
                            "firstCreated": "2018-09-03T23:01:01+00:00",
                            "headline": "The race to make the world's most powerful computer ever",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-03T23:01:01+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103278055": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/D72F/production/_103278055_gettyimages-523052310.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Could quantum computing unlock secrets of our bodies and the universe itself?",
                                            "altText": "Circuit board head graphic",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "The race to make the most powerful computer ever",
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Explainer",
                                    "categoryName": "Explainer"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Quantum computers promise to be blisteringly fast, helping us solve many of the world's problems.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45343236",
                            "assetUri": "/news/business-45343236",
                            "byline": {
                                "name": "By Lora Jones",
                                "persons": [
                                    {
                                        "name": "Lora Jones",
                                        "function": "Business Reporter, BBC News",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business Reporter, BBC News"
                            },
                            "firstCreated": "2018-09-05T23:00:07+00:00",
                            "headline": "How much debt do UK households have?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-05T23:00:07+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103273967": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/12C89/production/_103273967_gettyimages-682285434.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Stack of multicoloured credit cards.",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Explainer",
                                    "categoryName": "Explainer"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "With the collapse of payday loan company Wonga and new rules on credit cards, BBC News explains debt.",
                            "type": "STY"
                        },
                        {
                            "assetId": "44535287",
                            "assetUri": "/news/business-44535287",
                            "byline": {
                                "name": "By Ijeoma Ndukwe ",
                                "persons": [
                                    {
                                        "name": "Ijeoma Ndukwe",
                                        "function": "Ikeja, Nigeria",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Epe, Nigeria"
                            },
                            "firstCreated": "2018-09-03T23:07:07+00:00",
                            "headline": "In Nigeria this baby kit bag is saving mothers' lives",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-03T23:07:07+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "102700845": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/D610/production/_102700845_img_5993.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "The Mother's Delivery Kit contains everything from disinfectants and sterile globes to a scalpel to cut the umbilical cord.",
                                            "altText": "Peju Jaiyeoba showing the contents of the Mother's Delivery Kit",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "In Nigeria every day 118 women die giving birth, but one woman has created a life-saving maternity kit to keep them alive.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45330897",
                            "assetUri": "/news/business-45330897",
                            "byline": {
                                "name": "By Kieron Johnson",
                                "persons": [
                                    {
                                        "name": "Kieron Johnson",
                                        "function": "Business reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Business reporter"
                            },
                            "firstCreated": "2018-09-03T00:04:23+00:00",
                            "headline": "The basketball boss who made billions",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-03T00:04:23+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103231654": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/B22D/production/_103231654_gettyimages-474724673.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Mark Cuban",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Self-made billionaire Mark Cuban, owner of the Dallas Mavericks, says it was always his aim in life to be wealthy.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45020473",
                            "assetUri": "/news/business-45020473",
                            "byline": {
                                "name": "By Daniel Gallas",
                                "persons": [
                                    {
                                        "name": "Daniel Gallas",
                                        "function": "BBC South America Business correspondent",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "BBC South America Business correspondent"
                            },
                            "firstCreated": "2018-09-03T00:10:47+00:00",
                            "headline": "Creating start-ups against the odds in Brazil",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-03T00:10:47+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "102776497": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/1366B/production/_102776497_de217.jpg",
                                            "originCode": "cpsprodpb",
                                            "caption": "Brazil has the world's second-largest population of dogs",
                                            "altText": "Woman with her dog",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Brazil has a slow, bureaucratic tech scene - but some entrepreneurs say if you persist, it pays off.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45292798",
                            "assetUri": "/news/business-45292798",
                            "byline": {
                                "name": "By Ana Nicolaci da Costa ",
                                "persons": [
                                    {
                                        "name": "Ana Nicolaci da Costa",
                                        "function": "BBC Business reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "BBC Business reporter"
                            },
                            "firstCreated": "2018-09-02T00:22:55+00:00",
                            "hasShortForm": True,
                            "headline": "'Crazy Rich Asians' and a growing wealth gap",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-02T00:22:55+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103208712": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/5514/production/_103208712_constancewupic.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Actress Constance Wu at premier of \"Crazy Rich Asians\" movie in California",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                    "categoryName": "Analysis"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The Asia-Pacific has the biggest number of the world's very wealthy and almost two-thirds of its working poor.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45332710",
                            "assetUri": "/news/business-45332710",
                            "byline": {
                                "name": "By Padraig Belton",
                                "persons": [
                                    {
                                        "name": "Padraig Belton",
                                        "function": "Business reporter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Technology of Business reporter"
                            },
                            "firstCreated": "2018-08-30T23:22:38+00:00",
                            "headline": "'My robot makes me feel like I haven't been forgotten'",
                            "language": "en-gb",
                            "lastUpdated": "2018-08-30T23:22:38+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103232449": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/170D7/production/_103232449_zoejohnsoncomp.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Zoe Johnson",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "How internet-connected robots are helping combat the scourge of isolation and loneliness.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45359773",
                            "assetUri": "/news/business-45359773",
                            "byline": {
                                "name": "By Kevin Peachey",
                                "persons": [
                                    {
                                        "name": "Kevin Peachey",
                                        "function": "Personal finance reporter",
                                        "twitterName": "PeacheyK",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Personal finance reporter"
                            },
                            "firstCreated": "2018-08-30T16:49:14+00:00",
                            "headline": "Wonga: Will my debt be written off?",
                            "language": "en-gb",
                            "lastUpdated": "2018-08-30T17:37:47+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103231713": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/7BE1/production/_103231713_paymentbbc.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Payment due on calendar",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedSummary": " ",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Payday lender Wonga has collapsed, but what does this mean for borrowers and compensation claimants?",
                            "type": "STY"
                        }
                    ],
                    "semanticGroupName": "Features"
                },
                {
                    "type": "live-event-now",
                    "title": "The financial crisis 10 years on",
                    "strapline": {
                        "name": "The financial crisis 10 years on"
                    },
                    "maxRelatedLinks": 4,
                    "items": [
                        {
                            "assetId": "45488784",
                            "assetUri": "/news/business-45488784",
                            "byline": {
                                "name": "By Kevin Peachey",
                                "persons": [
                                    {
                                        "name": "Kevin Peachey",
                                        "function": "Personal finance reporter",
                                        "twitterName": "PeacheyK",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Personal finance reporter"
                            },
                            "firstCreated": "2018-09-12T23:01:27+00:00",
                            "headline": "How safe are my savings after the crisis?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T23:01:27+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103396619": {
                                            "height": 408,
                                            "width": 725,
                                            "href": "http://c.files.bbci.co.uk/16615/production/_103396619_savings_getty.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Piggy bank with lock and chain",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Are my savings safe after the crisis?",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "prominence": "none",
                            "relatedGroups": [
                                {
                                    "type": "index",
                                    "items": [
                                        {
                                            "assetId": "45487695",
                                            "assetUri": "/news/business-45487695",
                                            "firstCreated": "2018-09-11T23:02:10+00:00",
                                            "hasShortForm": True,
                                            "headline": "Workers are 800 a year poorer post-crisis",
                                            "includeComments": True,
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:02:10+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                                    "categoryName": "Analysis"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "On average earnings are 3% below where they were a decade ago, the Institute for Fiscal Studies says.",
                                            "type": "CSP"
                                        },
                                        {
                                            "assetId": "45491533",
                                            "assetUri": "/news/business-45491533",
                                            "firstCreated": "2018-09-12T04:00:44+00:00",
                                            "headline": "Carney warns against complacency",
                                            "includeComments": True,
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-12T04:00:44+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "The Governor of the Bank of England tells the BBC there are four risks to financial stability.",
                                            "type": "CSP"
                                        }
                                    ]
                                }
                            ],
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Protection dictates how many animals migrate and so it was with savers during the financial crisis.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45493147",
                            "assetUri": "/news/business-45493147",
                            "byline": {
                                "name": "By Karishma Vaswani",
                                "persons": [
                                    {
                                        "name": "Karishma Vaswani",
                                        "correspondentId": "karishmavaswani",
                                        "url": "/news/correspondents/karishmavaswani",
                                        "function": "Asia business correspondent",
                                        "thumbnail": "http://c.files.bbci.co.uk/14261/production/_84692528_karishma-headshot.jpg",
                                        "twitterName": "BBCKarishma",
                                        "originCode": "CPSPRODPB"
                                    }
                                ],
                                "title": "Asia business correspondent"
                            },
                            "firstCreated": "2018-09-12T23:01:44+00:00",
                            "headline": "How the crisis accelerated the rise of China",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T23:01:44+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103391980": {
                                            "height": 1152,
                                            "width": 2048,
                                            "href": "http://c.files.bbci.co.uk/22D7/production/_103391980_chinatrade.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Chinese port",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "How the crisis accelerated China's rise",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                    "categoryName": "Analysis"
                                }
                            },
                            "prominence": "none",
                            "relatedGroups": [
                                {
                                    "type": "index",
                                    "items": [
                                        {
                                            "assetId": "45491533",
                                            "assetUri": "/news/business-45491533",
                                            "firstCreated": "2018-09-12T04:00:44+00:00",
                                            "headline": "Carney warns against complacency",
                                            "includeComments": True,
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-12T04:00:44+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "The Governor of the Bank of England tells the BBC there are four risks to financial stability.",
                                            "type": "CSP"
                                        },
                                        {
                                            "assetId": "45488784",
                                            "assetUri": "/news/business-45488784",
                                            "firstCreated": "2018-09-12T23:01:27+00:00",
                                            "headline": "How safe are my savings after the crisis?",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-12T23:01:27+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                                    "categoryName": "Feature"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "Protection dictates how many animals migrate and so it was with savers during the financial crisis.",
                                            "type": "STY"
                                        },
                                        {
                                            "assetId": "44952925",
                                            "assetUri": "/news/business-44952925",
                                            "firstCreated": "2018-07-26T14:41:46+00:00",
                                            "headline": "How did the 2008 financial crisis affect you?",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-07-26T14:41:46+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/AskTheAudience",
                                                    "categoryName": "Ask the Audience"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "It was said to be the worst financial crisis since the 1930s. Did the 2008 crash change your life for better or worse?",
                                            "type": "STY"
                                        }
                                    ]
                                }
                            ],
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The global financial crisis had huge consequences for banks around the world, including in Asia, and accelerated China's rise.",
                            "type": "CSP"
                        },
                        {
                            "assetId": "45503767",
                            "assetUri": "/news/business-45503767",
                            "firstCreated": "2018-09-12T23:04:34+00:00",
                            "headline": "'I wanted to set up the antithesis of Lehmans'",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T23:04:34+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103401436": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/F7B2/production/_103401436_anil2.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Anil Stocker",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45503768": {
                                            "externalId": "p06l03s2",
                                            "caption": "'I wanted to set up the antithesis of Lehmans'",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "prominence": "none",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Three former Lehman workers recall the bank going bust 10 years ago and how they've used their experiences to set up their own companies.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45502105",
                            "assetUri": "/news/world-us-canada-45502105",
                            "firstCreated": "2018-09-12T22:23:56+00:00",
                            "headline": "Was the class of 2008 the unluckiest in history?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T22:23:56+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103403444": {
                                            "height": 1080,
                                            "width": 1920,
                                            "href": "http://c.files.bbci.co.uk/AD8E/production/_103403444_posterimage5-2.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Two graduates from the class of 08",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45456017": {
                                            "externalId": "p06l0fxs",
                                            "caption": "Was the class of 2008 the unluckiest in history?",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "prominence": "none",
                            "section": {
                                "name": "US & Canada",
                                "id": "99127",
                                "uri": "/news/world/us_and_canada",
                                "urlIdentifier": "/news/world/us_and_canada"
                            },
                            "summary": "Around 1.5m students graduated from US universities just as the financial crash upended the economy.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45503765",
                            "assetUri": "/news/business-45503765",
                            "firstCreated": "2018-09-12T17:16:19+00:00",
                            "headline": "Ex-Woolies worker 'had to make sacrifices'",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T17:16:19+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103401434": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/A992/production/_103401434_p06kzzgb.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Earl Marchan",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": False
                                        }
                                    }
                                },
                                "videos": {
                                    "primary": {
                                        "45503766": {
                                            "externalId": "p06kzyrh",
                                            "caption": "Former Woolworths worker: 'I'm actually worse off than I was 10 years ago'",
                                            "entityType": "Clip"
                                        }
                                    }
                                }
                            },
                            "mediaType": "Video",
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Feature",
                                    "categoryName": "Feature"
                                }
                            },
                            "prominence": "none",
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Former Woolworths employee Earl Marchan tells the BBC how the financial crisis affected him.",
                            "type": "MAP"
                        },
                        {
                            "assetId": "45487695",
                            "assetUri": "/news/business-45487695",
                            "byline": {
                                "name": "By Kamal Ahmed",
                                "persons": [
                                    {
                                        "name": "Kamal Ahmed",
                                        "correspondentId": "kamalahmed",
                                        "url": "/news/correspondents/kamalahmed",
                                        "function": "Economics editor",
                                        "thumbnail": "http://c.files.bbci.co.uk/03B0/production/_87244900_cba3378a-bc36-4179-bb88-f13993662cac.jpg",
                                        "twitterName": "bbckamal",
                                        "originCode": "CPSPRODPB"
                                    }
                                ],
                                "title": "Economics editor"
                            },
                            "firstCreated": "2018-09-11T23:02:10+00:00",
                            "hasShortForm": True,
                            "headline": "Workers are 800 a year poorer post-crisis",
                            "includeComments": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-11T23:02:10+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103378361": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/4003/production/_103378361_commuters.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "commuters in the rain",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Workers are 800 a year poorer",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                    "categoryName": "Analysis"
                                }
                            },
                            "prominence": "none",
                            "relatedGroups": [
                                {
                                    "type": "index",
                                    "items": [
                                        {
                                            "assetId": "45483636",
                                            "assetUri": "/news/business-45483636",
                                            "firstCreated": "2018-09-11T23:04:32+00:00",
                                            "headline": "How did the crisis affect your finances?",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:04:32+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "A decade on, the way we deal with our personal finances has changed - but not always for good.",
                                            "type": "STY"
                                        },
                                        {
                                            "assetId": "45489064",
                                            "assetUri": "/news/business-45489064",
                                            "firstCreated": "2018-09-11T23:19:42+00:00",
                                            "headline": "Who was to blame for the financial crisis?",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:19:42+00:00",
                                            "mediaType": "Video",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Explainer",
                                                    "categoryName": "Explainer"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "BBC Business editor Simon Jack explores who could have been to blame for the global financial crisis.",
                                            "type": "MAP"
                                        },
                                        {
                                            "assetId": "45488814",
                                            "assetUri": "/news/uk-45488814",
                                            "firstCreated": "2018-09-11T23:26:45+00:00",
                                            "headline": "'I earn the same as 10 years ago'",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:26:45+00:00",
                                            "mediaType": "Video",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "UK",
                                                "id": "99116",
                                                "uri": "/news/uk",
                                                "urlIdentifier": "/news/uk"
                                            },
                                            "summary": "A decade on from the 2008 global financial crisis, families are still feeling the effects.",
                                            "type": "MAP"
                                        }
                                    ]
                                }
                            ],
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "On average earnings are 3% below where they were a decade ago, the Institute for Fiscal Studies says.",
                            "type": "CSP"
                        },
                        {
                            "assetId": "45491533",
                            "assetUri": "/news/business-45491533",
                            "byline": {
                                "name": "By Kamal Ahmed",
                                "persons": [
                                    {
                                        "name": "Kamal Ahmed",
                                        "correspondentId": "kamalahmed",
                                        "url": "/news/correspondents/kamalahmed",
                                        "function": "Economics editor",
                                        "thumbnail": "http://c.files.bbci.co.uk/03B0/production/_87244900_cba3378a-bc36-4179-bb88-f13993662cac.jpg",
                                        "twitterName": "bbckamal",
                                        "originCode": "CPSPRODPB"
                                    }
                                ],
                                "title": "Economics editor"
                            },
                            "firstCreated": "2018-09-12T04:00:44+00:00",
                            "headline": "Carney warns against complacency",
                            "includeComments": True,
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T04:00:44+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103386951": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/3E60/production/_103386951_carney.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Mark Carney",
                                            "copyrightHolder": "BBC",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "prominence": "none",
                            "relatedGroups": [
                                {
                                    "type": "index",
                                    "items": [
                                        {
                                            "assetId": "45487695",
                                            "assetUri": "/news/business-45487695",
                                            "firstCreated": "2018-09-11T23:02:10+00:00",
                                            "hasShortForm": True,
                                            "headline": "Workers are 800 a year poorer post-crisis",
                                            "includeComments": True,
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:02:10+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                                    "categoryName": "Analysis"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "On average earnings are 3% below where they were a decade ago, the Institute for Fiscal Studies says.",
                                            "type": "CSP"
                                        },
                                        {
                                            "assetId": "45482461",
                                            "assetUri": "/news/business-45482461",
                                            "firstCreated": "2018-09-11T11:23:09+00:00",
                                            "hasShortForm": True,
                                            "headline": "Carney to stay at Bank of England until 2020",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T13:48:36+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "Mark Carney extends term as Bank of England governor until the end of January 2020, chancellor says.",
                                            "type": "STY"
                                        }
                                    ]
                                }
                            ],
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "The Governor of the Bank of England tells the BBC there are four risks to financial stability.",
                            "type": "CSP"
                        },
                        {
                            "assetId": "45488397",
                            "assetUri": "/news/business-45488397",
                            "byline": {
                                "name": "By Dominic O'Connell",
                                "persons": [
                                    {
                                        "name": "Dominic O'Connell",
                                        "function": "Today business presenter",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Today Programme business presenter"
                            },
                            "firstCreated": "2018-09-12T06:39:43+00:00",
                            "hasShortForm": True,
                            "headline": "Lehman gamble paid out for brave investors",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-12T06:39:43+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103382691": {
                                            "height": 576,
                                            "width": 1024,
                                            "href": "http://c.files.bbci.co.uk/4CAC/production/_103382691_lb.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Lehman UK staff",
                                            "copyrightHolder": "Reuters",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "Lehman bet paid off for investors",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "prominence": "none",
                            "relatedGroups": [
                                {
                                    "type": "index",
                                    "items": [
                                        {
                                            "assetId": "45491533",
                                            "assetUri": "/news/business-45491533",
                                            "firstCreated": "2018-09-12T04:00:44+00:00",
                                            "headline": "Carney warns against complacency",
                                            "includeComments": True,
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-12T04:00:44+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "The Governor of the Bank of England tells the BBC there are four risks to financial stability.",
                                            "type": "CSP"
                                        },
                                        {
                                            "assetId": "45487695",
                                            "assetUri": "/news/business-45487695",
                                            "firstCreated": "2018-09-11T23:02:10+00:00",
                                            "hasShortForm": True,
                                            "headline": "Workers are 800 a year poorer post-crisis",
                                            "includeComments": True,
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:02:10+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                                    "categoryName": "Analysis"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "On average earnings are 3% below where they were a decade ago, the Institute for Fiscal Studies says.",
                                            "type": "CSP"
                                        }
                                    ]
                                }
                            ],
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "Some investors who took a punt on the wreck of Lehman Brothers' UK operations made handsome returns.",
                            "type": "STY"
                        },
                        {
                            "assetId": "45483636",
                            "assetUri": "/news/business-45483636",
                            "byline": {
                                "name": "By Simon Read & Daniele Palumbo ",
                                "persons": [
                                    {
                                        "name": "Simon Read",
                                        "function": "Personal finance reporter",
                                        "originCode": "MCS"
                                    },
                                    {
                                        "name": "Daniele Palumbo",
                                        "function": "Data journalist",
                                        "twitterName": "danict89",
                                        "originCode": "MCS"
                                    }
                                ],
                                "title": "Personal finance reporter"
                            },
                            "firstCreated": "2018-09-11T23:04:32+00:00",
                            "headline": "How did the crisis affect your finances?",
                            "language": "en-gb",
                            "lastUpdated": "2018-09-11T23:04:32+00:00",
                            "media": {
                                "images": {
                                    "index": {
                                        "103391986": {
                                            "height": 549,
                                            "width": 976,
                                            "href": "http://c.files.bbci.co.uk/10D37/production/_103391986_financesgettyimages-612736550.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Woman holds head in shock",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    },
                                    "index-thumbnail": {
                                        "103391989": {
                                            "height": 180,
                                            "width": 320,
                                            "href": "http://c.files.bbci.co.uk/18267/production/_103391989_financesgettyimages-612736550.jpg",
                                            "originCode": "cpsprodpb",
                                            "altText": "Woman holds head in shock",
                                            "copyrightHolder": "Getty Images",
                                            "allowSyndication": True
                                        }
                                    }
                                }
                            },
                            "options": {
                                "isFactCheck": False,
                                "isBreakingNews": False
                            },
                            "overtypedHeadline": "How did it affect your finances?",
                            "passport": {
                                "category": {
                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                    "categoryName": "News"
                                }
                            },
                            "prominence": "none",
                            "relatedGroups": [
                                {
                                    "type": "index",
                                    "items": [
                                        {
                                            "assetId": "45487695",
                                            "assetUri": "/news/business-45487695",
                                            "firstCreated": "2018-09-11T23:02:10+00:00",
                                            "hasShortForm": True,
                                            "headline": "Workers are 800 a year poorer post-crisis",
                                            "includeComments": True,
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:02:10+00:00",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Analysis",
                                                    "categoryName": "Analysis"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "On average earnings are 3% below where they were a decade ago, the Institute for Fiscal Studies says.",
                                            "type": "CSP"
                                        },
                                        {
                                            "assetId": "45489064",
                                            "assetUri": "/news/business-45489064",
                                            "firstCreated": "2018-09-11T23:19:42+00:00",
                                            "headline": "Who was to blame for the financial crisis?",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:19:42+00:00",
                                            "mediaType": "Video",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/Explainer",
                                                    "categoryName": "Explainer"
                                                }
                                            },
                                            "section": {
                                                "name": "Business",
                                                "id": "99104",
                                                "uri": "/news/business",
                                                "urlIdentifier": "/news/business"
                                            },
                                            "summary": "BBC Business editor Simon Jack explores who could have been to blame for the global financial crisis.",
                                            "type": "MAP"
                                        },
                                        {
                                            "assetId": "45488814",
                                            "assetUri": "/news/uk-45488814",
                                            "firstCreated": "2018-09-11T23:26:45+00:00",
                                            "headline": "'I earn the same as 10 years ago'",
                                            "language": "en-gb",
                                            "lastUpdated": "2018-09-11T23:26:45+00:00",
                                            "mediaType": "Video",
                                            "passport": {
                                                "category": {
                                                    "categoryId": "http://www.bbc.co.uk/ontologies/applicationlogic-news/News",
                                                    "categoryName": "News"
                                                }
                                            },
                                            "section": {
                                                "name": "UK",
                                                "id": "99116",
                                                "uri": "/news/uk",
                                                "urlIdentifier": "/news/uk"
                                            },
                                            "summary": "A decade on from the 2008 global financial crisis, families are still feeling the effects.",
                                            "type": "MAP"
                                        }
                                    ]
                                }
                            ],
                            "section": {
                                "name": "Business",
                                "id": "99104",
                                "uri": "/news/business",
                                "urlIdentifier": "/news/business"
                            },
                            "summary": "A decade on, the way we deal with our personal finances has changed - but not always for good.",
                            "type": "STY"
                        }
                    ],
                    "semanticGroupName": "Cluster 1"
                }
            ],
            "options": {
                "allowAdvertising": True
            },
            "language": "en-gb",
            "id": "http://www.bbc.co.uk/asset/b5c53243-711d-e059-e040-850a02846523/mobile/domestic",
            "assetUri": "/news/business",
            "platform": "mobile",
            "audience": "domestic",
            "assetId": "10059368",
            "section": {
                "name": "Business",
                "id": "99104",
                "uri": "/news/business",
                "urlIdentifier": "/news/business"
            },
            "site": {
                "name": "BBC News",
                "code": "news-v6",
                "urlIdentifier": "/news",
                "frontPageUri": "/news/front_page"
            },
            "workerCallingCard": "app1163.back.live.telhc.local-47",
            "iStatsCounterName": "news.business.page"
        }
    ]
}

TEST_TREVOR_JSON = {
  "id" : "/cps/news/business",
  "type" : "bbc.mobile.news.collection",
  "format" : "bbc.mobile.news.cps.idx",
  "language" : "en-gb",
  "lastUpdated" : 1536824521000,
  "site" : "/news",
  "name" : "Business",
  "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
  "iStatsCounter" : "news.business.page",
  "iStatsLabels" : {
    "page_type" : "index",
    "cps_asset_id" : "10059368"
  },
  "allowAdvertising" : True,
  "relations" : [ {
    "eTag" : "059b8b36de81b69fc7fe909456bef247",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.top-story",
    "content" : {
      "id" : "/cps/news/business-45506322",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536823677000,
      "site" : "/news",
      "name" : "John Lewis profits slump 99% in 'challenging times'",
      "summary" : "The retailer's half-year profits slump to 1.2m amid discounting \"extravaganza days\" by rivals.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "John Lewis half-year profits slump 99%",
      "iStatsCounter" : "news.business.story.45506322.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/8D36/production/_103405163_9yniarol.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 768,
          "height" : 432,
          "href" : "http://c.files.bbci.co.uk/8D36/production/_103405163_9yniarol.jpg",
          "altText" : "John Lewis store",
          "copyrightHolder" : "Reuters",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/8D36/production/_103405163_9yniarol.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45506322",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45506322",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45506322"
      }
    }
  }, {
    "eTag" : "1b3b23b7cb455659c8f05ab64ce8b54a",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.second-story",
    "content" : {
      "id" : "/cps/news/business-45504521",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536811688000,
      "site" : "/news",
      "name" : "Gordon Brown in dire warning about the next financial crisis",
      "summary" : "The former prime minister tells the BBC that the world is sleepwalking into another financial crisis.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Gordon Brown warns about next crisis",
      "iStatsCounter" : "news.business.correspondent_story.45504521.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/15770/production/_103402978_brown.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/15770/production/_103402978_brown.jpg",
          "altText" : "BBC",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/15770/production/_103402978_brown.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06l03tr",
          "type" : "bbc.mobile.news.video",
          "duration" : 71000,
          "caption" : "Gordon Brown says we are sleepwalking into another financial crisis",
          "externalId" : "p06l03tx",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06l0bv0.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45504521",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45504521",
      "iStatsLabels" : {
        "page_type" : "correspondent-story",
        "cps_asset_id" : "45504521"
      }
    }
  }, {
    "eTag" : "eb0fd6fc988161a07d3a8a2d393f861f",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.third-story",
    "content" : {
      "id" : "/cps/news/live/business-45449121",
      "type" : "bbc.mobile.news.live_event_ext",
      "format" : "bbc.mobile.news.format.liveevent",
      "language" : "en-gb",
      "lastUpdated" : 1536319541000,
      "name" : "Business Live: Thursday 13 September",
      "summary" : "All the day's business news and views from the UK and beyond, as it happens.",
      "shortName" : "Business Live: Thursday 13 September",
      "iStatsCounter" : "news.business.live_coverage.45449121.page",
      "commentaryId" : "/commentary/45449127",
      "isLive" : False,
      "liveStatus" : "AUTO",
      "scheduledStartTime" : "2018-09-13T00:00:00+00:00",
      "scheduledEndTime" : "2018-09-13T20:45:00+00:00",
      "isAllDayEvent" : False,
      "keyPoints" : [ "Get in touch: bizlivepage@bbc.co.uk" ],
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/10A6D/production/_102650286_gherkin.ground.gc.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1061,
          "height" : 597,
          "href" : "http://c.files.bbci.co.uk/10A6D/production/_102650286_gherkin.ground.gc.jpg",
          "altText" : "City of London",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/10A6D/production/_102650286_gherkin.ground.gc.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/live/business-45449121",
      "shareUrl" : "http://www.bbc.co.uk/news/live/business-45449121",
      "site" : "/news",
      "live" : False,
      "iStatsLabels" : {
        "page_type" : "live-coverage",
        "cps_asset_id" : "45449121"
      }
    }
  }, {
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "a5fd5e0e31d964eb6921a38757382ee3",
      "type" : "bbc.mobile.news.group.link",
      "shareUrl" : "http://www.bbc.co.uk/news/business/market-data",
      "name" : "Live market data",
      "summary" : "Live market data",
      "lastUpdated" : 1525776290000,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/AC77/production/_101215144_marketimage_getty.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 2048,
          "height" : 1152,
          "href" : "http://c.files.bbci.co.uk/AC77/production/_101215144_marketimage_getty.jpg",
          "altText" : "Market data image",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/AC77/production/_101215144_marketimage_getty.jpg",
          "relations" : [ ]
        }
      } ],
      "allowAdvertising" : True,
      "iStatsLabels" : { }
    }
  }, {
    "eTag" : "94b848a4d2104fefb50cab4233738f78",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/business-45506492",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536822363000,
      "site" : "/news",
      "name" : "Morrisons sales soar as revival continues",
      "summary" : "The UK's fourth-biggest supermarket reports its best quarterly sales increase for almost a decade.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Morrisons sales soar as revival continues",
      "iStatsCounter" : "news.business.story.45506492.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/DFA2/production/_103405275_morrisons.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 2048,
          "height" : 1152,
          "href" : "http://c.files.bbci.co.uk/DFA2/production/_103405275_morrisons.jpg",
          "altText" : "Morrisons",
          "copyrightHolder" : "Reuters",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/DFA2/production/_103405275_morrisons.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45506492",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45506492",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45506492"
      }
    }
  }, {
    "eTag" : "588cc18691949ba3b2a75700a7e533f2",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/business-45498235",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536819146000,
      "site" : "/news",
      "name" : "Bob Diamond defends risk-taking banks",
      "summary" : "Former Barclays boss Bob Diamond says risk-averse banks can't create jobs and economic growth.",
      "passport" : {
        "category" : {
          "categoryName" : "Analysis"
        }
      },
      "shortName" : "Bob Diamond defends risk-taking banks",
      "iStatsCounter" : "news.business.correspondent_story.45498235.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/7165/production/_103392092_bobdiamond.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/7165/production/_103392092_bobdiamond.jpg",
          "altText" : "Bob Diamond",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/7165/production/_103392092_bobdiamond.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45498235",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45498235",
      "iStatsLabels" : {
        "page_type" : "correspondent-story",
        "cps_asset_id" : "45498235"
      }
    }
  }, {
    "eTag" : "7f4ccd2573e92e3432a22001980c68b0",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/business-45488784",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536793287000,
      "site" : "/news",
      "name" : "How safe are my savings after the financial crisis?",
      "summary" : "Protection dictates how many animals migrate and so it was with savers during the financial crisis.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "How safe are my savings after the crisis?",
      "iStatsCounter" : "news.business.story.45488784.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/16615/production/_103396619_savings_getty.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 725,
          "height" : 408,
          "href" : "http://c.files.bbci.co.uk/16615/production/_103396619_savings_getty.jpg",
          "altText" : "Piggy bank with lock and chain",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/16615/production/_103396619_savings_getty.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45488784",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45488784",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45488784"
      }
    }
  }, {
    "eTag" : "b7e1681414da76974a8ea024305a6c80",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/business-45493147",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536793304000,
      "site" : "/news",
      "name" : "Why Asia turned to China during the global financial crisis",
      "summary" : "The global financial crisis had huge consequences for banks around the world, including in Asia, and accelerated China's rise.",
      "passport" : {
        "category" : {
          "categoryName" : "Analysis"
        }
      },
      "shortName" : "How the crisis accelerated the rise of China",
      "iStatsCounter" : "news.business.correspondent_story.45493147.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/22D7/production/_103391980_chinatrade.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 2048,
          "height" : 1152,
          "href" : "http://c.files.bbci.co.uk/22D7/production/_103391980_chinatrade.jpg",
          "altText" : "Chinese port",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/22D7/production/_103391980_chinatrade.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45493147",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45493147",
      "iStatsLabels" : {
        "page_type" : "correspondent-story",
        "cps_asset_id" : "45493147"
      }
    }
  }, {
    "eTag" : "c81e82c4c04e46ff19f98a3e7e2c551b",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/world-asia-china-45505522",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536816886000,
      "site" : "/news",
      "name" : "Restaurant loses $190m in value after dead rat found in soup",
      "summary" : "A pregnant woman in China found the boiled rat in her dish after she had taken a few bites.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Dead rat in soup costs restaurant $190m",
      "iStatsCounter" : "news.world.asia.china.story.45505522.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/107D4/production/_103404576_raterswr.png",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/107D4/production/_103404576_raterswr.png",
          "altText" : "Rat found in hotpot",
          "caption" : "The dead rat was fished out a pot of boiling broth",
          "copyrightHolder" : "Weibo",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/107D4/production/_103404576_raterswr.png",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/world/asia/china",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536818532000,
          "site" : "/news",
          "name" : "China",
          "summary" : "Get the latest Asian news from BBC News in Asia: breaking news, features, analysis and special reports plus audio and video from across the Asian continent.",
          "iStatsCounter" : "news.world.asia.china.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "15296724"
          },
          "allowAdvertising" : True,
          "topic" : "/ldp/6892384e-1966-4c03-9ce3-f694a8f9f69e",
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/world/asia/china",
          "shareUrl" : "http://www.bbc.co.uk/news/world/asia/china",
          "eTag" : "f2212e41d31114e9ee8e078ff77f90a6"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/world-asia-china-45505522",
      "shareUrl" : "http://www.bbc.co.uk/news/world-asia-china-45505522",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45505522"
      }
    }
  }, {
    "eTag" : "afe3194e34729ae6aced14828c42250e",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/technology-45502465",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536783846000,
      "site" : "/news",
      "name" : "Apple iPhone XS unveiled alongside fall-detecting Watch",
      "summary" : "Three new iPhone models are revealed plus a fall-detecting smartwatch.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Apple unveils iPhone XS and new Watch",
      "iStatsCounter" : "news.technology.story.45502465.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/A73A/production/_103401824_33ca92d3-9cc3-4459-ba64-5e68883f21fd.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/A73A/production/_103401824_33ca92d3-9cc3-4459-ba64-5e68883f21fd.jpg",
          "altText" : "Two iPhone XS phones",
          "copyrightHolder" : "Apple",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/A73A/production/_103401824_33ca92d3-9cc3-4459-ba64-5e68883f21fd.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06l0gkj",
          "type" : "bbc.mobile.news.video",
          "duration" : 139000,
          "caption" : "WATCH: Hands on with new iPhone XS and XS Max",
          "externalId" : "p06l0ktn",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06l0lfs.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/technology",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536794943000,
          "site" : "/news",
          "name" : "Technology",
          "summary" : "Get the latest BBC Technology News: breaking news and analysis on computing, the web, blogs, games, gadgets, social media, broadband and more.",
          "iStatsCounter" : "news.technology.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059376"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/technology",
          "shareUrl" : "http://www.bbc.co.uk/news/technology",
          "eTag" : "a2f190d4fa61d4610cbb7658ec21990c"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/technology-45502465",
      "shareUrl" : "http://www.bbc.co.uk/news/technology-45502465",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45502465"
      }
    }
  }, {
    "eTag" : "75cf2aa4498945741c476bf915ee4feb",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/business-45501884",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536766560000,
      "site" : "/news",
      "name" : "Oil pushes past $80 as Iran fears mount",
      "summary" : "The rising price of Brent oil reflects concerns about the impact of US sanctions against Iran.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Oil pushes past $80 as Iran fears mount",
      "iStatsCounter" : "news.business.story.45501884.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/9DCF/production/_103399304_hi047580124.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 2048,
          "height" : 1152,
          "href" : "http://c.files.bbci.co.uk/9DCF/production/_103399304_hi047580124.jpg",
          "altText" : "Oil well in South Texas",
          "copyrightHolder" : "Reuters",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/9DCF/production/_103399304_hi047580124.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45501884",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45501884",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45501884"
      }
    }
  }, {
    "eTag" : "f319c5bcb1136e4532dbf4910635c813",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/business-45500384",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536763341000,
      "site" : "/news",
      "name" : "RBS bailout 'unlikely to be recouped'",
      "summary" : "Chairman Sir Howard Davies says the bank was rescued to save the financial system, not as an investment.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "RBS bailout 'unlikely to be recouped'",
      "iStatsCounter" : "news.business.story.45500384.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/14423/production/_103397928_rbsmoneygettyimages-864993966-1.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/14423/production/_103397928_rbsmoneygettyimages-864993966-1.jpg",
          "altText" : "RBS cash machines",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/14423/production/_103397928_rbsmoneygettyimages-864993966-1.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45500384",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45500384",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45500384"
      }
    }
  }, {
    "eTag" : "e3304d6c875bd3d7cc7368b31c27d01f",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/business-45502084",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536768238000,
      "site" : "/news",
      "name" : "Hammond: 'Shock' of financial crisis still with us",
      "summary" : "The UK's chancellor admits peoples' incomes are suffering, but sees \"light at the end of the tunnel\".",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Hammond: Financial crisis 'shock' continues",
      "iStatsCounter" : "news.business.story.45502084.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/164B8/production/_103402319_mediaitem103399867.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/164B8/production/_103402319_mediaitem103399867.jpg",
          "altText" : "Philip Hammond",
          "copyrightHolder" : "Reuters",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/164B8/production/_103402319_mediaitem103399867.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06l08nk",
          "type" : "bbc.mobile.news.video",
          "duration" : 833000,
          "caption" : "Hammond: Many countries suffered worse than the UK during the crisis",
          "externalId" : "p06l08nn",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06l08y0.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45502084",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45502084",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45502084"
      }
    }
  }, {
    "eTag" : "36bd5d810188ef9c8b2e671542365e80",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/business-45505232",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536815726000,
      "site" : "/news",
      "name" : "World's largest dairy exporter posts first annual loss",
      "summary" : "The New Zealand co-operative said it let down farmers with overly optimistic financial forecasts.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Dairy giant Fonterra posts first loss",
      "iStatsCounter" : "news.business.story.45505232.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/E3E4/production/_103404385_gettyimages-1032378322-1.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/E3E4/production/_103404385_gettyimages-1032378322-1.jpg",
          "altText" : "Cow eating grass on a dairy farm",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/E3E4/production/_103404385_gettyimages-1032378322-1.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45505232",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45505232",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45505232"
      }
    }
  }, {
    "eTag" : "d37015e42528c53041aa6b2a922e3385",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.other-top-stories",
    "content" : {
      "id" : "/cps/news/world-asia-india-45492856",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536798404000,
      "site" : "/news",
      "name" : "Viewpoint: What can stop India's rupee plunge?",
      "summary" : "The currency's sharp fall has raised concerns that fuel prices in the country will climb.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Viewpoint: What can stop India's rupee plunge?",
      "iStatsCounter" : "news.world.asia.india.story.45492856.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/733A/production/_103389492_gettyimages-625464948.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/733A/production/_103389492_gettyimages-625464948.jpg",
          "altText" : "A man counts rupee notes",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/733A/production/_103389492_gettyimages-625464948.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/world/asia/india",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536798460000,
          "site" : "/news",
          "name" : "India",
          "summary" : "Get the latest Asian news from BBC News in Asia: breaking news, features, analysis and special reports plus audio and video from across the Asian continent.",
          "iStatsCounter" : "news.world.asia.india.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "15592104"
          },
          "allowAdvertising" : True,
          "topic" : "/ldp/5a08f030-710f-4168-acee-67294a90fc75",
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/world/asia/india",
          "shareUrl" : "http://www.bbc.co.uk/news/world/asia/india",
          "eTag" : "33da66154de8fcf3f7c7ede3cac7f6e1"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/world-asia-india-45492856",
      "shareUrl" : "http://www.bbc.co.uk/news/world-asia-india-45492856",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45492856"
      }
    }
  }, {
    "eTag" : "474c21d5ab806a1ae8bdae02d0782861",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.av-stories-best",
    "content" : {
      "id" : "/cps/news/business-45500664",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.video",
      "language" : "en-gb",
      "lastUpdated" : 1536822700000,
      "site" : "/news",
      "name" : "Barclay's Bob Diamond says banks 'must take risks'",
      "summary" : "In a wide-ranging interview Bob Diamond talks of risk, market rigging and why RBS is worse than Barclays.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Barclay's ex-boss: Banks must take risks",
      "iStatsCounter" : "news.business.media_asset.45500664.page",
      "allowAdvertising" : True,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/F19A/production/_103405816_mediaitem103405814.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/F19A/production/_103405816_mediaitem103405814.jpg",
          "altText" : "Bob Diamond",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/F19A/production/_103405816_mediaitem103405814.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.body",
        "content" : {
          "id" : "/cpsprodpb/CA8A/production/_103405815_mediaitem103405814.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "positionHint" : "full-width",
          "href" : "http://c.files.bbci.co.uk/CA8A/production/_103405815_mediaitem103405814.jpg",
          "altText" : "Bob Diamond",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/CA8A/production/_103405815_mediaitem103405814.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06kz69n",
          "type" : "bbc.mobile.news.video",
          "duration" : 295000,
          "caption" : "Barclays' former boss Bob Diamond defends its pre-crisis \"strong culture\"",
          "externalId" : "p06kz69x",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06l12cp.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45500664",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45500664",
      "iStatsLabels" : {
        "page_type" : "media-asset",
        "cps_asset_id" : "45500664"
      }
    }
  }, {
    "eTag" : "49326bc3f63494976bb1b56b8133d9ef",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.av-stories-best",
    "content" : {
      "id" : "/cps/news/uk-politics-45504585",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.video",
      "language" : "en-gb",
      "lastUpdated" : 1536817039000,
      "site" : "/news",
      "name" : "Financial crisis: What's happened in the last 10 years?",
      "summary" : "Lasting consequences and possible future implications: BBC experts take a look at the financial crash 10 years on.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "'You'll be lucky to ever retire'",
      "iStatsCounter" : "news.politics.media_asset.45504585.page",
      "allowAdvertising" : True,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/BB44/production/_103404974_p06l0tsr.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1024,
          "height" : 576,
          "href" : "http://c.files.bbci.co.uk/BB44/production/_103404974_p06l0tsr.jpg",
          "altText" : "Protesters gather outside of the New York Stock Exchange October 24, 2008 in New York City.",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/BB44/production/_103404974_p06l0tsr.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06l0cbj",
          "type" : "bbc.mobile.news.video",
          "duration" : 242000,
          "caption" : "Financial crisis: What's happened in the last 10 years?",
          "externalId" : "p06l0cbl",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06l0tsr.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/politics",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536820572000,
          "site" : "/news",
          "name" : "UK Politics",
          "summary" : "Get the latest BBC Politics news: breaking news, comment and analysis plus political guides and in-depth special reports on UK and EU politics.",
          "iStatsCounter" : "news.politics.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10067595"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/politics",
          "shareUrl" : "http://www.bbc.co.uk/news/politics",
          "eTag" : "a8d47986f7421800f5a80c400dd27cc4"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/uk-politics-45504585",
      "shareUrl" : "http://www.bbc.co.uk/news/uk-politics-45504585",
      "iStatsLabels" : {
        "page_type" : "media-asset",
        "cps_asset_id" : "45504585"
      }
    }
  }, {
    "eTag" : "62a40a8ebac3ab88833d69a1c24a8370",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.av-stories-best",
    "content" : {
      "id" : "/cps/news/business-45503767",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.video",
      "language" : "en-gb",
      "lastUpdated" : 1536793474000,
      "site" : "/news",
      "name" : "I wanted to set up the antithesis of Lehmans",
      "summary" : "Three former Lehman workers recall the bank going bust 10 years ago and how they've used their experiences to set up their own companies.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "'I wanted to set up the antithesis of Lehmans'",
      "iStatsCounter" : "news.business.media_asset.45503767.page",
      "allowAdvertising" : True,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/F7B2/production/_103401436_anil2.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1024,
          "height" : 576,
          "href" : "http://c.files.bbci.co.uk/F7B2/production/_103401436_anil2.jpg",
          "altText" : "Anil Stocker",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/F7B2/production/_103401436_anil2.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06l03s2",
          "type" : "bbc.mobile.news.video",
          "duration" : 116000,
          "caption" : "'I wanted to set up the antithesis of Lehmans'",
          "externalId" : "p06l03s6",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06l0knw.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45503767",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45503767",
      "iStatsLabels" : {
        "page_type" : "media-asset",
        "cps_asset_id" : "45503767"
      }
    }
  }, {
    "eTag" : "cae5c21f04692694f0e35329e670cc8a",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.av-stories-best",
    "content" : {
      "id" : "/cps/news/business-45503765",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.video",
      "language" : "en-gb",
      "lastUpdated" : 1536772579000,
      "site" : "/news",
      "name" : "Former Woolworths worker 'had to make sacrifices'",
      "summary" : "Former Woolworths employee Earl Marchan tells the BBC how the financial crisis affected him.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "Ex-Woolies worker 'had to make sacrifices'",
      "iStatsCounter" : "news.business.media_asset.45503765.page",
      "allowAdvertising" : True,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/A992/production/_103401434_p06kzzgb.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1024,
          "height" : 576,
          "href" : "http://c.files.bbci.co.uk/A992/production/_103401434_p06kzzgb.jpg",
          "altText" : "Earl Marchan",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/A992/production/_103401434_p06kzzgb.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06kzyrh",
          "type" : "bbc.mobile.news.video",
          "duration" : 59000,
          "caption" : "Former Woolworths worker: 'I'm actually worse off than I was 10 years ago'",
          "externalId" : "p06kzyrk",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06kzzgb.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45503765",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45503765",
      "iStatsLabels" : {
        "page_type" : "media-asset",
        "cps_asset_id" : "45503765"
      }
    }
  }, {
    "eTag" : "872ab31523f86682ab7a6c86475e9c6c",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.av-stories-best",
    "content" : {
      "id" : "/cps/news/business-45499828",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.video",
      "language" : "en-gb",
      "lastUpdated" : 1536761642000,
      "site" : "/news",
      "name" : "'I earned more as a student than I have since'",
      "summary" : "Thirty-somethings' salaries are the worst affected by the 2008 financial crisis.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "'I earned more as a student than I do now'",
      "iStatsCounter" : "news.business.media_asset.45499828.page",
      "allowAdvertising" : True,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/A919/production/_103398234_p06kzfns.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1024,
          "height" : 576,
          "href" : "http://c.files.bbci.co.uk/A919/production/_103398234_p06kzfns.jpg",
          "altText" : "Carol-Ann Costello",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/A919/production/_103398234_p06kzfns.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06kzdpv",
          "type" : "bbc.mobile.news.video",
          "duration" : 113000,
          "caption" : "'I earned more as a student than I have since'",
          "externalId" : "p06kzdpx",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06kzhnv.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45499828",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45499828",
      "iStatsLabels" : {
        "page_type" : "media-asset",
        "cps_asset_id" : "45499828"
      }
    }
  }, {
    "eTag" : "c1e0f4d0da028106a4235171c2c4d7d8",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.av-stories-best",
    "content" : {
      "id" : "/cps/news/business-45489064",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.video",
      "language" : "en-gb",
      "lastUpdated" : 1536707982000,
      "site" : "/news",
      "name" : "Who was to blame for the financial crisis?",
      "summary" : "BBC Business editor Simon Jack explores who could have been to blame for the global financial crisis.",
      "passport" : {
        "category" : {
          "categoryName" : "Explainer"
        }
      },
      "shortName" : "Who was to blame for the financial crisis?",
      "iStatsCounter" : "news.business.media_asset.45489064.page",
      "allowAdvertising" : True,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/10189/production/_103392956_p06kyh5t.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1024,
          "height" : 576,
          "href" : "http://c.files.bbci.co.uk/10189/production/_103392956_p06kyh5t.jpg",
          "altText" : "Animated characters",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/10189/production/_103392956_p06kyh5t.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06kygbl",
          "type" : "bbc.mobile.news.video",
          "duration" : 130000,
          "caption" : "Who was to blame for the financial crisis?",
          "externalId" : "p06kygbp",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06kyh9l.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45489064",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45489064",
      "iStatsLabels" : {
        "page_type" : "media-asset",
        "cps_asset_id" : "45489064"
      }
    }
  }, {
    "eTag" : "473f066076c1f8fb30084bd13afb1a02",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.av-stories-best",
    "content" : {
      "id" : "/cps/news/business-45491531",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.video",
      "language" : "en-gb",
      "lastUpdated" : 1536724823000,
      "site" : "/news",
      "name" : "Mark Carney: No one can rule out another financial crisis",
      "summary" : "The Bank of England governor says history shows that another financial crisis could occur.",
      "passport" : {
        "category" : {
          "categoryName" : "News"
        }
      },
      "shortName" : "Carney: Can't rule out another crisis",
      "iStatsCounter" : "news.business.media_asset.45491531.page",
      "allowAdvertising" : True,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/14BE8/production/_103386948_p06kxhjm.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1024,
          "height" : 576,
          "href" : "http://c.files.bbci.co.uk/14BE8/production/_103386948_p06kxhjm.jpg",
          "altText" : "Mark Carney",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/14BE8/production/_103386948_p06kxhjm.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06kxhc0",
          "type" : "bbc.mobile.news.video",
          "duration" : 146000,
          "caption" : "Bank of England governor Mark Carney says history shows no one can rule out another crisis",
          "externalId" : "p06kxhc2",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06kxhjm.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45491531",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45491531",
      "iStatsLabels" : {
        "page_type" : "media-asset",
        "cps_asset_id" : "45491531"
      }
    }
  }, {
    "eTag" : "4edeca24d9008e5b48ca172442c6f7bf",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.av-stories-best",
    "content" : {
      "id" : "/cps/news/business-45396884",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.video",
      "language" : "en-gb",
      "lastUpdated" : 1536621197000,
      "site" : "/news",
      "name" : "Using tools made me feel like a superwoman",
      "summary" : "One woman in New York is trying to encourage more girls to join the construction industry.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "Using tools made me feel like a superwoman",
      "iStatsCounter" : "news.business.media_asset.45396884.page",
      "allowAdvertising" : True,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/F43F/production/_103372526_p06ktwgx.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1024,
          "height" : 576,
          "href" : "http://c.files.bbci.co.uk/F43F/production/_103372526_p06ktwgx.jpg",
          "altText" : "Judaline Cassidy",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/F43F/production/_103372526_p06ktwgx.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.video",
        "secondaryType" : "bbc.mobile.news.placement.primary",
        "content" : {
          "id" : "/video/p06k4y1j",
          "type" : "bbc.mobile.news.video",
          "duration" : 94000,
          "caption" : "'Using tools gave me a sense of empowerment, almost like I became a superwoman'",
          "externalId" : "p06kzxdc",
          "isEmbeddable" : True,
          "isAvailable" : True,
          "relations" : [ ],
          "iChefUrl" : "http://ichef.bbci.co.uk/images/ic/$recipe/p06kzy6k.jpg"
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45396884",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45396884",
      "iStatsLabels" : {
        "page_type" : "media-asset",
        "cps_asset_id" : "45396884"
      }
    }
  }, {
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "3c11c15d68ca94e68acb3819444736ff",
      "type" : "bbc.mobile.news.group.link",
      "shareUrl" : "https://www.bbc.co.uk/news/resources/idt-sh/The_lost_decade",
      "name" : "The financial crisis: The lost decade",
      "lastUpdated" : 1536673653000,
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/6AE8/production/_103386372_skyline_getty.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/6AE8/production/_103386372_skyline_getty.jpg",
          "altText" : "London skyline",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/6AE8/production/_103386372_skyline_getty.jpg",
          "relations" : [ ]
        }
      } ],
      "allowAdvertising" : True,
      "iStatsLabels" : { }
    }
  }, {
    "eTag" : "4ff172421451975cf60a56081ebf59e4",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "/cps/news/business-45485255",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536794308000,
      "site" : "/news",
      "name" : "The UK's growing tech trade ties with Israel",
      "summary" : "As the UK looks at developing more trade deals outside the EU after Brexit, its increasing ties with Israel could provide the model.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "The UK's growing tech trade ties with Israel",
      "iStatsCounter" : "news.business.story.45485255.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/AC6B/production/_103393144_hi048470912.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/AC6B/production/_103393144_hi048470912.jpg",
          "altText" : "A Tevva Motors lorry",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/AC6B/production/_103393144_hi048470912.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45485255",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45485255",
      "summaryOverride" : " ",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45485255"
      }
    }
  }, {
    "eTag" : "59101451d072df52cf04e58083071fcf",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "/cps/news/business-44968514",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536708840000,
      "site" : "/news",
      "name" : "Who's winning the global race to offer superfast 5G?",
      "summary" : "China, the US and the UK are all vying to dominate the market for next-generation mobile networks.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "Who's winning the global race to offer superfast 5G?",
      "iStatsCounter" : "news.business.story.44968514.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/8708/production/_103386543_gettyimages-932866170.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 1024,
          "height" : 576,
          "href" : "http://c.files.bbci.co.uk/8708/production/_103386543_gettyimages-932866170.jpg",
          "altText" : "Ice skaters racing",
          "caption" : "5G was showcased in a variety of ways during this year's Winter Olympics",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/8708/production/_103386543_gettyimages-932866170.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-44968514",
      "shareUrl" : "http://www.bbc.co.uk/news/business-44968514",
      "summaryOverride" : " ",
      "nameOverride" : "Who's winning the race to offer superfast 5G?",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "44968514"
      }
    }
  }, {
    "eTag" : "aafbb090461498eb3c5ee940e89aa59f",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "/cps/news/business-45371502",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536708210000,
      "site" : "/news",
      "name" : "Why 12 is the magic number when it comes to composting",
      "summary" : "More and more packaging is claiming to be \"biodegradable\" or \"compostable\", but what does that really mean?",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "Why 12 is the magic number when it comes to composting",
      "iStatsCounter" : "news.business.story.45371502.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/14C87/production/_103272158_finishedcompost-1.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/14C87/production/_103272158_finishedcompost-1.jpg",
          "altText" : "Hands holding compost",
          "copyrightHolder" : "Jenny Grant",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/14C87/production/_103272158_finishedcompost-1.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45371502",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45371502",
      "summaryOverride" : "  ",
      "nameOverride" : "The magic number when it comes to composting",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45371502"
      }
    }
  }, {
    "eTag" : "396066d47153b6da4bfd417b8910b495",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "/cps/news/business-45481996",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536709005000,
      "site" : "/news",
      "name" : "Which universities will really impress the boss?",
      "summary" : "Which is the best university name in the world to put on a job application?",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "Which universities will really impress the boss?",
      "iStatsCounter" : "news.business.story.45481996.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/5D6E/production/_103381932_graduation2.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/5D6E/production/_103381932_graduation2.jpg",
          "altText" : "Graduation",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/5D6E/production/_103381932_graduation2.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45481996",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45481996",
      "summaryOverride" : " ",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45481996"
      }
    }
  }, {
    "eTag" : "28a6ba1dc80b086c9da23b523e274fb4",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "/cps/news/business-45470799",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536620617000,
      "site" : "/news",
      "name" : "'A new bladder made from my cells gave me my life back'",
      "summary" : "Specialised printers are helping to create organic replacement body parts more quickly and safely.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "'A new bladder made from my cells gave me my life back'",
      "iStatsCounter" : "news.business.story.45470799.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/1774C/production/_103367069_lukemassella.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/1774C/production/_103367069_lukemassella.jpg",
          "altText" : "Luke Massella as a boy with his parents",
          "caption" : "Luke Massella has to undergo surgery multiple times as a boy",
          "copyrightHolder" : "Massella Family",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/1774C/production/_103367069_lukemassella.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45470799",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45470799",
      "summaryOverride" : " ",
      "nameOverride" : "'A bladder made from my cells gave me my life back'",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45470799"
      }
    }
  }, {
    "eTag" : "8ae53ec3140a34497018511b693fda77",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "/cps/news/business-44846317",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536620930000,
      "site" : "/news",
      "name" : "The entrepreneur creating Ghana's next generation of inventors",
      "summary" : "Charles Ofori Antimpem is the inventor of a science set which is the size and price of a textbook which he now hopes to share with children across Africa.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "The entrepreneur behind Ghana's future inventors",
      "iStatsCounter" : "news.business.story.44846317.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/15F00/production/_102565898_15-year-oldprincessmakafui-right2.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/15F00/production/_102565898_15-year-oldprincessmakafui-right2.jpg",
          "altText" : "Princess Makafui and her friend use the science kit",
          "caption" : "Princess Makafui and her friend use the science kit",
          "copyrightHolder" : "BBC",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/15F00/production/_102565898_15-year-oldprincessmakafui-right2.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-44846317",
      "shareUrl" : "http://www.bbc.co.uk/news/business-44846317",
      "summaryOverride" : " ",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "44846317"
      }
    }
  }, {
    "eTag" : "45cee75f4525061ed8357e4fbfe627c0",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "/cps/news/business-45395216",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536534854000,
      "site" : "/news",
      "name" : "The dad who feeds his son burgers almost every day",
      "summary" : "A profile of Ethan Brown, the founder and boss of best-selling vegan burger company Beyond Meat.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "The dad who feeds his son burgers almost every day",
      "iStatsCounter" : "news.business.story.45395216.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/8887/production/_103315943_beyondmeat_ethanbrown_beyondburger.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/8887/production/_103315943_beyondmeat_ethanbrown_beyondburger.jpg",
          "altText" : "Ethan Brown",
          "copyrightHolder" : "Beyond Meat",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/8887/production/_103315943_beyondmeat_ethanbrown_beyondburger.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45395216",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45395216",
      "summaryOverride" : " ",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45395216"
      }
    }
  }, {
    "eTag" : "fde50dab3052324b06fa1e57888bd63e",
    "primaryType" : "bbc.mobile.news.item",
    "secondaryType" : "bbc.mobile.news.group.feature-main",
    "content" : {
      "id" : "/cps/news/business-45419105",
      "type" : "bbc.mobile.news.item",
      "format" : "bbc.mobile.news.format.textual",
      "language" : "en-gb",
      "lastUpdated" : 1536274810000,
      "site" : "/news",
      "name" : "Are 'swipe left' dating apps bad for our mental health?",
      "summary" : "Dating apps are hugely popular around the world, but some think they're making many of us unhappy.",
      "passport" : {
        "category" : {
          "categoryName" : "Feature"
        }
      },
      "shortName" : "Are 'swipe left' dating apps bad for our mental health?",
      "iStatsCounter" : "news.business.story.45419105.page",
      "relations" : [ {
        "primaryType" : "bbc.mobile.news.image",
        "secondaryType" : "bbc.mobile.news.placement.index",
        "content" : {
          "id" : "/cpsprodpb/15811/production/_103318088_gettyimages-871189020.jpg",
          "type" : "bbc.mobile.news.image",
          "width" : 976,
          "height" : 549,
          "href" : "http://c.files.bbci.co.uk/15811/production/_103318088_gettyimages-871189020.jpg",
          "altText" : "Sad girl listening to music on her phone",
          "caption" : "Too many rejections on dating apps can lower our self-esteem, psychologists say",
          "copyrightHolder" : "Getty Images",
          "urn" : "urn:bbc:content:assetUri:asset:prodpb/15811/production/_103318088_gettyimages-871189020.jpg",
          "relations" : [ ]
        }
      }, {
        "primaryType" : "bbc.mobile.news.collection",
        "secondaryType" : "bbc.mobile.news.home_section",
        "content" : {
          "id" : "/cps/news/business",
          "type" : "bbc.mobile.news.collection",
          "format" : "bbc.mobile.news.cps.idx",
          "language" : "en-gb",
          "lastUpdated" : 1536824521000,
          "site" : "/news",
          "name" : "Business",
          "summary" : "The latest BBC Business News: breaking personal finance, company, financial and economic news, plus insight and analysis into UK and global markets.",
          "iStatsCounter" : "news.business.page",
          "iStatsLabels" : {
            "page_type" : "index",
            "cps_asset_id" : "10059368"
          },
          "allowAdvertising" : True,
          "relations" : [ ],
          "urn" : "urn:bbc:content:assetUri:asset:/news/business",
          "shareUrl" : "http://www.bbc.co.uk/news/business",
          "eTag" : "412c170772317291285da46cc8bb111b"
        }
      } ],
      "urn" : "urn:bbc:content:assetUri:asset:/news/business-45419105",
      "shareUrl" : "http://www.bbc.co.uk/news/business-45419105",
      "summaryOverride" : " ",
      "iStatsLabels" : {
        "page_type" : "story",
        "cps_asset_id" : "45419105"
      }
    }
  } ],
  "urn" : "urn:bbc:content:assetUri:asset:/news/business",
  "shareUrl" : "http://www.bbc.co.uk/news/business",
  "eTag" : "412c170772317291285da46cc8bb111b"
}




CONTENT_API_TEMPLATE = 'http://content-api-a127.api.bbci.co.uk/asset/{}?api_key={}'
TREVOR_API_TEMPLATE = 'http://trevor-producer-cdn.api.bbci.co.uk/content/cps/{}'

LEVEL_INDENTERS = ['', '-', '---', '-----']


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


def AddLabelIfExistToTree(existing_tree, label, obj):
    if label in obj:
       existing_tree[label] = obj[label]

def walkTrevorResponseTree(jsonContent):
    tree_json = {}

    AddLabelIfExistToTree(tree_json, 'id', jsonContent)
    AddLabelIfExistToTree(tree_json, 'type', jsonContent)
    AddLabelIfExistToTree(tree_json, 'name', jsonContent)
    AddLabelIfExistToTree(tree_json, 'format', jsonContent)
    AddLabelIfExistToTree(tree_json, 'shareUrl', jsonContent)

    relations = jsonContent['relations']
    tree_relations_json = []
    tree_json['__meta_realtions_count'] = len(relations)
    r_pos = 0
    for relation in relations:
        tree_relation_json = {}
        tree_relation_json['__meta_relations_pos'] = r_pos
        r_pos = r_pos + 1
        AddLabelIfExistToTree(tree_relation_json, 'primaryType', relation)
        AddLabelIfExistToTree(tree_relation_json, 'secondaryType', relation)
        if 'content' in relation:
            AddLabelIfExistToTree(tree_relation_json, 'id', relation['content'])
            AddLabelIfExistToTree(tree_relation_json, 'type', relation['content'])
            AddLabelIfExistToTree(tree_relation_json, 'name', relation['content'])
            #AddLabelIfExistToTree(tree_relation_json, 'shortName', relation['content'])

        tree_relations_json.append(tree_relation_json)
    tree_json['relations'] = tree_relations_json

    return tree_json


def item_pos_in_trevor(item, label, trevor_tree):

    if label in item:
        #find in trevor
        assetUri = item[label]
        relations = trevor_tree['relations']
        for relation in relations:
            if relation['id'].find(assetUri) != -1:
                return relation['__meta_relations_pos']

    #not found
    return -1

def walkContentResponseTree(jsonContent, trevor_walked_tree):
  
    tree_json = {}
  

    results = jsonContent['results']
    if results is None or len(results) == 0: 
        return

    result = results[0]

    AddLabelIfExistToTree(tree_json, 'type', result)
    AddLabelIfExistToTree(tree_json, 'assetUri', result)
    AddLabelIfExistToTree(tree_json, 'title', result)

    #get groups
    groups = result['groups']
    tree_groups_json = []
    tree_json['__meta_group_count'] = len(groups)
    gp_pos = 0
    for group in groups:        
        tree_group_json = {}
        tree_group_json['__meta_groups_pos'] = gp_pos
        gp_pos = gp_pos + 1
        AddLabelIfExistToTree(tree_group_json, 'semanticGroupName', group)
        AddLabelIfExistToTree(tree_group_json, 'title', group)
        AddLabelIfExistToTree(tree_group_json, 'type', group)
        if 'strapline' in group:
            strapline = group['strapline']
            if strapline is not None:
                tree_group_json['strapline'] = strapline['name']
        
        tree_group_json['__meta_item_count'] = len(group['items'])
        tree_group_items_json = []
        pos = 0
        for item in group['items']:
            tree_group_item_json = {}
            #tree_group_item_json['__meta_item_pos'] = pos
            pos = pos + 1
            AddLabelIfExistToTree(tree_group_item_json, 'assetUri', item)
            AddLabelIfExistToTree(tree_group_item_json, 'assetTypeCode', item)
            AddLabelIfExistToTree(tree_group_item_json, 'title', item)
            AddLabelIfExistToTree(tree_group_item_json, 'type', item)
            AddLabelIfExistToTree(tree_group_item_json, 'headline', item)
            #see if item is found in Trevor tree
            tree_group_item_json['__meta_trevor_pos'] = item_pos_in_trevor(item, 'assetUri', trevor_walked_tree)
            if 'section' in item:
                section = item['section']
                if section is not None:
                    tree_group_item_json['section'] =section['name']
            
            tree_group_items_json.append(tree_group_item_json)

        tree_group_json['items'] = tree_group_items_json
        tree_groups_json.append(tree_group_json)
    tree_json['groups'] = tree_groups_json
    
    print json.dumps(tree_json, indent=4, sort_keys=True)
    return 

def get_content_fromcontent_api(root_url, cps_id, api_key):
    url = root_url.format(cps_id, api_key)
    
    headers = {'X-Candy-Platform' : 'mobile', 'X-Candy-Audience' : 'domestic', 'Accept' : 'application/json'}
    response = requests.get(url, cert=("/Users/mcalpn93/certificates/neilm_devcert.pem"), verify=False, headers=headers)
    return response.json()
    
    
def main(argv):

    api_key = ''
    cps_id = ''
    get_from_trevor = False

    try:
        opts, args = getopt.getopt(argv,"ha:i:tc")
    except getopt.GetoptError, error:
        print_options_manual()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_options_manual()
            sys.exit()
        elif opt == "-a":
            api_key = arg
        elif opt == "-i":
            cps_id = arg
        elif opt == "-t":
            get_from_trevor = True
        elif opt == "-c":
            get_from_trevor = False
            

    #print 'api_key:' + api_key + ' ' + 'cps_id' + cps_id 
    if cps_id is not None: 
        jsonTrevor = get_content_fromcontent_api(TREVOR_API_TEMPLATE, cps_id, api_key)        
        #test data
        #jsonTrevor = TEST_TREVOR_JSON
        trevor_walked_tree = walkTrevorResponseTree(jsonTrevor)
        
        if api_key is not None and get_from_trevor == False:
            #when walking the content we do a comparison against the Trevor feed to see what items 
            #make it into the Trevor feed (and what are filtered out)        
            jsonContent = get_content_fromcontent_api(CONTENT_API_TEMPLATE, cps_id, api_key)        
            #jsonContent = TEST_CONTENT_JSON
            walkContentResponseTree(jsonContent, trevor_walked_tree)
        else:
            print json.dumps(trevor_walked_tree, indent=4, sort_keys=True)
    else:
        #cannot do anything
        print_options_manual()

def print_options_manual():
	print 'tree_walker.py -a <api_key> -i <cps_index_id> -t (to get from trevor) -c (to get from content API)'
	print '      E.g. cpsindex_to_idealizedapi.py -s ffj55jfs34sds -i news/business -t '




if __name__ == "__main__":
   main(sys.argv[1:])



    

    

