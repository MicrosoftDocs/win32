---
description: Sets the title and subtitle that appear in the wizard header. In general, the client will display the header above the HTML and below the title bar.
title: WebWizardHost.SetHeaderText method (Shldisp.h)
ms.topic: reference
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
ms.assetid: e627de44-9929-4e08-9fd9-ca22743f434a
api_name: 
 - WebWizardHost.SetHeaderText
api_type: 
 - COM
api_location: 
 - Shldisp.h
topic_type: 
 - APIRef
 - kbSyntax

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

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

String containing the title.

</dd> <dt>

*bstrHeaderSubtitle* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

String containing the subtitle.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl> |



 

 
