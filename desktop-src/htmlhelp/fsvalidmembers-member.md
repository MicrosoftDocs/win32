---
title: fsValidMembers Member
description: fsValidMembers Member
ms.assetid: 99230C25-8C54-4ce6-AB4B-4E397D69A84E
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# fsValidMembers Member

The *fsValidMembers* member is used when modifying an existing window type, and determines which of the other members should be updated. This parameter can be a combination of one or more of the following values.



| Value                    | Description                            |
|--------------------------|----------------------------------------|
| HHWIN\_PARAM\_CUR\_TAB   | The *curNavType* member is valid.      |
| HHWIN\_PARAM\_EXPANSION  | The *fNotExpanded* member is valid.    |
| HHWIN\_PARAM\_EXSTYLES   | The *dwExStyles* member is valid.      |
| HHWIN\_PARAM\_NAV\_WIDTH | The *iNavWidth* member is valid.       |
| HHWIN\_PARAM\_PROPERTIES | The *fsWinProperties* member is valid. |
| HHWIN\_PARAM\_STYLES     | The *dwStyles* member is valid.        |
| HHWIN\_PARAM\_RECT       | The *rcWindowPos* member is valid.     |
| HHWIN\_PARAM\_SHOWSTATE  | The *nShowState* member is valid.      |
| HHWIN\_PARAM\_TB\_FLAGS  | The *fsToolBarFlags* member is valid.  |



 

## Related topics

<dl> <dt>

[**Back to HH\_WINTYPE**](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghh_wintype)
</dt> </dl>

 

 




