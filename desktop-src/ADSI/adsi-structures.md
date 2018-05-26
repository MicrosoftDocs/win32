---
title: ADSI Structures
description: Active Directory Service Interfaces (ADSI) define and use the structures listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3ee0e469-9932-4135-8798-27d318011786
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,reference,structures
- structures ADSI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Structures

Active Directory Service Interfaces (ADSI) define and use the structures listed in the following table.



| Structure                                                                      | Description                                                                                                    |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**ADS\_ATTR\_DEF**](/windows/win32/Iads/ns-iads-_ads_attr_def?branch=master)<br/>                              | Describes a set of attribute definitions of an **attributeSchema** object.<br/>                          |
| [**ADS\_ATTR\_INFO**](/windows/win32/Iads/ns-iads-_ads_attr_info?branch=master)<br/>                            | Holds the value of a named attribute and specifies operations to modify the attribute.<br/>              |
| [**ADS\_BACKLINK**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0008?branch=master)<br/>                               | Represents an ADSI representation of the **Back Link** attribute.<br/>                                   |
| [**ADS\_CASEIGNORE\_LIST**](/windows/win32/Iads/ns-iads-_ads_caseignore_list?branch=master)<br/>                | Represents an ADSI representation of the **Case Ignore List** attribute.<br/>                            |
| [**ADS\_CLASS\_DEF**](/windows/win32/Iads/ns-iads-_ads_class_def?branch=master)<br/>                            | Describes schema data for an object.<br/>                                                                |
| [**ADS\_DN\_WITH\_BINARY**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0015?branch=master)<br/>                 | An ADSI-defined structure that maps a distinguished name to an object **GUID**.<br/>                     |
| [**ADS\_DN\_WITH\_STRING**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0016?branch=master)<br/>                 | An ADSI-defined structure that maps a distinguished name of an object to a nonvarying string value.<br/> |
| [**ADS\_EMAIL**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0014?branch=master)<br/>                                     | Represents an ADSI representation of the **EMail** attribute.<br/>                                       |
| [**ADS\_FAXNUMBER**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0013?branch=master)<br/>                             | Represents an ADSI representation of the **Facsimile Telephone Number** attribute.<br/>                  |
| [**ADS\_HOLD**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0010?branch=master)<br/>                                       | Represents an ADSI representation of the **Hold** attribute.<br/>                                        |
| [**ADS\_NETADDRESS**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0011?branch=master)<br/>                           | Represents an ADSI representation of the **Net Address** attribute.<br/>                                 |
| [**ADS\_NT\_SECURITY\_DESCRIPTOR**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0003?branch=master)<br/> | Describes a security descriptor.<br/>                                                                    |
| [**ADS\_OBJECT\_INFO**](/windows/win32/Iads/ns-iads-_ads_object_info?branch=master)<br/>                        | Describes directory service object data.<br/>                                                            |
| [**ADS\_OCTET\_LIST**](/windows/win32/Iads/ns-iads-_ads_octet_list?branch=master)<br/>                          | Represents an ADSI representation of the **Octet List** attribute.<br/>                                  |
| [**ADS\_OCTET\_STRING**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0002?branch=master)<br/>                      | Represents an ADSI representation of the **Octet String** attribute.<br/>                                |
| [**ADS\_PATH**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0005?branch=master)<br/>                                       | Represents an ADSI representation of the **Path** attribute.<br/>                                        |
| [**ADS\_POSTALADDRESS**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0006?branch=master)<br/>                     | Represents an ADSI representation of the **Postal Address** attribute.<br/>                              |
| [**ADS\_PROV\_SPECIFIC**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0004?branch=master)<br/>                    | Describes a provider-specific data type.<br/>                                                            |
| [**ADS\_REPLICAPOINTER**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0012?branch=master)<br/>                   | Represents an ADSI representation of the Replica Pointer attribute.<br/>                                 |
| [**ADS\_SEARCH\_COLUMN**](/windows/win32/Iads/ns-iads-ads_search_column?branch=master)<br/>                    | Represents a column resulting from a directory query.<br/>                                               |
| [**ADS\_SEARCHPREF\_INFO**](/windows/win32/Iads/ns-iads-ads_searchpref_info?branch=master)<br/>                | Describes query preferences.<br/>                                                                        |
| [**ADS\_SORTKEY**](/windows/win32/Iads/ns-iads-_ads_sortkey?branch=master)<br/>                                 | Describes the sort key used for sorting a query.<br/>                                                    |
| [**ADS\_TIMESTAMP**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0007?branch=master)<br/>                             | Represents an ADSI representation of the **Timestamp** attribute.<br/>                                   |
| [**ADS\_TYPEDNAME**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0009?branch=master)<br/>                             | Represents an ADSI representation of the **Typed Name** attribute.<br/>                                  |
| [**ADSVALUE**](/windows/win32/Iads/ns-iads-_adsvalue?branch=master)<br/>                                        | Describes the value of an ADSI data type.<br/>                                                           |
| [**ADS\_VLV**](/windows/win32/Iads/ns-iads-_ads_vlv?branch=master)<br/>                                         | Specifies that the virtual list view should be used when returning search results from the server.<br/>  |



 

 

 





