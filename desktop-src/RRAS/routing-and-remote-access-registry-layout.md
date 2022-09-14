---
title: Routing and Remote Access Registry Layout
description: The following syntax shows an example registry layout for the router service.
ms.assetid: 5464c2f7-6bb8-4838-939d-d58508715505
keywords:
- Routing and Remote Access Service RRAS , Routing and Remote Access Registry Layout
ms.topic: article
ms.date: 05/31/2018
---

# Routing and Remote Access Registry Layout

The following syntax shows an example registry layout for the router service.

``` syntax
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\RasMan 
    \PPP
        \ControlProtocols
            \Builtin
                Path: REG_EXPAND_SZ: %SystemRoot%\System32\rasppp.dll
            \Chap
                Path: REG_EXPAND_SZ: %SystemRoot%\System32\raschap.dll
        \EAP 
            \<typeID> 
                ConfigCLSID: REG_SZ: <guid> 
                ConfigUiPath: REG_EXPAND_SZ: %SystemRoot%\System32\rastls.dll 
                FriendlyName: REG_SZ: Public Key Based Authentication (EAP-TLS) 
                IdentityUIPath: REG_EXPAND_SZ: %SystemRoot%\System32\rastls.dll 
                InvokePasswordDialog: REG_DWORD: 0 
                InvokeUsernameDialog: REG_DWORD: 0 
                Path: REG_EXPAND_SZ: %SystemRoot%\System32\rastls.dll 
            \<typeID> 
                FriendlyName: REG_SZ: MD5 CHAP 
                InvokePasswordDialog: REG_DWORD: 0x1 
                InvokeUsernameDialog: REG_DWORD: 0x1 
                Path: REG_EXPAND_SZ: %SystemRoot%\System32\raschap.dll 
                StandaloneSupported: REG_DWORD: 0 
 
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\RemoteAccess 
    \Accounting 
        \Providers 
            ActiveProvider: REG_SZ: . . .             \<guid>
                ConfigCLSID: REG_SZ: <guid>
                DisplayName: REG_SZ: Radius Accounting
                Path: REG_EXPAND_SZ: %SystemRoot%\System32\rasrad.dll
                Vendor: REG_SZ: Microsoft
             . . . 
    \Authentication 
        \Providers 
            ActiveProvider: REG_SZ: . . .             \<guid>
                ConfigCLSID: REG_SZ: <guid>
                DisplayName: REG_SZ: Radius Authentication
                Path: REG_EXPAND_SZ: %SystemRoot%\System32\rasrad.dll
                Vendor: REG_SZ: Microsoft
            \<guid>
                ConfigCLSID: REG_SZ: <guid>
                DisplayName: REG_SZ: NT Authentication
                Path: REG_EXPAND_SZ: %SystemRoot%\System32\rasauth.dll
                Vendor: REG_SZ: Microsoft
             . . . 
    \DemandDialManager
        DLLPath: REG_EXPAND_SZ: . . . 
        < RAS parameters and DDM parameters > 
    \Interfaces
        \0
            Enabled: REG_DWORD: (0/1) 
            InterfaceName: REG_SZ: CorpHQ 
            Type: REG_DWORD: (Internal/Dedicated/Loopback) 
                \IP
                    InterfaceInfo: REG_BINARY: . . . 
                    ProtocolID: REG_DWORD: 0x0021 
                \IPX
                    InterfaceInfo: REG_BINARY: . . . 
                    ProtocolID: REG_DWORD: 0x002B
                . . . 
        \N
            InterfaceName: REG_SZ: IntelEtherExpressPro2 
            . . . 
    \Parameters 
        LANOnlyMode: REG_DWORD: (0/1) 
        ServerFlags: REG_DWORD: . . . 
        ServiceDLL: REG_EXPAND_SZ: %SystemRoot%\System32\mprdim.dll
    \RouterManagers 
        \IP 
            DLLPath: REG_SZ: . . . 
            GlobalInFilter: REG_BSZ: < filter set name > . . . 
            GlobalInfo: REG_BINARY: . . . 
            GlobalInterfaceInfo: REG_BINARY: . . . 
            ProtocolID: REG_DWORD: 0x0021 
            . . . 
            \IPX 
            DLLPath: REG_SZ: . . . 
            GlobalInFilter: REG_BSZ: < filter set name > . . . 
            GlobalInfo: REG_BINARY: . . . 
            GlobalInterfaceInfo: REG_BINARY: . . . 
            ProtocolID: REG_DWORD: 0x002B 
            . . . 
        . . .
 
HKEY_LOCAL_MACHINE\Software\Microsoft 
    \Router 
        \CurrentVersion 
            \RouterManagers 
                \IP 
                    \OSPF 
                        ConfigDll: REG_SZ: ipadmin.dll 
                        DllName: REG_SZ: ospf.dll 
                        ProtocolID: REG_DWORD: 0xD 
                        Title: REG_SZ: Open Shortest Path First 
                    \IPBOOTP
                        . . . 
                    \IPRIP
                        . . . 
                \IPX 
                    \IpxRip 
                        ConfigDll: REG_SZ: ipxadmin.dll 
                        DllName: REG_SZ: IPXRIP.DLL 
                        ProtocolID: REG_DWORD: 0x20000 
                        Title: REG_SZ: RIP for Ipx 
                    \IpxSap
                        . . . 
                    . . . 
            \UIConfigDlls 
                <guid1>: REG_SZ: ifadmin.dll 
                <guid2>: REG_SZ: ipadmin.dll 
                <guid3>: REG_SZ: ipxadmin.dll 
                <guid4>: REG_SZ: ddmadmin.dll
```

Every router manager installed in the system has a registry key created under the Router key. The DLLPath variable specifies the location of the DLL that corresponds to the router manager and the ProtocolID variable specifies the protocol family identifier for the router manager.

The Interfaces key is populated with the interfaces that have been added to the local system from the Router configuration. Each interface has an associated Type (Internal, Dedicated, or Dynamic) and subkeys for each router manager (IP and IPX, for example).

 

 




