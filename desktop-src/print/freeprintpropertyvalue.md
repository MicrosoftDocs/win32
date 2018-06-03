---
Description: Frees the value that is retrieved using GetJobNamedPropertyValue function.
ms.assetid: 38B760D9-CB6E-45AD-A83F-3C26D1B31A30
title: FreePrintPropertyValue function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FreePrintPropertyValue function

Frees the value that is retrieved using [**GetJobNamedPropertyValue**](getjobnamedpropertyvalue.md) function.

## Syntax


```C++
DWORD WINAPI FreePrintPropertyValue(
  _Inout_ PrintPropertyValue *pValue
);
```



## Parameters

<dl> <dt>

*pValue* \[in, out\]
</dt> <dd>

Pointer to **PrintPropertyValue** structure that is returned from [**GetJobNamedPropertyValue**](getjobnamedpropertyvalue.md).

</dd> </dl>

## Return value

If the operation succeeds, the function returns **ERROR\_SUCCESS**.

## Requirements



|                            |                                                                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                         |
| Header<br/>          | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>WinSpool.lib</dt> </dl>                                                                    |
| DLL<br/>             | <dl> <dt>Spoolss.dll; </dt> <dt>WinSpool.drv</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20FreePrintPropertyValue%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




