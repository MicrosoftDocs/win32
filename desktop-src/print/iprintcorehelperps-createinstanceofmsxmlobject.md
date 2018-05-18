---
Description: 'The IPrintCoreHelperPS::CreateInstanceOfMSXMLObject method creates an instance of an MSXML object.'
ms.assetid: '017f6e00-694b-4ada-86be-cf2be047fa88'
title: 'IPrintCoreHelperPS::CreateInstanceOfMSXMLObject method'
---

# IPrintCoreHelperPS::CreateInstanceOfMSXMLObject method

The **IPrintCoreHelperPS::CreateInstanceOfMSXMLObject** method creates an instance of an MSXML object.

## Syntax


```C++
STDMETHOD CreateInstanceOfMSXMLObject(
  [in]  REFCLSID  rclsid,
  [in]  LPUNKNOWN pUnkOuter,
  [in]  DWORD     dwClsContext,
  [in]  REFIID    riid,
  [out] LPVOID    ppv
);
```



## Parameters

<dl> <dt>

*rclsid* \[in\]
</dt> <dd>

The CLSID that is associated with the data and code that will be used to create the object.

</dd> <dt>

*pUnkOuter* \[in\]
</dt> <dd>

A pointer to the aggregate object's **IUnknown** interface (the controlling **IUnknown**). This parameter must be **NULL**, which means that the object is not being created as part of an aggregate.

</dd> <dt>

*dwClsContext* \[in\]
</dt> <dd>

The context in which the code that manages the newly created object will run. The only valid values are **NULL** and CLSCTX\_INPROC\_SERVER, which is a value of the CLSCTX enumeration (described in the Microsoft Windows SDK documentation).

</dd> <dt>

*riid* \[in\]
</dt> <dd>

A reference to the identifier of the interface that will be used to communicate with the object.

</dd> <dt>

*ppv* \[out\]
</dt> <dd>

A pointer to a memory address that receives the address of the interface that is requested in the *riid* parameter. If **IPrintCoreHelperPS::CreateInstanceOfMSXMLObject** successfully returns, \**ppv* contains the address of the requested interface. If this method fails, \**ppv* contains **NULL**.

</dd> </dl>

## Return value

**IPrintCoreHelperPS::CreateInstanceOfMSXMLObject** should return one of the following values.



| Return code                                                                                            | Description                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | An instance of the specified object class was successfully created.<br/>                                                                                                                                                                                   |
| <dl> <dt>**CLASS\_E\_NOAGGREGATION**</dt> </dl> | The specified class cannot be created as part of an aggregate.<br/>                                                                                                                                                                                        |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl>          | The specified class does not implement the requested interface, or the controlling **IUnknown** interface does not expose the requested interface.<br/>                                                                                                    |
| <dl> <dt>**REGDB\_E\_CLASSNOTREG**</dt> </dl>   | A specified class is not registered in the registration database. This value can also indicate that the type of server you requested in the CLSCTX enumeration type is not registered or the values for the server types in the registry are corrupt.<br/> |



 

## Remarks

The plug-in should not directly create an MSXML object by calling CoCreateInstance (described in the Windows SDK documentation). Instead, it should call Pscript to do so. The reason is that under certain conditions in which the printer driver might be used, such as with older operating system versions, the operating system does not need to register the required version of MSXML, which currently is version 6. In such situations, calling CoCreateInstance can fail. However, the core driver ensures that wherever the driver is present, the MSXML parser DLL is also present on the machine, making it possible to create an MSXML object when needed.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperPS::CreateInstanceOfMSXMLObject%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




