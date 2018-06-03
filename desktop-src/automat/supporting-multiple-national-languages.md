---
title: Supporting Multiple National Languages
description: The IDispatch interface provides a range of solutions that vary in cost of implementation and quality of language support.
ms.assetid: 47dc5add-232c-4268-b977-43e12da81ede
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Supporting Multiple National Languages

Applications sometimes need to expose objects with names that differ across localized versions of the product. The names pose a problem for programming languages that need to access these objects, because late binding will be sensitive to the locale of the application. The [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface provides a range of solutions that vary in cost of implementation and quality of language support. All methods of the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface that are potentially sensitive to language are passed a LCID, which identifies the local language context.

The following are some of the approaches a class implementation can take:

-   Accept any LCID and use the same member names in all locales. This is acceptable if the exposed interface will typically be accessed only by very advanced users. For example, the member names for OLE interfaces will never be localized.

-   Accept all LCIDs supported by all versions of the product. In this case, the implementation of [**GetIDsOfNames**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-getidsofnames) would need to interpret the passed array of names based on the given LCID. This is the most acceptable solution because it allows users to write code in their natural language and run the code on any localized version of the application.

-   Return an error (DISP\_E\_UNKNOWNLCID) from [**GetIDsOfNames**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-getidsofnames) if the caller's LCID does not match the localized version of the class. This prevents users from being able to write late-bound code that runs on machines with different localized implementations of the class.

-   Recognize the particular version's localized names, as well as one language that is recognized in all versions. For example, a French version might accept French and English names, where English is the language supported in all versions. Users who want to write code that runs in all countries/regions would have to use English names.

To provide general language support, the application should check the LCID before interpreting member names. Because [**Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke) is passed a LCID, methods can properly interpret parameters whose meaning varies by locale. The following sections provide examples and guidelines for creating multilingual applications.

## In this section



| Topic                                                                                                                                 | Description                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Implementing IDispatch for Multilingual Applications](implementing-idispatch-for-multilingual-applications.md)<br/>           | When creating applications that will support multiple languages, you need to create separate type libraries for each supported language, as well as for versions of the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) member functions that include dependencies for each language.<br/> |
| [Implementing the IDispatch Member Functions](implementing-the-idispatch-member-functions.md)<br/>                             | The [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) member functions must be implemented in such a way as to take into account any language-specific features.<br/>                                                                                                                        |
| [Creating Separate Type Libraries](creating-separate-type-libraries.md)<br/>                                                   | For each supported language, write and register a separate type library.<br/>                                                                                                                                                                                             |
| [Defining the Locale IDs](defining-the-locale-ids.md)<br/>                                                                     | Demonstrates how to use locale IDs.<br/>                                                                                                                                                                                                                                  |
| [Loading Type Information](loading-type-information.md)<br/>                                                                   | Demonstrates how to load locale-specific type library information.<br/>                                                                                                                                                                                                   |
| [Interpreting Arguments and Strings Based on the Locale ID](interpreting-arguments-and-strings-based-on-the-locale-id.md)<br/> | Some methods or properties need to interpret arguments based on the LCID.<br/>                                                                                                                                                                                            |



 

 

 





