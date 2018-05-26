---
Description: COM Port Database Support Routines
ms.assetid: 8da059ea-7d2d-4dbf-b020-6d8a4330d2e4
title: COM Port Database Support Routines
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COM Port Database Support Routines

## 

This section describes the following system-supplied routines that support the [COM port database](https://msdn.microsoft.com/library/windows/hardware/ff546481).

<dl>

[**ComDBClaimNextFreePort**](/windows/win32/msports/nf-msports-comdbclaimnextfreeport?branch=master)  
[**ComDBClaimPort**](/windows/win32/msports/nf-msports-comdbclaimport?branch=master)  
[**ComDBClose**](/windows/win32/msports/nf-msports-comdbclose?branch=master)  
[**ComDBGetCurrentPortUsage**](/windows/win32/msports/nf-msports-comdbgetcurrentportusage?branch=master)  
[**ComDBOpen**](/windows/win32/msports/nf-msports-comdbopen?branch=master)  
[**ComDBReleasePort**](/windows/win32/msports/nf-msports-comdbreleaseport?branch=master)  
[**ComDBResizeDatabase**](/windows/win32/msports/nf-msports-comdbresizedatabase?branch=master)  
</dl>

This section also describes the following routines:

-   [**SerialDisplayAdvancedSettings**](/windows/win32/msports/nf-msports-serialdisplayadvancedsettings?branch=master), which is a system-supplied routine for [installing an advanced properties page for a COM port](https://msdn.microsoft.com/library/windows/hardware/ff546508)

-   [**PPORT\_ADVANCED\_DIALOG**](pport-advanced-dialog.md)-typed routine, which supplies an optional vendor-supplied dialog box that is called by **SerialDisplayAdvancedSettings**

To call these routines from an installer, link the installer to *msports.lib*, which is included with the Microsoft Windows Driver Kit (WDK).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20COM%20Port%20Database%20Support%20Routines%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



