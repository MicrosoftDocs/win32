---
description: Shows how to use the VSS interfaces to create a VSS hardware provider.
ms.assetid: 4d3c3f3c-22d2-4246-afef-aee2a0bd52d6
title: VssSampleProvider Tool and Sample
ms.topic: article
ms.date: 05/31/2018
---

# VssSampleProvider Tool and Sample

Shows how to use the VSS [interfaces](volume-shadow-copy-api-interfaces.md) to create a VSS hardware provider.

> [!Note]  
> The VssSampleProvider tool and sample are included in the Microsoft Windows Software Development Kit (SDK). You can download the Windows SDK from [Windows Software Development Kit (SDK) for Windows 8](https://developer.microsoft.com/windows/downloads/windows-8-sdk).

 

In the Windows SDK installation, the VssSampleProvider tool can be found in `%Program Files(x86)%\Windows Kits\8.1\bin\x64` (for 64-bit Windows) and `%Program Files(x86)%\Windows Kits\8.1\bin\x86` (for 32-bit Windows).

> [!Note]  
> Hardware providers are only supported on Windows Server operating systems. On a Windows Client operating system, you can compile the VssSampleProvider sample, but you can't register it as a hardware provider.

 

The VssSampleProvider tool consists of the following files:

-   Virtualstorage.sys
-   Vstorcontrol.exe
-   Vssampleprovider.dll
-   Vstorinterface.dll

The VssSampleProvider sample includes the following installation and uninstallation scripts:

-   Install-sampleprovider.cmd
-   Uninstall-sampleprovider.cmd
-   Register\_app.vbs

**To install and use the VssSampleProvider sample**

1.  Navigate to the `Program Files (x86)\Windows Kits\8.0\bin\` directory. This directory contains virtualstoragevss.sys and vstorcontrol.exe.
2.  Open a command prompt window in the specified directory.
3.  To install the virtual storage driver, in the command prompt window, type the following command:

    ```cmd
    vstorcontrol.exe install
    ```

    

4.  To install the VSS sample provider, in the command prompt window, type the following command:

    ```cmd
    install-sampleprovider.cmd
    ```

    

5.  To create a virtual LUN, do the following.

    1.  In the command prompt window, type the following command:

        ```cmd
        vstorcontrol.exe create fixeddisk -
        newimage C:\disk1.image -size 20M -storid "VSS Sample HW Provider"
        ```

        

        This command creates a virtual LUN whose storage identifier is **VSS Sample HW Provider**. To create additional virtual LUNs, repeat this step.

        The VSS sample provider recognizes a LUN only if **VSS Sample HW Provider** is a part of the storage identifier. For more information about the storage identifier, see the following blog post.

        [LUN - Resync with Diskshadow and Virtual Storage](https://blogs.msdn.microsoft.com/b/himanshu_kale/archive/2009/06/02/lun-resync-with-diskshadow-virtual-storage.aspx)

    2.  In the command prompt window, use diskpart.exe to format the virtual disk and assign a drive letter to it.

        Here is a sample script to run at the diskpart command prompt.

        ```cmd
        Select disk 
        Create partition primary size=<size>
        Format FS=NTFS quick
        Assign Letter=<letter>
        Exit
        ```

        

6.  To run the sample provider, in the command prompt window, type the following command:

    ```cmd
    Run vshadow.exe -p -nw <drive>
    ```

    

    *&lt;drive&gt;* represents the drive letter of the virtual LUN.

7.  To uninstall the VSS sample provider, in the command prompt window, type the following command:

    ```cmd
    uninstall-sampleprovider.cmd
    ```

    

8.  To uninstall the virtual storage driver, in the command prompt window, type the following command:

    ```cmd
    vstorcontrol.exe uninstall
    ```

    

 

 



