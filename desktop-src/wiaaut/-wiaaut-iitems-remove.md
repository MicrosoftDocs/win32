---
title: Items.Remove method
description: Removes the designated Item.
ms.assetid: '9f80b62e-0d55-4c85-9c65-c1dd3a72fe9a'
keywords: ["Remove method WIA Automation", "Remove method WIA Automation , Items object", "Items object WIA Automation , Remove method"]
topic_type:
- apiref
api_name:
- Items.Remove
api_location:
- Wiaaut.h
api_type:
- COM
---

# Items.Remove method

Removes the designated [**Item**](-wiaaut-item.md).

## Syntax


```VB
Items.Remove( _
  ByVal Index As LONG _
) As HRESULT
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **LONG**

Required. **Long** value.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example code, see [Implement a Windows Script Host Script that Runs Automatically](-wiaaut-shared-samples.md#implement-a-windows-script-host-script-that-runs-automatically) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Items**](-wiaaut-items.md)
</dt> </dl>

 

 





