---
title: Detecting Whether the Remote Desktop Services Role Is Installed
description: C\ code example that shows a method that returns True if the Remote Desktop Services server role is installed and running or false otherwise, beginning with Windows Server 2008.
ms.assetid: 53ef8d43-2141-4df7-b9e6-baf0677924ba
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Detecting Whether the Remote Desktop Services Role Is Installed

You can use the [**Win32\_ServerFeature**](/windows/desktop/WmiSdk/win32-serverfeature) WMI class to detect whether the Remote Desktop Services server role is installed.

The following C# example shows a method that returns **True** if the Remote Desktop Services server role is installed and running or **false** otherwise. Because the [**Win32\_ServerFeature**](/windows/desktop/WmiSdk/win32-serverfeature) WMI class is only available beginning with Windows Server 2008, this code is not compatible with earlier versions of Windows.


```CSharp
static void Main(string[] args)
{
    // 14 is the identifier of the Remote Desktop Services role.
    HasServerFeatureById(14);
}

static bool HasServerFeatureById(UInt32 roleId)
{
    try
    {
        ManagementClass serviceClass = new ManagementClass("Win32_ServerFeature");
        foreach (ManagementObject feature in serviceClass.GetInstances())
        {
            if ((UInt32)feature["ID"] == roleId)
            {
                return true;
            }
        }

        return false;
    }
    catch (ManagementException)
    {
        // The most likely cause of this is that this is being called from an 
        // operating system that is not a server operating system.
    }

    return false;
}

```



 

 