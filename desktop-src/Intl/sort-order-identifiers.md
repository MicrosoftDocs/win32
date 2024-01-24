---
description: This topic describes sort order identifiers, which can be used in the preparation of locale identifiers.
ms.assetid: abef64b5-ca3f-4cb3-92f0-1b7286bfb686
title: Sort Order Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Sort Order Identifiers

This topic describes sort order identifiers, which can be used in the preparation of [locale identifiers](locale-identifiers.md). A sort order identifier is defined in the form "\_sortorder", at the end of the locale name used in the identifier, for example, "de-DE\_phoneb", where "phoneb" is the sort order. The corresponding locale identifier is created as follows: `MAKELCID(MAKELANGID(LANG_GERMAN, SUBLANG_GERMAN), SORT_GERMAN_PHONE_BOOK)`.



| Constant                      | Locale name                                                                                         | Meaning                                                           |
|-------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| SORT\_CHINESE\_BIG5           | zh-TW<br/> zh-HK<br/> zh-MO<br/>                                                  | Chinese BIG5 order                                                |
| SORT\_CHINESE\_BOPOMOFO       | zh-TW\_pronun                                                                                       | Traditional Chinese Bopomofo order                                |
| SORT\_CHINESE\_PHONE\_BOOK    | zh-CN\_phoneb<br/>                                                                            | Chinese phone book (surname) order                                |
| SORT\_CHINESE\_PRC            | zh-CN\_stroke<br/> zh-HK\_stroke<br/> zh-MO\_stroke<br/> zh-SG\_stroke<br/> | PRC Chinese stroke count order                                    |
| SORT\_CHINESE\_PRCP           | zh-CN<br/> zh-SG<br/>                                                                   | PRC Chinese phonetic order                                        |
| SORT\_CHINESE\_RADICALSTROKE  | zh-TW<br/> zh-HK<br/> zh-MO<br/>                                                  | Chinese radical/stroke order                                      |
| SORT\_CHINESE\_UNICODE        | —                                                                                                   | Chinese Unicode order**Windows 2000:** Not supported.<br/>  |
| SORT\_DEFAULT                 | Locale name that is the same as the corresponding language name                                     | Default sort order                                                |
| SORT\_GEORGIAN\_MODERN        | ka-GE\_modern                                                                                       | Georgian modern order                                             |
| SORT\_GEORGIAN\_TRADITIONAL   | ka-GE                                                                                               | Georgian traditional order                                        |
| SORT\_GERMAN\_PHONE\_BOOK     | de-DE\_phoneb                                                                                       | German phone book order                                           |
| SORT\_HUNGARIAN\_DEFAULT      | hu-HU                                                                                               | Hungarian default order                                           |
| SORT\_HUNGARIAN\_TECHNICAL    | hu-HU\_technl                                                                                       | Hungarian technical order                                         |
| SORT\_JAPANESE\_RADICALSTROKE | ja-JP                                                                                               | Japanese radical/stroke order                                     |
| SORT\_JAPANESE\_UNICODE       | —                                                                                                   | Japanese Unicode order**Windows 2000:** Not supported.<br/> |
| SORT\_JAPANESE\_XJIS          | ja-JP                                                                                               | Japanese XJIS order                                               |
| SORT\_KOREAN\_KSC             | ko-KR                                                                                               | Korean KSC order                                                  |
| SORT\_KOREAN\_UNICODE         | —                                                                                                   | Korean Unicode order**Windows 2000:** Not supported.<br/>   |



 

 

 




