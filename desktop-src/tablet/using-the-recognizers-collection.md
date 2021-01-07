---
description: If you use multiple recognizers, you can use the Recognizers collection to list available recognizers and enable a user to select from among them.
ms.assetid: 1b89def0-3491-42da-9138-5280002e447a
title: Using the Recognizers Collection
ms.topic: article
ms.date: 05/31/2018
---

# Using the Recognizers Collection

If you use multiple recognizers, you can use the [**Recognizers**](/previous-versions/windows/desktop/legacy/ms702438(v=vs.85)) collection to list available recognizers and enable a user to select from among them. A **Recognizers** collection checks for installed recognizers, queries the attributes of the [**Recognizer**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognizer) objects, and stores the results. Applications can use the **Recognizers** collection to display a list of available recognizers without loading each recognizer DLL.

> [!Note]  
> The [**Recognizers**](/previous-versions/windows/desktop/legacy/ms702438(v=vs.85)) collection uses the system registry to check for both Microsoft recognizers and third-party recognizers.

 

The following table shows the values of the language identifiers each Microsoft recognizer supports.

> [!Note]  
> There are no language identifiers associated with the Microsoft gesture recognizer.

 



| Recognizer Name                                                      | Primary Language Id, Sublanguage Id (in order supported)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Microsoft Gesture Recognizer<br/>                              | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Microsoft English (United Kingdom) Handwriting Recognizer<br/> | LANG\_ENGLISH, SUBLANG\_ENGLISH\_UK<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_EIRE<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Microsoft English (United States) Handwriting Recognizer<br/>  | LANG\_ENGLISH, SUBLANG\_ENGLISH\_US<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_AUS<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_BELIZE<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_CAN<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_CARIBBEAN<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_JAMAICA<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_NZ<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_PHILIPPINES<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_SOUTH\_AFRICA<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_TRINIDAD<br/> LANG\_ENGLISH, SUBLANG\_ENGLISH\_ZIMBABWE<br/> LANG\_ENGLISH, SUBLANG\_NEUTRAL<br/> |
| Microsoft French Handwriting Recognizer<br/>                   | LANG\_FRENCH, SUBLANG\_FRENCH<br/> LANG\_FRENCH, SUBLANG\_FRENCH\_BELGIAN<br/> LANG\_FRENCH, SUBLANG\_FRENCH\_CANADIAN<br/> LANG\_FRENCH, SUBLANG\_FRENCH\_LUXEMBOURG<br/> LANG\_FRENCH, SUBLANG\_FRENCH\_MONACO<br/> LANG\_FRENCH, SUBLANG\_FRENCH\_SWISS<br/> LANG\_FRENCH, SUBLANG\_NEUTRAL<br/>                                                                                                                                                                                                                                                                                     |
| Microsoft German Handwriting Recognizer<br/>                   | LANG\_GERMAN, SUBLANG\_GERMAN<br/> LANG\_GERMAN, SUBLANG\_GERMAN\_AUSTRIAN<br/> LANG\_GERMAN, SUBLANG\_GERMAN\_LIECHTENSTEIN<br/> LANG\_GERMAN, SUBLANG\_GERMAN\_LUXEMBOURG<br/> LANG\_GERMAN, SUBLANG\_GERMAN\_SWISS<br/> LANG\_GERMAN, SUBLANG\_NEUTRAL<br/>                                                                                                                                                                                                                                                                                                                                |
| Microsoft Spanish Handwriting Recognizer<br/>                  | LANG\_SPANISH, SUBLANG\_SPANISH<br/> LANG\_SPANISH, SUBLANG\_NEUTRAL<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Microsoft Japanese Handwriting Recognizer<br/>                 | LANG\_JAPANESE, SUBLANG\_NEUTRAL<br/> LANG\_JAPANESE, SUBLANG\_DEFAULT<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Microsoft Korean Handwriting Recognizer<br/>                   | LANG\_KOREAN, SUBLANG\_NEUTRAL<br/> LANG\_KOREAN, SUBLANG\_DEFAULT<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Microsoft Chinese (Simplified) Handwriting Recognizer<br/>     | LANG\_CHINESE, SUBLANG\_CHINESE\_SIMPLIFIED<br/> LANG\_CHINESE, SUBLANG\_CHINESE\_SINGAPORE<br/> LANG\_CHINESE, SUBLANG\_NEUTRAL<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Microsoft Chinese (Traditional) Handwriting Recognizer<br/>    | LANG\_CHINESE, SUBLANG\_CHINESE\_TRADITIONAL<br/> LANG\_CHINESE, SUBLANG\_CHINESE\_HONGKONG<br/> LANG\_CHINESE, SUBLANG\_CHINESE\_MACAU<br/> LANG\_CHINESE, SUBLANG\_NEUTRAL<br/>                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

For more information about language identifiers, see [Language Identifier Constants and Strings](../intl/language-identifier-constants-and-strings.md).

 

 
