---
Description: Helper Interfaces for Plug-Ins
ms.assetid: 889d00f8-3147-449b-9fbb-a879bc6b3d11
title: Helper Interfaces for Plug-Ins
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Helper Interfaces for Plug-Ins

The **IPrintCoreHelper** interface provides a basic set of functionality that is available to all four core driver modules: Unidrv rendering plug-ins, Unidrv UI plug-ins, Pscript5 rendering plug-ins, and Pscript5 UI plug-ins.

The **IPrintCoreHelper** interface is the base interface from which the **IPrintCoreHelperPS** and **IPrintCoreHelperUni** interfaces inherit. Developers of Pscript5 plug-ins should implement the **IPrintCoreHelperPS** interface. Developers of Unidrv plug-ins should implement the **IPrintCoreHelperUni** interface.

<dl>

[IPrintCoreHelper Interface](iprintcorehelper-interface.md)  
[IPrintCoreHelperPS Interface](iprintcorehelperps-interface.md)  
[IPrintCoreHelperUni Interface](iprintcorehelperuni-interface.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Helper%20Interfaces%20for%20Plug-Ins%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



