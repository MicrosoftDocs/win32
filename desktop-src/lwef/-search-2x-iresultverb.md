---
title: IResultVerb interface
description: Exposes verb properties.
ms.assetid: 8cc8408e-0117-4344-ad26-0c4a5d09a935
keywords:
- IResultVerb interface Legacy Windows Environment Features
- IResultVerb interface Legacy Windows Environment Features , described
topic_type:
- apiref
api_name:
- IResultVerb
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultVerb interface

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

Exposes verb properties.

## Members

The **IResultVerb** interface inherits from the [**IUnknown**](https://docs.microsoft.com/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IResultVerb** also has these types of members:

-   [Properties](#properties)

### Properties

The **IResultVerb** interface has these properties.



| Property                                                             | Access type           | Description                                                                                                       |
|:---------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------|
| [**DisplayName**](-search-2x-iresultverb-displayname.md)<br/> | Read-only<br/>  | This property returns a pointer to the localized display name for the verb. <br/>                           |
| [**DoIt**](-search-2x-iresultverb-doit.md)<br/>               | Write-only<br/> | Executes the verb. <br/>                                                                                    |
| [**Enabled**](-search-2x-iresultverb-enabled.md)<br/>         | Read-only<br/>  | This property returns TRUE if the verb is enabled. <br/>                                                    |
| [**HelpText**](-search-2x-iresultverb-helptext.md)<br/>       | Read-only<br/>  | This property returns a pointer to the localized help string for the verb. <br/>                            |
| [**Icon**](-search-2x-iresultverb-icon.md)<br/>               | Read-only<br/>  | This property returns a pointer to handle of the optional icon associated with the verb. <br/>              |
| [**Name**](-search-2x-iresultverb-name.md)<br/>               | Read-only<br/>  | This property returns a pointer to the cononical name for the verb such as print, open, and so forth. <br/> |



 

## Remarks

These methods expose properties and actions applicable to verbs.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>                                               |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





