---
title: IConfigAsfWriter2 GetParam method
description: The GetParam method retrieves the current value of the specified filter configuration parameter.
ms.assetid: 81d915a1-6190-46e3-a5cb-7f5fc242b8dd
keywords:
- GetParam method windows Media Format
- GetParam method windows Media Format , IConfigAsfWriter2 interface
- IConfigAsfWriter2 interface windows Media Format , GetParam method
topic_type:
- apiref
api_name:
- IConfigAsfWriter2.GetParam
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IConfigAsfWriter2::GetParam method

The **GetParam** method retrieves the current value of the specified filter configuration parameter.

## Syntax


```C++
HRESULT GetParam(
  [in]  DWORD dwParam,
  [out] DWORD *pdwParam1,
  [out] DWORD *pdwParam2
);
```



## Parameters

<dl> <dt>

*dwParam* \[in\]
</dt> <dd>

Specifies the parameter to retrieve. It must be a value defined in the [\_AM\_ASFWRITERCONFIG\_PARAM](/windows/desktop/api/Dshowasf/) enumeration.

</dd> <dt>

*pdwParam1* \[out\]
</dt> <dd>

Pointer to a variable that retrieves the value of the parameter specified in *dwParam*.

</dd> <dt>

*pdwParam2* \[out\]
</dt> <dd>

Not used, must be zero.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## See also

<dl> <dt>

[**IConfigAsfWriter2 Interface**](/windows/desktop/api/dshowasf/)
</dt> <dt>

[**IConfigAsfWriter2::SetParam**](iconfigasfwriter2-setparam.md)
</dt> </dl>

 

 




