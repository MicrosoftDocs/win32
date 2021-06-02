---
description: Prevents edge gesture behaviors when an application window is active and in full-screen mode (or an owned window is active).
ms.assetid: F4242C05-181B-44FC-BE6C-8ABB76079981
title: System.EdgeGesture.DisableTouchWhenFullscreen
ms.topic: article
ms.date: 05/31/2018
---

# System.EdgeGesture.DisableTouchWhenFullscreen

Prevents edge gesture behaviors when an application window is active and in full-screen mode (or an owned window is active).

> [!Note]  
> In full-screen mode, the size of the application window matches the screen resolution.

 

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.EdgeGesture.DisableTouchWhenFullscreen
   shellPKey = PKEY_EdgeGesture_DisableTouchWhenFullscreen
   formatID = 32CE38B2-2C9A-41B1-9BC5-B3784394AA44
   propID = 2
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
```

## Remarks

In Windows 8, user interactions with the edges of the screen display system UI such as app bars, charms, and running apps.

For full-screen, remote applications, this UI behavior on the local machine might override and interfere with the UI of the remote session. This property enables an application to disable the edge UI on the local machine.

To disable edge UI, set this property to VARIANT\_TRUE. The default value is VARIANT\_FALSE.

This property has no effect on Windows Store apps.

The following example shows how to set edge UI behaviors.


```
HRESULT SetTouchDisableProperty(HWND hwnd, BOOL fDisableTouch)
{
    IPropertyStore* pPropStore;
    HRESULT hrReturnValue = SHGetPropertyStoreForWindow(hwnd, IID_PPV_ARGS(&pPropStore));
    if (SUCCEEDED(hrReturnValue))
    {
        PROPVARIANT var;
        var.vt = VT_BOOL;
        var.boolVal = fDisableTouch ? VARIANT_TRUE : VARIANT_FALSE;
        hrReturnValue = pPropStore->SetValue(PKEY_EdgeGesture_DisableTouchWhenFullscreen, var);
        pPropStore->Release();
    }
    return hrReturnValue;
}
```



## Related topics

<dl> <dt>

[propertyDescription](./propdesc-schema-propertydescription.md)
</dt> <dt>

[searchInfo](./propdesc-schema-searchinfo.md)
</dt> <dt>

[typeInfo](./propdesc-schema-typeinfo.md)
</dt> </dl>

 

 
