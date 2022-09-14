---
title: IConfigAsfWriter2 SetParam method
description: The SetParam method sets the value of the specified filter configuration parameter.
ms.assetid: b8067fb2-c379-4b26-b4f7-c790604e3edc
keywords:
- SetParam method windows Media Format
- SetParam method windows Media Format , IConfigAsfWriter2 interface
- IConfigAsfWriter2 interface windows Media Format , SetParam method
topic_type:
- apiref
api_name:
- IConfigAsfWriter2.SetParam
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter2::SetParam method

The **SetParam** method sets the value of the specified filter configuration parameter.

## Syntax


```C++
HRESULT SetParam(
  [in] DWORD dwParam,
  [in] DWORD dwParam1,
  [in] DWORD dwParam2
);
```



## Parameters

<dl> <dt>

*dwParam* \[in\]
</dt> <dd>

Specifies the parameter to set. It must be a value defined in the [\_AM\_ASFWRITERCONFIG\_PARAM](/previous-versions/windows/desktop/legacy/dd758054(v=vs.85)) enumeration.

</dd> <dt>

*dwParam1* \[in\]
</dt> <dd>

Specifies the value to assign to the *dwParam* parameter.

</dd> <dt>

*dwParam2* \[in\]
</dt> <dd>

Not used; must be 0.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## See also

<dl> <dt>

[**IConfigAsfWriter2 Interface**](/previous-versions/windows/desktop/legacy/dd743206(v=vs.85))
</dt> <dt>

[**IConfigAsfWriter2::GetParam**](iconfigasfwriter2-getparam.md)
</dt> </dl>

 

 