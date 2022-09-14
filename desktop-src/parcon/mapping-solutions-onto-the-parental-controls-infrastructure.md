---
description: Mapping Solutions onto the Parental Controls Infrastructure
ms.assetid: 09677019-2cf9-43fe-b16c-e802767bef3a
title: Mapping Solutions onto the Parental Controls Infrastructure
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Solutions onto the Parental Controls Infrastructure

Five categories of common ISV and ISP/portal parental-controls aware offerings are readily apparent:

-   Standalone client application. Examples are email clients and media players. Although media players have Internet-facing risk and some have specific services, Windows Parental Controls primarily promotes logging and restrictions on playback activities only to minimize library impacts and logging noise to administrators.
-   Client/server solutions. The most prominent examples are instant messaging solutions.
-   ISP suites. These are collections of client/server solutions and client applications, often integrated in a single client user interface. Note that most of these also provide most or all functionality by using browser access, crossing over into web-only solutions.
-   Web-only solutions. Accessed through browser. Examples are web-based email and instant messaging functionality. Access to these may be blocked by appropriately populated web filter categories.
-   Firewall-like solutions. Provides filtering at the network stack level, and potentially other operating system restrictions.

Recommendations for implementing compliant solutions for each category are specified in the following table.



| Category                           | Logging                                                  | Restrictions settings                                    | Restrictions enforcement                                 | Web Content Filter replacement                                                        | Use of extensibility link for logging and settings access               |
|------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| "Stand-alone" client<br/>    | Required on client<br/>                            | Required on client<br/>                            | Required on client<br/>                            | N/A<br/>                                                                        | Required, will be exe. May simply invoke app UI navigation<br/>   |
| Client/server solution<br/>  | Required on client if not performed by server<br/> | Required on client if not performed by server<br/> | Required on client if not performed by server<br/> | N/A<br/>                                                                        | Required, will be exe<br/>                                        |
| ISP suite<br/>               | Required on client if not performed by server<br/> | Required on client if not performed by server<br/> | Required on client if not performed by server<br/> | Recommend using WPC filter, but allow replacement if robust for multi-user<br/> | Required, will be exe<br/>                                        |
| Web-only solution<br/>       | Recommend performing on server<br/>                | Recommend performing on server<br/>                | Recommend performing on server<br/>                | N/A<br/>                                                                        | Recommended. Expose server logging and settings by using exe<br/> |
| Firewall-like solutions<br/> | Required on client<br/>                            | Required on client<br/>                            | Required on client<br/>                            | Recommend using WPC filter, but allow replacement if robust for multi-user<br/> | Required, will be exe<br/>                                        |



 

 

 




