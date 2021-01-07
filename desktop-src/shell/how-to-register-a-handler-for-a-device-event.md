---
description: Describes the processes for implementing device event handlers in the registry.
ms.assetid: 84B12B5C-C179-4124-A1FC-B90D120336BF
title: How to Register a Handler for a Device Event
ms.topic: article
ms.date: 05/31/2018
---

# How to Register a Handler for a Device Event

Handlers define the software portion of AutoPlay. They define the software's icon and friendly name, as well as the Component Object Model (COM) component to instantiate and how to initialize the component in response to an event. Each handler for a specific event registers as a value under the appropriate **EventHandler** key. When that event is detected, the user is prompted to choose a handler from a list of all the handlers registered for that event.

## Instructions


Handlers and their associated values are defined under the **AutoplayHandlers**\\**Handlers** key. Subkeys differ depending on whether the system can read device contents directly or whether the device provides contents to the system through a proprietary interface.

The following example shows the subkeys and values that are used for a device, such as a digital video camera or .mp3 player, that provides its contents to the system through a proprietary interface. The example handler is called **MyHandler**.

```
HKEY_LOCAL_MACHINE or HKEY_CURRENT_USER
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AutoplayHandlers
                     Handlers
                        MyHandler
                           Action [REG_SZ] = Play music
                           CLSID [REG_SZ] = {a51f2ed3-634e-4a97-9d55-efcf08e7b32f}
                           DefaultIcon [REG_EXPAND_SZ] = %ProgramFiles%\Windows Media Player\wmplayer.exe,0
                           InitCmdLine [REG_SZ] = /Play
                           ProgID [REG_SZ] = WMP.PlayMusicFiles
                           Provider [REG_SZ] = Windows Media Player
```

> [!Note]  
> While the example shows both a ProgID and a class identifier (CLSID) value, in practice these values are mutually exclusive so that only one or the other is present. The ProgID value is preferred. Whichever is used, it should point to a COM component that implements the [**IHWEventHandler**](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler) interface.

 

You can enter the Action value as a literal value, for example "Play music" as shown in this example, or as a file name with a resource string. You can also enter the Provider value as a literal value or as a file name with a resource string. AutoPlay combines the Action value and the Provider value with the word "using" to create a friendly caption that displays in the UI. In the example, the resulting caption is "Play music using Windows Media Player."

The DefaultIcon value points to either an .ico file or a resource in a binary file. If the numeric value that follows the binary file name is zero or greater, then it is the index value of the icon in that binary file. If it is a negative value, then it is the icon resource ID. Negative index values are recommended. No value is necessary in the case of an .ico file. It is recommended that you use environment variables in the path.

The InitCmdLine value passes unaltered through the [**IHWEventHandler::Initialize**](/windows/desktop/api/Shobjidl/nf-shobjidl-ihweventhandler-initialize) method before any other methods are called.

The following example shows the subkeys and values that are used for a device that can be read directly, such as a CD-ROM drive or other removable disk. Again, the example handler is called **MyHandler**.

```
HKEY_LOCAL_MACHINE or HKEY_CURRENT_USER
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AutoplayHandlers
                     Handlers
                        MyHandler
                           Action [REG_SZ] = @%systemroot%\System32\wiaacmgr.exe,-276
                           DefaultIcon [REG_EXPAND_SZ] = %systemroot%\System32\wiaacmgr.exe,-2
                           InvokeProgID [REG_SZ] = WIA.AutoPlayDropHandler
                           InvokeVerb [REG_SZ] = open
                           Provider [REG_SZ] = @%systemroot%\System32\wiaacmgr.exe,-101
```

In this example, the Action and Provider values are shown as a file name with a resource string rather than literal values, but the strings that they reference are used in the same manner. They are combined with the word "using" to form a friendly caption as explained earlier.

InvokeProgID and InvokeVerb values replace CLSID, InitCmdLine, and ProgID. The InvokeProgID and InvokeVerb values match key names that are found under **HKEY\_CLASSES\_ROOT**, as shown in the following registry entry. This set of example keys corresponds to the specific Handler example described earlier.

```
HKEY_CLASSES_ROOT
   WIA.AutoplayDropHandler
      shell
         open
            DropTarget
               Clsid = {F1ABE2B5-C073-4dba-B6EB-FD7A5111DD8F}
```

The [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function uses the CLSID to implement the appropriate application.

After you define the handler in either of these two ways, you need to register it for a specific event. You do this by providing the handler name as a value for that event's key under **EventHandlers**. The following example shows how to register **MyHandler** as a handler for the GenericVolumeArrival event. It has no assigned data value.

```
HKEY_LOCAL_MACHINE or HKEY_CURRENT_USER
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AutoplayHandlers
                     EventHandlers
                        GenericVolumeArrival
                           MyHandler [REG_SZ]
```

## Related topics

<dl> <dt>

[**IHWEventHandler**](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler)
</dt> <dt>

[**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance)
</dt> </dl>

 

 
