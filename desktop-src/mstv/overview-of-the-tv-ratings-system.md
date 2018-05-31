---
title: Overview of the TV Ratings System
description: Overview of the TV Ratings System
ms.assetid: f1ebfb27-73ba-479e-8071-26c79dbd43f7
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Overview of the TV Ratings System

This topic applies only to Windows XP Service Pack 1 or later.

The Microsoft TV Ratings system provides a way for Microsoft  Windows  Media Center to access content ratings from a broadcast stream and use them to make decisions about whether or not to display the content. These ratings are mandatory on all US broadcast streams, and are contained in the extended data services (XDS) channel of line 21.

The TV Ratings System uses two COM objects that are provided by third-party developers:

-   The **XDSToRat** (Ratings Decoder) object parses XDS data into content ratings.
-   The **EvalRat** (Ratings Evaluator) object determines whether broadcast content is allowed to be viewed, based on the rating and the current permissions.

The **XDSToRat** and **EvalRat** objects are both COM objects. The **XDSToRat** object exposes the [**IXDSToRat**](/previous-versions/windows/desktop/api/Tvratings/nn-tvratings-ixdstorat) interface, and the **EvalRat** object exposes the [**IEvalRat**](/previous-versions/windows/desktop/api/Tvratings/nn-tvratings-ievalrat) interface.

TV ratings are a combination of three things: rating system, rating level, and attributes.

-   Rating *systems* vary by country/region, and one country/region may have more than one system. For example, Canada has both English and French rating systems, and the United States has both MPAA and TV rating systems. Rating systems are enumerated by the [**EnTvRat\_System**](/previous-versions/windows/desktop/api/Tvratings/ne-tvratings-entvrat_system) enumeration.
-   Each system has *levels*. For example, the MPAA uses G, PG, R, and other levels. The number of levels in use varies by system, but the Microsoft TV Rating system provides eight levels. Unused levels can be ignored. Each system has an enumeration that lists its levels.
-   Each level can have additional content *attributes*. For example, the United States TV system uses additional attribute tags for content containing violence, adult situations, and so on. Currently, only the United States TV rating system uses additional content attributes.

Each rating system can be treated as a permission grid, where each column specifies the allowable permissions and each row specifies a rating level. The use of this grid model allows very specific permissions to be set, and to even interleave allowable viewing levels with disallowed viewing levels. Because one level is prohibited does not require that more restrictive levels be prohibited as well. The following table shows a sample permission grid using the US TV rating system.

**US TV rating system (US\_TV)**



|                 |                                          |                                          |                                                  |                                                |                                                           |          |          |          |
|-----------------|------------------------------------------|------------------------------------------|--------------------------------------------------|------------------------------------------------|-----------------------------------------------------------|----------|----------|----------|
| Attribute Level | US\_TV\_<br/> IsBlocked<br/> | US\_TV\_<br/> IsViolent<br/> | US\_TV\_IsSexual<br/> Situation<br/> | US\_TV\_Is<br/> AdultLanguage<br/> | US\_TV\_IsSexually<br/> SuggestiveDialog<br/> | Not used | Not used | Not used |
| None            | 0                                        | 0                                        | 0                                                | 0                                              | 0                                                         | 0        | 0        | 0        |
| Y               | 0                                        | 0                                        | 0                                                | 0                                              | 0                                                         | 0        | 0        | 0        |
| Y7              | 0                                        | 0                                        | 0                                                | 0                                              | 0                                                         | 0        | 0        | 0        |
| G               | 1                                        | 0                                        | 0                                                | 0                                              | 0                                                         | 0        | 0        | 0        |
| PG              | 0                                        | 1                                        | 0                                                | 0                                              | 0                                                         | 0        | 0        | 0        |
| 14              | 0                                        | 1                                        | 1                                                | 0                                              | 1                                                         | 0        | 0        | 0        |
| MA              | 1                                        | 0                                        | 0                                                | 0                                              | 0                                                         | 0        | 0        | 0        |
| None 2          | 0                                        | 0                                        | 0                                                | 0                                              | 0                                                         | 0        | 0        | 0        |



 

The preceding table shows the enumerated values for the attributes as column headings, and the levels as rows. Each row shows an 8-bit attribute field that describes viewing permissions. A value of 1 means restricted, and a value of 0 means not restricted.

The preceding table can be interpreted as follows:

-   No restrictions on nonrated programs (a nonrating is given to news or sports, generally).
-   No restrictions on "Y" or "Y7" rated programs.
-   Do not permit "G" rated programs.
-   Allow all "PG" programs except those showing violence.
-   Allow only "14" rated programs with no additional attributes or adult language.
-   Do not permit "MA" rated programs.

Notice that the **IsBlocked** bit blocks playback of that level regardless of any other attributes that are set, so when setting the **IsBlocked** bit, it is not necessary to specify any other restrictions (which will be ignored anyway).

Also notice how the restricted rated-G row does not prevent playback of more restrictive levels. This is an unlikely example of the use of this property, but it does show that levels do not affect each other, and that permissions for all levels must be set.

The enumerated names for levels and attributes are only used to make the code more readable. Any enumeration values used for levels or attributes in the same ordinal position can be substituted for any other. The essential idea is an eight-bit by eight-bit grid.

**Unrated Programs**

A program is *unrated* if a rating has not yet been detected in the broadcast. All programs are considered unrated when they are received, until a valid program rating is processed by the [XDSToRat](xdstorat-object.md) object.

Different broadcasters may post ratings information at different time intervals, and content may remain unrated for a significant amount of time. Also, programs can be changed to an unrated status by certain XDS codes. See EIA-608B, section 9.5.1.5.4 for details.

Note that "unrated" is not the same as the "None" or "Exempt" ratings in the US or Canadian TV rating systems, or "Not Rated" in the MPAA system. These are valid ratings, and are treated as such.

**Building the EvalRat and XDSToRat Objects**

In order to understand and build these objects, a programmer must be familiar with the EIA/CEA-608-B specifications, which explain the format of XDS packets. To build the **EvalRat** or **XDSToRat** objects, an application must include TvRatings.h.

## Related topics

<dl> <dt>

[TV Ratings Components](tv-ratings-components.md)
</dt> </dl>

 

 





