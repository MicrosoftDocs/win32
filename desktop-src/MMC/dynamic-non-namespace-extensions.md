---
title: Dynamic Non-Namespace Extensions
description: This feature is introduced in MMC 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6087bd8a-08bf-4430-be9e-258262c60900'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["dynamic non-namespace extensions MMC"]
---

# Dynamic Non-Namespace Extensions

This feature is introduced in MMC 1.1.

Using the [**CCF\_MMC\_DYNAMIC\_EXTENSIONS**](ccf-mmc-dynamic-extensions.md) clipboard format, a snap-in can also add any of the following types of extensions to its own scope or result items:

-   Context menus
-   Toolbars
-   Property sheets
-   Taskpads

For these types of extensions, add the clipboard format CCF\_MMC\_DYNAMIC\_EXTENSIONS to the snap-in's [**IDataObject**](_ole_idataobject) implementation for the items you want to extend. The CCF\_MMC\_DYNAMIC\_EXTENSIONS format uses the [**SMMCDynamicExtensions**](smmcdynamicextensions.md) structure. This structure specifies the extension snap-ins you want to extend the item represented by the **IDataObject** object.

Be aware that the MMC registry entries for the primary snap-in and the extension snap-in must be set correctly. For details on setting MMC registry entries for namespace extensions, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).

The following Steps describe how to implement dynamic extensions for non-namespace extensions:

**To implement dynamic extensions for non-namespace extensions**

1.  Add the CCF\_MMC\_DYNAMIC\_EXTENSIONS clipboard format to the snap-in's [**IDataObject**](_ole_idataobject) implementation.

    Usually, [**IDataObject**](_ole_idataobject) has its supported clipboard formats as static members. If so, add the CCF\_MMC\_DYNAMIC\_EXTENSIONS format as a member:

    ```C++
    static UINT s_cfDynamicExtensions;
    ```

    

    Register the CCF\_MMC\_DYNAMIC\_EXTENSIONS format and assign the registered format to the static member in the **IDataObject** implementation's constructor:

    ```C++
    s_cfDynamicExtensions = RegisterClipboardFormat (W2T(CCF_MMC_DYNAMIC_EXTENSIONS));
    ```

    

2.  Handle the CCF\_MMC\_DYNAMIC\_EXTENSIONS format in the [**IDataObject::GetData**](_ole_idataobject_getdata) method.

    The following example handles the CCF\_MMC\_DYNAMIC\_EXTENSIONS format and returns an [**SMMCDynamicExtensions**](smmcdynamicextensions.md) structure that contains an array of two GUIDs that are the CLSIDs of the two extension snap-ins (CLSID\_Snapin1 and CLSID\_Snapin2) that will extend the item:

    ```C++
        if (cf == s_cfDynamicExtensions)
        {
          UINT cGuids = 2;
          UINT size = sizeof(SMMCDynamicExtensions) + 
                      (cGuids-1) * sizeof(GUID);
     
          lpMedium->hGlobal = ::GlobalAlloc(GPTR, size);
     
          if (!lpMedium->hGlobal)
              return E_OUTOFMEMORY;
     
          SMMCDynamicExtensions* pdata = 
                     reinterpret_cast<SMMCDynamicExtensions*>
                     (lpMedium->hGlobal);
          pdata->count = cGuids;
          int i=0;
          pdata->guid[i++] = CLSID_Snapin1;
          pdata->guid[i++] = CLSID_Snapin2;
          return S_OK;
        }
    ```

    

Just before MMC must use an extensible feature (that is, just before creating and that displays a context menu, property sheet, toolbar, or taskpad), MMC calls [**IDataObject::GetData**](_ole_idataobject_getdata) on the data object for the selected item and asks for dynamic extensions to add through the CCF\_MMC\_DYNAMIC\_EXTENSIONS clipboard format. Based on the CLSIDs passed in the [**SMMCDynamicExtensions**](smmcdynamicextensions.md) structure, MMC attempts to add the specified extensions to the extensible feature. If an extension is unavailable or unregistered, MMC skips that extension and continues to the next CLSID passed in the structure.

## Related topics

<dl> <dt>

[Adding Dynamic Extensions: Interfaces](adding-dynamic-extensions-interfaces.md)
</dt> <dt>

[Dynamic Namespace Extensions](dynamic-namespace-extensions.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> <dt>

[MMC Registry Entries](mmc-registry-entries.md)
</dt> </dl>

 

 




