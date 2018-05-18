---
Description: 'The PROPSHEETUI\_GETICON\_INFO structure is used as an input parameter to an application''s PFNPROPSHEETUI-typed function, when the function is called with a reason value of PROPSHEETUI\_REASON\_GET\_ICON.'
ms.assetid: '23c06f1c-0c8f-4055-a997-1ff94c4a541e'
title: 'PROPSHEETUI\_GETICON\_INFO structure'
---

# PROPSHEETUI\_GETICON\_INFO structure

The PROPSHEETUI\_GETICON\_INFO structure is used as an input parameter to an application's [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed function, when the function is called with a reason value of PROPSHEETUI\_REASON\_GET\_ICON.

## Syntax


```C++
typedef struct _PROPSHEETUI_GETICON_INFO {
  WORD  cbSize;
  WORD  Flags;
  WORD  cxIcon;
  WORD  cyIcon;
  HICON hIcon;
} PROPSHEETUI_GETICON_INFO, *PPROPSHEETUI_GETICON_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

CPSUI-supplied size, in bytes, of the PROPSHEETUI\_GETICON\_INFO structure.

</dd> <dt>

**Flags**
</dt> <dd>

Reserved.

</dd> <dt>

**cxIcon**
</dt> <dd>

CPSUI-supplied icon width, in pixels.

</dd> <dt>

**cyIcon**
</dt> <dd>

CPSUI-supplied icon height, in pixels.

</dd> <dt>

**hIcon**
</dt> <dd>

Receives an application-supplied icon handle. If the icon is not loaded, the member must be set to zero.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PROPSHEETUI_GETICON_INFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




