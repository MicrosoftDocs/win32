---
Description: Sets the title and subtitle that appear in the wizard header. In general, the client will display the header above the HTML and below the title bar.
title: WebWizardHost.SetHeaderText method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WebWizardHost.SetHeaderText
api_type: 
- COM
api_location: 
- Shldisp.h
---

# WebWizardHost.SetHeaderText method

Sets the title and subtitle that appear in the wizard header. In general, the client will display the header above the HTML and below the title bar.

## Syntax


```JScript
iRetVal = WebWizardHost.SetHeaderText(
  bstrHeaderTitle,
  bstrHeaderSubtitle
)
```



## Parameters

<dl> <dt>

*bstrHeaderTitle* \[in\]
</dt> <dd>

Type: **[**BSTR**](https://msdn.microsoft.com/en-us/library/ms221069(v=VS.71).aspx)**

String containing the title.

</dd> <dt>

*bstrHeaderSubtitle* \[in\]
</dt> <dd>

Type: **[**BSTR**](https://msdn.microsoft.com/en-us/library/ms221069(v=VS.71).aspx)**

String containing the subtitle.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl> |



 

 




