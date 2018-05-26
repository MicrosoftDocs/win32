---
Description: Gets the reason why the printer extension was activated.
ms.assetid: 404E9893-97BA-48A7-87CE-0B4AF46692CE
title: IPrinterExtensionEventArgsReasonId property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrinterExtensionEventArgs::ReasonId property

Gets the reason why the printer extension was activated.

This property is read-only.

## Syntax


```C++
HRESULT get_ReasonId(
  [out, retval] GUID *pReasonId
);
```



## Property value

The reason why the printer extension was activated.

## Error codes

Returns an **HRESULT** value. If the property call was not successful, it returns the appropriate **HRESULT** error code.

## Remarks

-   In this mode, preferences for a print job or default print preferences is expected to be displayed.

    Guid = {EC8F261F-267C-469F-B5D6-3933023C29CC}

    **PRINTER\_EXTENSION\_REASON\_PRINT\_PREFERENCES** = { 0xec8f261f, 0x267c, 0x469f, 0xb5, 0xd6, 0x39, 0x33, 0x2, 0x3c, 0x29, 0xcc };

-   In this mode a status monitor for the print queue is expected to be displayed

    Guid = {23BB1328-63DE-4293-915B-A6A23D929ACB}

    **PRINTER\_EXTENSION\_REASON\_DRIVER\_EVENT** = { 0x23bb1328, 0x63de, 0x4293, 0x91, 0x5b, 0xa6, 0xa2, 0x3d, 0x92, 0x9a, 0xcb };

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**DetailedReasonId**](iprinterextensioneventargs-detailedreasonid.md)
</dt> <dt>

[**IPrinterExtensionEventArgs**](iprinterextensioneventargs.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterExtensionEventArgs::ReasonId%20property%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





