---
title: DVC plug-in registration
description: Describes syntax for the dynamic virtual channel (DVC) plug-in entry for the Remote Desktop Connection (RDC) client.
ms.assetid: cda4f8c9-867a-41ac-894a-4296d5912b2b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# DVC plug-in registration

The dynamic virtual channel (DVC) plug-in is registered for use by the Remote Desktop Connection (RDC) client using one of the following methods:

-   Invoking the [**IMsTscAdvancedSettings::put\_PluginDlls**](imstscadvancedsettings-plugindlls.md) method of the Remote Desktop Protocol (RDP) ActiveX control. Multiple entries must be comma separated.
-   Writing the plug-in entry to the following location in the registry on the computer where the Remote Desktop Connection (RDC) client process is started:

    **HKEY\_CURRENT\_USER**\\**Software**\\**Microsoft**\\**Terminal Server Client**\\**Default**\\**AddIns**\\***unique plug-in name***

    > [!Note]  
    > You must create the *unique plug-in name* subkey if it does not exist. The *unique plug-in name* subkey name is an arbitrary string that can identify the plug-in. The string can be any combination of characters.

     

    Under *unique plug-in name*, you must add an entry that identifies the plug-in.

    Entry name = **Name**

    Data type = **REG\_SZ** or **REG\_EXPAND\_SZ**

In both cases, the entry value must conform to one of the following formats:

<dl> <dt>

<span id="Plug-inDLLName__CLSID_"></span><span id="plug-indllname__clsid_"></span><span id="PLUG-INDLLNAME__CLSID_"></span>"*Plug-inDLLName*:{*CLSID*}"
</dt> <dd>

The plug-in is not necessarily registered in the Windows registry as a Component Object Model (COM) object, but the DLL is implemented as an in-process COM object. The RDC client will load the DLL specified by *Plug-inDLLName* and retrieve the COM object directly using *CLSID*.

</dd> <dt>

<span id="Plug-inDLLName"></span><span id="plug-indllname"></span><span id="PLUG-INDLLNAME"></span>"*Plug-inDLLName*"
</dt> <dd>

The DLL implements the [**VirtualChannelGetInstance**](virtualchannelgetinstance.md) function and exports it by name. The RDC client will use the **VirtualChannelGetInstance** function to obtain [**IWTSPlugin**](/windows/desktop/api/TsVirtualChannels/nn-tsvirtualchannels-iwtsplugin) interface pointers for all of the plug-ins implemented by the DLL.

</dd> <dt>

<span id="_CLSID_"></span><span id="_clsid_"></span>"{*CLSID*}"
</dt> <dd>

The RDC client will instantiate the plug-in as a regular COM object using [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) with the *CLSID*.

</dd> </dl>

> [!Note]  
> *Plug-inDLLName* represents the full path and file name of the .dll file. If the data type is **REG\_EXPAND\_SZ**, the path can contain unexpanded environment variables that are expanded at runtime.

 

When the Remote Desktop Connection (RDC) client finishes its initialization, it will perform the following for every registered plug-in:

1.  Obtain an instance of the [**IWTSPlugin**](/windows/desktop/api/TsVirtualChannels/nn-tsvirtualchannels-iwtsplugin) interface for each plug-in using one of the methods described above.
2.  Call the [**Initialize**](/windows/desktop/api/TsVirtualChannels/nf-tsvirtualchannels-iwtsplugin-initialize) method of each [**IWTSPlugin**](/windows/desktop/api/TsVirtualChannels/nn-tsvirtualchannels-iwtsplugin) interface.
3.  If the client connects multiple times to the same or to a different server, there may be multiple calls to the [**Connected**](/windows/desktop/api/TsVirtualChannels/nf-tsvirtualchannels-iwtsplugin-connected) and [**Disconnected**](/windows/desktop/api/TsVirtualChannels/nf-tsvirtualchannels-iwtsplugin-disconnected) methods.
4.  The last call that the plug-in should handle is [**Terminated**](/windows/desktop/api/TsVirtualChannels/nf-tsvirtualchannels-iwtsplugin-terminated). It is a signal that the Remote Desktop Connection (RDC) client is about to unload the plug-in.

 

 