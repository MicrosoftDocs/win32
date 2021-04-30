---
description: If you choose to implement erasing in your application other than by using the InkOverlay object, you can do so by using one of the following two methods.
ms.assetid: c05c7dbf-c3e0-42a7-a97e-bb9d9764209d
title: Erasing by Using the Pen
ms.topic: article
ms.date: 05/31/2018
---

# Erasing by Using the Pen

If you choose to implement erasing in your application other than by using the [**InkOverlay**](inkoverlay-class.md) object, you can do so by using one of the following two methods.

## Using the Tip of the Pen

The tip of the tablet pen is generally used for handwriting and drawing; however, the tip can also be used to erase ink. To do so, the application must have an erase mode that users can employ. In this mode, use hit testing to determine which ink the cursor is moving over. You can set the erase mode to delete only the ink that the cursor passes over or whole strokes that intersect the path of the cursor, depending upon design or functional considerations.

For an example of how to use an erase mode to erase ink, see the [Ink Erasing Sample](ink-erasing-sample.md).

## Using the Top of the Pen

To implement erasing with the top of the tablet pen, your application must look for a change in the cursor. To look for the inverted cursor, listen for the [**CursorInRange**](inkoverlay-cursorinrange.md) event to determine when the cursor is within the context of your application. When the cursor is in range, look for the [**Inverted**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcursor-get_inverted) property on the [**Cursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object. If the **Inverted** property is **true**, perform hit testing to determine which ink the cursor is moving over. Erase either the ink or the strokes that intersect the path of the cursor, depending upon design or functional considerations.

For an example of how to use the top of the pen to erase ink, see the [Ink Erasing Sample](ink-erasing-sample.md).

### Determining if Erasing with the Top of the Pen Is Enabled

Users can use the top of the pen to erase ink in applications designed for Tablet PC, if their particular hardware allows for it. This functionality is accessed by a check box in the Pen buttons group box on the Pen Options tab of the Tablet and Pen Settings control panel dialog. To detect if the user has enabled erasing for the top of the pen, check the following registry subkey:

`HKEY_CURRENT_USER\SOFTWARE\Microsoft\WISP\PEN\SysEventParameters`

The `EraseEnable` entry of this subkey is of type **REG\_DWORD**. The value of this entry is 1 for enabled, or 0 for disabled. Other values are reserved for future use.

If your application allows the top of the pen to be used for erasing, you should check and cache the value of the EraseEnable entry when:

-   Your application launches.
-   Any time your application receives focus after losing focus.

Use this cached value to modify the behavior of your application appropriately.

The following C\# example defines a `GetEraseEnabled` method that checks the value of the `EraseEnable` entry of the `SysEventParameters` subkey. The `GetEraseEnabled` method returns **TRUE** if the value of the entry is 1; returns **FALSE** if the value of the entry is 0; or throws an [InvalidOperationException](/dotnet/api/system.invalidoperationexception) exception if the value of the entry is other than 1 or 0. The `GetEraseEnabled` method returns the expected value of **TRUE** if either the subkey or the entry is not present.


```C++
private bool GetEraseEnabled()
{
    // 0 is disabled, 1 is enabled. The default is enabled
    const int Enabled = 1;
    const int Disabled = 0;
    const int DefaultValue = Enabled;

    // Constants for the registry subkey and the entry
    const string Subkey =
                @"SOFTWARE\Microsoft\WISP\PEN\SysEventParameters";
    const string KeyEntry = "EraseEnable";

    // Open the registry subkey.
    Microsoft.Win32.RegistryKey regKey =
        Microsoft.Win32.Registry.CurrentUser.OpenSubKey(Subkey);

    // Retrieve the value of the EraseEnable subkey entry. If either
    // the subkey or the entry does not exist, use the default value.
    object keyValue = (null == regKey) ? DefaultValue :
        regKey.GetValue(KeyEntry,DefaultValue);

    switch((int)keyValue)
    {
        case Enabled:
            // Return true if erasing on pen inversion is enabled. 
            return true;
        case Disabled:
            // Return false if erasing on pen inversion is disabled. 
            return false;
        default:
            // Otherwise, throw an exception. Do not assume this is
            // a Boolean value. Enabled and Disabled are the values
            // defined for this entry at this time. Other values are
            // reserved for future use.
            throw new InvalidOperationException(
                "Unexpected registry subkey value.");
    }
}
```



 

 
