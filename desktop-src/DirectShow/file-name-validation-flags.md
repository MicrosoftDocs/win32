---
description: These flags specify the behavior of the media locator.
ms.assetid: 60afb2e8-cdd1-493e-8fc8-6fa581720b8d
title: File Name Validation Flags (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SFN_VALIDATEF_CHECK
- SFN_VALIDATEF_POPUP
- SFN_VALIDATEF_TELLME
- SFN_VALIDATEF_REPLACE
- SFN_VALIDATEF_USELOCAL
- SFN_VALIDATEF_NOFIND
- SFN_VALIDATEF_IGNOREMUTED
api_type: 
- HeaderDef
api_location: 
- Qedit.h
---

# File Name Validation Flags

\[Deprecated. This API may be removed from future releases of Windows.\]

These flags specify the behavior of the media locator.



| Constant/value                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                    |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SFN_VALIDATEF_CHECK"></span><span id="sfn_validatef_check"></span><dl> <dt>**SFN\_VALIDATEF\_CHECK**</dt> <dt>0x01</dt> </dl>                   | Check the validity of file names. You must set this flag to validate file names. If not, the other flags have no effect.<br/>                                                                                            |
| <span id="SFN_VALIDATEF_POPUP"></span><span id="sfn_validatef_popup"></span><dl> <dt>**SFN\_VALIDATEF\_POPUP**</dt> <dt>0x02</dt> </dl>                   | If a file is not located, display an Open File dialog box for the end user.<br/>                                                                                                                                         |
| <span id="SFN_VALIDATEF_TELLME"></span><span id="sfn_validatef_tellme"></span><dl> <dt>**SFN\_VALIDATEF\_TELLME**</dt> <dt>0x04</dt> </dl>                | If a missing file is located, briefly display a message box with the name and location of the file. This flag is mostly useful for testing purposes; the message box is probably not suitable for a retail product.<br/> |
| <span id="SFN_VALIDATEF_REPLACE"></span><span id="sfn_validatef_replace"></span><dl> <dt>**SFN\_VALIDATEF\_REPLACE**</dt> <dt>0x08</dt> </dl>             | If a missing file is located, update the name of the source object. (Only valid in the [**IAMTimeline::ValidateSourceNames**](iamtimeline-validatesourcenames.md) method.)<br/>                                         |
| <span id="SFN_VALIDATEF_USELOCAL"></span><span id="sfn_validatef_uselocal"></span><dl> <dt>**SFN\_VALIDATEF\_USELOCAL**</dt> <dt>0x10</dt> </dl>          | Always use a local file, even if a version of the file exists on the network.<br/>                                                                                                                                       |
| <span id="SFN_VALIDATEF_NOFIND"></span><span id="sfn_validatef_nofind"></span><dl> <dt>**SFN\_VALIDATEF\_NOFIND**</dt> <dt>0x20</dt> </dl>                | Do not search for missing files. File names are still validated if you set the SFN\_VALIDATEF\_CHECK flag.<br/>                                                                                                          |
| <span id="SFN_VALIDATEF_IGNOREMUTED"></span><span id="sfn_validatef_ignoremuted"></span><dl> <dt>**SFN\_VALIDATEF\_IGNOREMUTED**</dt> <dt>0x40</dt> </dl> | Ignore muted source objects. (Only valid in the [**IAMTimeline::ValidateSourceNames**](iamtimeline-validatesourcenames.md) method.)<br/>                                                                                |



## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IMediaLocator::FindMediaFile**](imedialocator-findmediafile.md)
</dt> <dt>

[**IRenderEngine::SetSourceNameValidation**](irenderengine-setsourcenamevalidation.md)
</dt> </dl>

 

 




