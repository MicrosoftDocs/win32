---
Description: 'Sets the title and subtitle that appear in the wizard header. In general, the client will display the header above the HTML and below the title bar.'
title: 'WebWizardHost.SetHeaderText method'
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

Type: **[**BSTR**](1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

String containing the title.

</dd> <dt>

*bstrHeaderSubtitle* \[in\]
</dt> <dd>

Type: **[**BSTR**](1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

String containing the subtitle.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl> |



 

 




