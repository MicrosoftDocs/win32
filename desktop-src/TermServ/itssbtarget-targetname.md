---
title: ITsSbTarget TargetName property
description: Specifies or retrieves the name of the target.
ms.assetid: ba5c3158-b4bc-457f-94ea-adb2e0852129
ms.tgt_platform: multiple
keywords:
- TargetName property Remote Desktop Services
- TargetName property Remote Desktop Services , ITsSbTarget interface
- ITsSbTarget interface Remote Desktop Services , TargetName property
- TargetName property Remote Desktop Services , ITsSbTargetEx interface
- ITsSbTargetEx interface Remote Desktop Services , TargetName property
topic_type:
- apiref
api_name:
- ITsSbTarget.TargetName
- ITsSbTarget.get_TargetName
- ITsSbTarget.put_TargetName
- ITsSbTargetEx.TargetName
- ITsSbTargetEx.get_TargetName
- ITsSbTargetEx.put_TargetName
api_location:
- Sbtsv.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbTarget::TargetName property

Specifies or retrieves the name of the target.

This property is read/write.

## Syntax


```C++
HRESULT put_TargetName(
  [in]          BSTR Val
);

HRESULT get_TargetName(
  [out, retval] BSTR *pVal
);
```



## Property value

A **BSTR** variable that specifies the target name.

## Remarks

This property was read-only prior to Windows Server 2012.

## Requirements




| Requirement | Value |
|--------|-------|
| Minimum supported client<br /> | None supported<br /> | 
| Minimum supported server<br /> | Windows Server 2012<br /> | 
| IDL<br /> | <dl><dt>Sbtsv.idl</dt></dl> | 
| IID<br /> | IID_ITsSbTarget is defined as:<ul><li>16616ECC-272D-411D-B324-126893033856</li><li>e85e10ea-db0b-4752-b456-5fd5840901c0 on Windows Server 2008 R2</li></ul> | 




## See also

<dl> <dt>

[**ITsSbTargetEx**](itssbtargetex.md)
</dt> <dt>

[**ITsSbTarget**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtarget)
</dt> </dl>

 

 





