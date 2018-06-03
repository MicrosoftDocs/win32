---
title: Querying Networking Objects
description: The following JScript sample retrieves and displays physical and virtual network information of the current system.
ms.assetid: 2021825e-ae4f-4816-9106-42b0536a22af
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying Networking Objects

The following JScript sample retrieves and displays physical and virtual network information of the current system.

The command-line syntax for this sample is: **CScript nvspinfo.js** \[**/p**\]\[**/m**\]\[**/e**\]\[**/z**\]\[**/?**\]


```JScript
/*
Copyright (c) Microsoft Corporation
 
Module Name:
 
    nvspinfo.js
 
*/


//
// VirtualSwitchManagementService object.  Logical wrapper class for Switch Management Service
//
function
VirtualSwitchManagementService( Server, User, Password )
 {
  //
  // Define instance fields.
  //    
  this.m_VirtualizationNamespace  = null;
    
  this.m_VirtualSwitchManagementService = null;
    
  VirtualSwitchManagementService.prototype.GetSingleObject = function( SWbemObjectSet )

  /*++

    Description:

        Takes a SWbemObjectSet which is expected to have one object and returns the object

    Arguments:

        SWbemObjectSet - The set.

    Return Value:

        The lone member of the set.  Exception thrown if Count does not equal 1.

  --*/

  {
   if (SWbemObjectSet.Count != 1)
    {
     throw(new Error(5, "SWbemObjectSet was expected to have one item but actually had " + SWbemObjectSet.Count)); 
    }
        
   return SWbemObjectSet.ItemIndex(0);
  }

    
  //
  // Constructor code
  //
    
  if (Server == null)
   {
    Server = WScript.CreateObject("WScript.Network").ComputerName; 
   }
    
  //
  // Set Namespace fields
  //
  try
   {
    var locator = new ActiveXObject("WbemScripting.SWbemLocator");

    this.m_VirtualizationNamespace = locator.ConnectServer(Server, "root\\virtualization", User, Password);
   }
  catch (e)
   {
    this.m_VirtualizationNamespace = null;
        
    throw(new Error("Unable to get an instance of Virtualization namespace: " + e.description));
   }
    
  //
  // Set Msvm_VirtualSwitchManagementService field
  //
  try
   {
    var physicalComputerSystem = 
          this.m_VirtualizationNamespace.Get( "Msvm_ComputerSystem.CreationClassName='Msvm_ComputerSystem',Name='" 
                                              + Server + "'");
          
    this.m_VirtualSwitchManagementService = 
      this.GetSingleObject( physicalComputerSystem.Associators_( "Msvm_HostedService",
                                                                 "Msvm_VirtualSwitchManagementService",
                                                                 "Dependent"));
   }
  catch (e)
   {
    this.m_VirtualSwitchManagementService = null;
        
    throw(new Error("Unable to get an instance of Msvm_VirtualSwitchManagementService: " + e.description));
   }
 }


//
// main
// 

var wshShell = WScript.CreateObject("WScript.Shell");

var g_NvspWmi   = null;
var g_CimV2     = null;


Main();

//
// Helper function for displaying Win32_NetworkAdapterConfiguration settings
//
function DisplayWin32NetworkAdapterConfiguration(win32NetworkAdapterConfiguration)
 {
  WScript.echo("    Win32_NetworkAdapterConfiguration. " + win32NetworkAdapterConfiguration.Index);
  WScript.echo("        SettingID = " + win32NetworkAdapterConfiguration.SettingID);
  WScript.echo("        InterfaceIndex = " + win32NetworkAdapterConfiguration.InterfaceIndex);
  WScript.echo("        IPEnabled = " + win32NetworkAdapterConfiguration.IPEnabled);

  if (win32NetworkAdapterConfiguration.IPEnabled)
   {
    if (win32NetworkAdapterConfiguration.IPAddress != null)
     {
      var ipAddresses = win32NetworkAdapterConfiguration.IPAddress.toArray();
      WScript.echo("        IP addresses:");
      for (k = 0; k < ipAddresses.length; k++)
       {
        WScript.echo("            " + ipAddresses[k]);
       }
     }
        
    if (win32NetworkAdapterConfiguration.IPSubnet != null)
     {
      var ipSubnet = win32NetworkAdapterConfiguration.IPSubnet.toArray();
      WScript.echo("        IP subnets:");
      for (k = 0; k < ipSubnet.length; k++)
       {  
        WScript.echo("            " + ipSubnet[k]);
       }
     }

    if (win32NetworkAdapterConfiguration.DefaultIPGateway != null)
     {
      var ipGateway = win32NetworkAdapterConfiguration.DefaultIPGateway.toArray();
      WScript.echo("        IP gateways:");
      for (k = 0; k < ipGateway.length; k++)
       {
        WScript.echo("            " + ipGateway[k]);
       }
     }
   }
 }

//
// Helper function for displaying Win32_NetworkAdapter settings
//
function DisplayWin32NetworkAdapter(win32NetworkAdapter)
 {
  var protocols = win32NetworkAdapter.Associators_( "Win32_ProtocolBinding", 
                                                    "Win32_NetworkProtocol", 
                                                    "Antecedent" );

  WScript.echo("    Win32_NetworkAdapter");
  WScript.echo("        Name = " + win32NetworkAdapter.Name);
  WScript.echo("        GUID = " + win32NetworkAdapter.GUID);
  WScript.echo("        DeviceID = " + win32NetworkAdapter.DeviceID);
  WScript.echo("        Index = " + win32NetworkAdapter.Index);
  WScript.echo("        ConfigManagerErrorCode = " + win32NetworkAdapter.ConfigManagerErrorCode);
  WScript.echo("        NetConnectionID = " + win32NetworkAdapter.NetConnectionID);
  WScript.echo("        NetConnectionStatus = " + win32NetworkAdapter.NetConnectionStatus);
  WScript.echo("        NetEnabled = " + win32NetworkAdapter.NetEnabled);
  WScript.echo("        MAC address = " + win32NetworkAdapter.MACAddress);
  WScript.echo("        Bindings:");

  for (k = 0; k < protocols.Count; k++)
   {
    var protocol = protocols.ItemIndex(k);
    WScript.echo("            " + protocol.Name);
   }
 }

//
// Helper function for displaying network settings
//
function DisplayNetworkSettings(DeviceID)
 {
  // get corresponding Win32_NetworkAdapterConfiguration
  var win32NetworkAdapterConfigurations = 
        g_CimV2.ExecQuery("SELECT * FROM Win32_NetworkAdapterConfiguration WHERE SettingID = '" + DeviceID + "'");

  if (win32NetworkAdapterConfigurations.Count)
   {
    var win32NetworkAdapterConfiguration = win32NetworkAdapterConfigurations.ItemIndex(0);
    DisplayWin32NetworkAdapterConfiguration(win32NetworkAdapterConfiguration);
   }
    
  // get corresponding Win32_NetworkAdapter
  var win32NetworkAdapters = g_CimV2.ExecQuery("SELECT * FROM Win32_NetworkAdapter WHERE GUID = '" + DeviceID + "'");

  if (win32NetworkAdapters.Count)
   {
    var win32NetworkAdapter = win32NetworkAdapters.ItemIndex(0);
    DisplayWin32NetworkAdapter(win32NetworkAdapter);
   }        
 }

//
// Helper function which takes a connection string and displays the switch and port
//
function DumpConnectionInformation(connection)
 {
  var connected = false;
    
  if (connection != null &amp;&amp; connection != "")
   {
    var switchPort = null;
        
    try
     {
      switchPort = GetObject("winmgmts:" + connection);
     }
    catch (e)
     {
      switchPort = null;
     }
        
    if (switchPort != null)
     {
      var switches = g_NvspWmi.m_VirtualizationNamespace.ExecQuery( "SELECT * FROM Msvm_VirtualSwitch WHERE Name = '" 
                                                                  + switchPort.SystemName + "'");

      if (switches.Count)
       {
        WScript.echo("    connection:");
        WScript.echo("        switch = " + switches.ItemIndex(0).ElementName);
        WScript.echo("        port = " + switchPort.Name);
        connected = true;
       }
     }

    if (!connected)
     {
      WScript.echo("    invalid connection: "+ connection);
     }
   }
  else
   {
    WScript.echo("    not connected");
   }
 }

function Main()
 {
  var enumAdapters = false;
  var everything = false;
  var analyze = false;
  var includePorts = false;
  var includeMac = false;
    
  if (WScript.arguments.Named.Exists("?"))
   {
    WScript.Echo("");
    WScript.Echo("    /p    include port details");
    WScript.Echo("    /m    include mac details (implies -p)");
    WScript.Echo("    /e    everything");
    WScript.Echo("    /z    analyze (implies /e)");
    WScript.Echo("");
    WScript.Quit();
   }
        
  if (WScript.arguments.Named.Exists("p"))
   {
    includePorts = true;
   }
    
  if (WScript.arguments.Named.Exists("a"))
   {
    enumAdapters = true;
   }

  if (WScript.arguments.Named.Exists("m"))
   {
    includePorts = true;
    includeMac = true;
   }

  if (WScript.arguments.Named.Exists("e"))
   {
    everything = true;
   }
    
  if (WScript.arguments.Named.Exists("z"))
   {
    analyze = true;
    everything = true;
   }

  if (everything)
   {
    enumAdapters = true;
    includePorts = true;
    includeMac = true;
   }

  //
  // Connect to root\cimv2 namespace and verify Hyper-V network drivers and services are running
  //
  WScript.Echo("Looking for root\\cimv2...");
  var locator = new ActiveXObject("WbemScripting.SWbemLocator");
  g_CimV2 = locator.ConnectServer("", "root\\cimv2", "", "");

  WScript.Echo("");
  WScript.Echo("Looking for VSP drivers...");
  var list = g_CimV2.ExecQuery("SELECT * FROM Win32_SystemDriver WHERE Name='VMSMP' OR Name='vmbus' OR Name='storvsp'");
  for (i = 0; i < list.Count; i++)
   {
    var next = list.ItemIndex(i);
    WScript.echo("Driver " + next.Name + ": State = " + next.State + ", Status = " + next.Status);
   }

  WScript.Echo("");
  WScript.Echo("Looking for VSP services...");
  var list = g_CimV2.ExecQuery("SELECT * FROM Win32_Service WHERE Name='nvspwmi' OR Name='vmms' OR Name='vhdsvc'");
  for (i = 0; i < list.Count; i++)
   {
    var next = list.ItemIndex(i);
    WScript.echo("Service " + next.Name + ": State = " + next.State + ", Status = " + next.Status);
   }

  //
  // Enumerate all the adapters in the system
  //
  if (enumAdapters)
   {
    WScript.Echo("");
    WScript.Echo("Looking for Win32_NetworkAdapterConfiguration...");
    var list = g_CimV2.ExecQuery("SELECT * FROM Win32_NetworkAdapterConfiguration");
    for (i = 0; i < list.Count; i++)
     {
      var next = list.ItemIndex(i);
      DisplayWin32NetworkAdapterConfiguration(next);
      WScript.Echo("");
     }
        
    WScript.Echo("");
    WScript.Echo("Looking for Win32_NetworkAdapterConfiguration...");
    var list = g_CimV2.ExecQuery("SELECT * FROM Win32_NetworkAdapter");
    for (i = 0; i < list.Count; i++)
     {
      var next = list.ItemIndex(i);
      DisplayWin32NetworkAdapter(next);
      WScript.Echo("");
     }
   }
    
  //
  // The nvspwmi service exposes the Hyper-V WMI objects
  //
  WScript.Echo("Looking for nvspwmi...");
  g_NvspWmi   = new VirtualSwitchManagementService();

  //
  // "Internal" NICs are virtual NICs exposed to the root partition and provide the root
  // connectivity to the virtual network.
  //
  WScript.Echo("");
  WScript.Echo("Looking for internal (host) virtual nics...");
  var list = g_NvspWmi.m_VirtualizationNamespace.ExecQuery("SELECT * FROM Msvm_InternalEthernetPort");
  for (i = 0; i < list.Count; i++)
   {
    var next = list.ItemIndex(i);
    WScript.echo(next.DeviceID);
    WScript.echo("    " + next.ElementName);
    WScript.echo("    MTU = " + next.MaxDataSize);

    DisplayNetworkSettings(next.DeviceID);

    WScript.Echo("");
   }
    
  //
  // "External" NICs are NICs (typically physical) used by a virtual network.
  //
  // "IsBound=TRUE" indicates the NIC is currently bound to the switch protocol and is already used by a
  // virtual network.
  //
  WScript.Echo("");
  WScript.Echo("Looking for bound external nics...");
  list = g_NvspWmi.m_VirtualizationNamespace.ExecQuery("SELECT * FROM Msvm_ExternalEthernetPort WHERE IsBound=TRUE");
  for (i = 0; i < list.Count; i++)
   {
    var next = list.ItemIndex(i);
    WScript.echo(next.DeviceID);
    WScript.echo("    " + next.ElementName);

    DisplayNetworkSettings(next.DeviceID);

    WScript.Echo("");
   }

  //
  // "IsBound=FALSE" indicates the NIC is not currently bound to the switch protocol.
  //
  WScript.Echo("");
  WScript.Echo("Looking for unbound external nics...");
  list = g_NvspWmi.m_VirtualizationNamespace.ExecQuery("SELECT * FROM Msvm_ExternalEthernetPort WHERE IsBound=FALSE");
  for (i = 0; i < list.Count; i++)
   {
    var next = list.ItemIndex(i);
    WScript.echo(next.DeviceID);
    WScript.echo("    " + next.ElementName);
    WScript.echo("    MTU = " + next.MaxDataSize);

    DisplayNetworkSettings(next.DeviceID);

    WScript.Echo("");
   }

  //
  // "Synthetic" NICs are enlightened virtual NICs within VMs
  //
  WScript.Echo("");
  WScript.Echo("Looking for synthetic nics...");
  list = g_NvspWmi.m_VirtualizationNamespace.ExecQuery("SELECT * FROM Msvm_SyntheticEthernetPortSettingData");
  for (i = 0; i < list.Count; i++)
   {
    var next = list.ItemIndex(i);

    if (next.Address == null)
     {
      continue;
     }
       
    var syntheticEthernetPorts = next.Associators_( "Msvm_ElementSettingData", "Msvm_SyntheticEthernetPort", "ManagedElement");

    WScript.echo(next.ElementName + ":");

    if (next.Connection != null)
     {
      var connection = next.Connection.toArray();
      for (k = 0; k < connection.length; k++)
       {
        DumpConnectionInformation(connection[k]);
       }
     }
        
    WScript.Echo("    MAC address = " + next.Address);
        
    if (syntheticEthernetPorts.Count)
     {
      syntheticEthernetPort = syntheticEthernetPorts.ItemIndex(0);
      WScript.echo("    DeviceID = " + syntheticEthernetPort.DeviceID);
      WScript.echo("    MTU = " + syntheticEthernetPort.MaxDataSize);
     }
    else
     {
      WScript.echo("    not powered on");
     }
        
    WScript.Echo("");
   }

  //
  // "Emulated" NICs are emulated legacy virtual NICs within VMs
  //
  WScript.Echo("");
  WScript.Echo("Looking for emulated nics...");
  list = g_NvspWmi.m_VirtualizationNamespace.ExecQuery("SELECT * FROM Msvm_EmulatedEthernetPortSettingData");
  for (i = 0; i < list.Count; i++)
   {
    var next = list.ItemIndex(i);

    if (next.Address == null)
     {
      continue;
     }

    var emulatedEthernetPorts = next.Associators_( "Msvm_ElementSettingData", "Msvm_EmulatedEthernetPort", "ManagedElement");

    WScript.echo(next.ElementName + ":");
        
    if (next.Connection != null)
     {
      var connection = next.Connection.toArray();
      for (k = 0; k < connection.length; k++)
       {
        DumpConnectionInformation(connection[k]);
       }
     }
        
    WScript.Echo("    MAC address = " + next.Address);
        
    if (emulatedEthernetPorts.Count)
     {
      emulatedEthernetPort = emulatedEthernetPorts.ItemIndex(0);
      WScript.echo("    DeviceID = " + emulatedEthernetPort.DeviceID);
      WScript.echo("    MTU = " + emulatedEthernetPort.MaxDataSize);
     }
    else
     {
      WScript.echo("    not powered on");
     }
        
    WScript.Echo("");
   }

  //
  // Enumerate all the switches (virtual networks) in the system
  //
  WScript.Echo("");
  WScript.Echo("Looking for switches...");
  var switches = g_NvspWmi.m_VirtualizationNamespace.ExecQuery("SELECT * FROM Msvm_VirtualSwitch");
  for (i = 0; i < switches.Count; i++)
   {
    var isExternalConnected = false;    // indicates if an external NIC is connected
    var isInternalConnected = false;    // indicates if an internal NIC is connected
        
    var nextSwitch = switches.ItemIndex(i);
    WScript.echo(nextSwitch.Name);
    WScript.echo("    " + nextSwitch.ElementName);
    WScript.echo("    MaxChimneyOffloads = " + nextSwitch.MaxChimneyOffloads);
    WScript.echo("    MaxVMQOffloads = " + nextSwitch.MaxVMQOffloads);
     
    WScript.echo("    Ports:");

    var ports = g_NvspWmi.m_VirtualizationNamespace.ExecQuery( "SELECT * FROM Msvm_SwitchPort WHERE SystemName= '" 
                                                             + nextSwitch.Name + "'");
    for (j = 0; j < ports.Count; j++)
     {
      var port = ports.ItemIndex(j);
      var isConnected = false;

      if (includePorts)
       {
        if (j > 0)
         {
          WScript.Echo("");
         }

        WScript.echo("        " + port.Name);
        WScript.echo("        AllowMacSpoofing     = " + port.AllowMacSpoofing);
        WScript.echo("        ChimneyOffloadWeight = " + port.ChimneyOffloadWeight);
        WScript.echo("        ChimneyOffloadUsage  = " + port.ChimneyOffloadUsage);
        WScript.echo("        VMQOffloadWeight     = " + port.VMQOffloadWeight);
        WScript.echo("        VMQOffloadUsage      = " + port.VMQOffloadUsage);
       }

      // switch Msvm_SwitchLANEndpoints are for internal and external NICs
      var switchLanEndpoints = port.Associators_( "Msvm_ActiveConnection", "Msvm_SwitchLANEndpoint", "Dependent");
            
      // VM Msvm_LANEndpoints are for virtual machine (synthetic and emulated) NICs
      var vmLanEndpoints = port.Associators_( "Msvm_ActiveConnection", "Msvm_VmLANEndpoint", "Dependent");

      // Msvm_VLANEndpoint hold VLAN data for a switch port
      var vlanEndpoints = port.Associators_( "Msvm_BindsTo", "Msvm_VLANEndpoint", "Dependent");

      // if interested in port details, find VLAN settings
      if (includePorts &amp;&amp; vlanEndpoints.Count)
       {
        var vlanEndpoint = vlanEndpoints.ItemIndex(0);
        var mode = vlanEndpoint.OperationalEndpointMode;

        // the VLAN ID and trunk array are stored in Msvm_VLANEndpointSettingData
        var vLANEndpointSettingData = vlanEndpoint.Associators_( "Msvm_NetworkElementSettingData", 
                                                                 "Msvm_VLANEndpointSettingData", 
                                                                 "SettingData");
                
        var accessVlanId = 0;   // only applicable in access mode
        var nativeVlanId = 0;   // only applicable in trunk mode

        if (vLANEndpointSettingData.Count)
         {
          accessVlanId = vLANEndpointSettingData.ItemIndex(0).AccessVLAN;
          nativeVlanId = vLANEndpointSettingData.ItemIndex(0).NativeVLAN;
         }

        // 2 = access mode, 5 = trunk mode
        if (mode == 2)
         {
          WScript.echo("        VLAN Mode            = ACCESS " + accessVlanId);
         }
        else if (mode == 5)
         {
          // build up a string for the trunk list
          var trunkList = vLANEndpointSettingData.ItemIndex(0).TrunkedVLANList.toArray();
          var txtTrunkList = "";

          for (k = 0; k < trunkList.length; k++)
           {
            if (k != 0)
             {
              txtTrunkList = txtTrunkList + ",";
             }
            txtTrunkList = txtTrunkList + trunkList[k];
           }
                    
          WScript.echo("        VLAN Mode            = TRUNK, NativeVLAN=" + nativeVlanId + ", TrunkArray=" + txtTrunkList);
         }
        else
         {
          WScript.echo("        VLAN Mode            = ", mode);
         }
       }
            
      if (switchLanEndpoints.Count)
       {
        var switchLanEndpoint = switchLanEndpoints.ItemIndex(0);

        var internals = switchLanEndpoint.Associators_( "Msvm_GlobalEthernetPortSAPImplementation", 
                                                        "Msvm_InternalEthernetPort", 
                                                        "Antecedent");

        if (internals.Count)
         {
          // the connected port of type "Internal"
          WScript.echo("        Internal NIC: " + internals.ItemIndex(0).Name);
          WScript.echo("            " + internals.ItemIndex(0).ElementName);
          isInternalConnected = true;
          isConnected = true;
         }
                    
        var externals = switchLanEndpoint.Associators_( "Msvm_GlobalEthernetPortSAPImplementation",
                                                        "Msvm_ExternalEthernetPort",
                                                        "Antecedent");
                
        if (externals.Count)
         {
          // the connected port of type "External"
          WScript.echo("        External NIC: " + externals.ItemIndex(0).Name);
          WScript.echo("            " + externals.ItemIndex(0).ElementName);
          isExternalConnected = true;
          isConnected = true;
         }
       }
            
      if (vmLanEndpoints.Count)
       {
        var vmLanEndpoint = vmLanEndpoints.ItemIndex(0);

        var synthetic = vmLanEndpoint.Associators_( "Msvm_DeviceSAPImplementation", "Msvm_SyntheticEthernetPort", "Antecedent");
                
        if (synthetic.Count)
         {
          // get name of VM
          var vmName = synthetic.ItemIndex(0).SystemName;
                    
          var vm = g_NvspWmi.m_VirtualizationNamespace.ExecQuery( "SELECT * FROM Msvm_ComputerSystem WHERE Name= '" 
                                                                + synthetic.ItemIndex(0).SystemName + "'");
                    
          if (vm.Count)
           {
            vmName = vm.ItemIndex(0).ElementName;
           }
                    
          // the connected port is of type "Synthetic"
          WScript.echo("        VM NIC:       " + synthetic.ItemIndex(0).ElementName);
          WScript.echo("            VM = " + vmName);
          WScript.echo("            DeviceID = " + synthetic.ItemIndex(0).DeviceID);
          isConnected = true;

          // get the operational status
          var operationalStatuses = vmLanEndpoint.OperationalStatus.toArray();
          for (k = 0; k < operationalStatuses.length; k++)
           {
            WScript.Echo("            OperationalStatus = " + operationalStatuses[k]);
           }
                    
          // get the corresponding Msvm_SyntheticEthernetPortSettingData
          var syntheticEthernetPortSettingData = synthetic.ItemIndex(0).Associators_( "Msvm_ElementSettingData",
                                                                                      "Msvm_SyntheticEthernetPortSettingData",
                                                                                      "SettingData");
          if (syntheticEthernetPortSettingData.Count)
           {
            WScript.Echo("            MAC address = " + syntheticEthernetPortSettingData.ItemIndex(0).Address);

            WScript.Echo("            VirtualSystemIdentifiers = ");
            var vsids = syntheticEthernetPortSettingData.ItemIndex(0).VirtualSystemIdentifiers.toArray();

            for (k = 0; k < vsids.length; k++)
             {
              WScript.Echo("                " + vsids[k]);
             }
           }
         }

        var emulated = vmLanEndpoint.Associators_( "Msvm_DeviceSAPImplementation", "Msvm_EmulatedEthernetPort", "Antecedent");
                
        if (emulated.Count)
         {
          // get name of VM
          var vmName = emulated.ItemIndex(0).SystemName;
                    
          var vm = g_NvspWmi.m_VirtualizationNamespace.ExecQuery( "SELECT * FROM Msvm_ComputerSystem WHERE Name= '" 
                                                                + emulated.ItemIndex(0).SystemName + "'");
                    
          if (vm.Count)
           {
            vmName = vm.ItemIndex(0).ElementName;
           }
                    
          // the connected port is of type "Emulated" (legacy)
          WScript.echo("        Legacy NIC:   " + emulated.ItemIndex(0).ElementName);
          WScript.echo("            VM = " + vmName);
          WScript.echo("            DeviceID = " + emulated.ItemIndex(0).DeviceID);
          isConnected = true;
                    
          // get the corresponding Msvm_EmulatedEthernetPortSettingData
          var emulatedEthernetPortSettingData = emulated.ItemIndex(0).Associators_( "Msvm_ElementSettingData", 
                                                                                    "Msvm_EmulatedEthernetPortSettingData", 
                                                                                    "SettingData");
          if (emulatedEthernetPortSettingData.Count)
           {
            WScript.Echo("            MAC address = " + emulatedEthernetPortSettingData.ItemIndex(0).Address);
           }
         }
       }

      if (includeMac)
       {
        var macs = port.Associators_( "Msvm_SwitchPortDynamicForwarding", "Msvm_DynamicForwardingEntry", "Dependent");
                
        for (k = 0; k < macs.Count; k++)
         {
          var mac = macs.ItemIndex(k);
          var str = mac.MACAddress;
          if (str.length != 12)
           {
            WScript.echo("                " + str);
           }
          else
           {
            WScript.echo( "                " + str.charAt(0)  + str.charAt(1)  + "-" + str.charAt(2)  + str.charAt(3)  + "-" +
                          str.charAt(4)  + str.charAt(5)  + "-" + str.charAt(6)  + str.charAt(7)  + "-" + str.charAt(8)  + 
                          str.charAt(9)  + "-" + str.charAt(10) + str.charAt(11) + "  VLAN:" + mac.VlanId );
           }
         }
       }
            
      if (!includePorts &amp;&amp; isConnected &amp;&amp; j < (ports.Count-1))
       {
        WScript.Echo("");
       }
            
     }

    if (isExternalConnected)
     {
      if (isInternalConnected)
       {
        WScript.echo("    Switch is of type 'External' with a root virtual NIC");
       }
      else
       {
        WScript.echo("    Switch is of type 'External' without a root virtual NIC");
       }
     }    
    else
     {
      if (isInternalConnected)
       {
        WScript.echo("    Switch is of type 'Internal'");
       }
      else
       {
        WScript.echo("    Switch is of type 'Private'");
       }
     } 
    WScript.Echo("");
   }
    
  WScript.Echo("");
  WScript.Echo("Finished!");
 }
```



## Related topics

<dl> <dt>

[**Msvm\_ActiveConnection**](msvm-activeconnection.md)
</dt> <dt>

[**Msvm\_BindsTo**](msvm-bindsto.md)
</dt> <dt>

[**Msvm\_ComputerSystem**](msvm-computersystem.md)
</dt> <dt>

[**Msvm\_DeviceSAPImplementation**](msvm-devicesapimplementation.md)
</dt> <dt>

[**Msvm\_DynamicForwardingEntry**](msvm-dynamicforwardingentry.md)
</dt> <dt>

[**Msvm\_ElementSettingData**](msvm-elementsettingdata.md)
</dt> <dt>

[**Msvm\_EmulatedEthernetPort**](msvm-emulatedethernetport.md)
</dt> <dt>

[**Msvm\_EmulatedEthernetPortSettingData**](msvm-emulatedethernetportsettingdata.md)
</dt> <dt>

[**Msvm\_ExternalEthernetPort**](msvm-externalethernetport.md)
</dt> <dt>

[**Msvm\_GlobalEthernetPortSAPImplementation**](msvm-globalethernetportsapimplementation.md)
</dt> <dt>

[**Msvm\_HostedService**](msvm-hostedservice.md)
</dt> <dt>

[**Msvm\_InternalEthernetPort**](msvm-internalethernetport.md)
</dt> <dt>

[**Msvm\_NetworkElementSettingData**](msvm-networkelementsettingdata.md)
</dt> <dt>

[**Msvm\_SwitchLANEndpoint**](msvm-switchlanendpoint.md)
</dt> <dt>

[**Msvm\_SwitchPort**](msvm-switchport.md)
</dt> <dt>

[**Msvm\_SwitchPortDynamicForwarding**](msvm-switchportdynamicforwarding.md)
</dt> <dt>

[**Msvm\_SyntheticEthernetPort**](msvm-syntheticethernetport.md)
</dt> <dt>

[**Msvm\_SyntheticEthernetPortSettingData**](msvm-syntheticethernetportsettingdata.md)
</dt> <dt>

[**Msvm\_VirtualSwitch**](msvm-virtualswitch.md)
</dt> <dt>

[**Msvm\_VirtualSwitchManagementService**](msvm-virtualswitchmanagementservice.md)
</dt> <dt>

[**Msvm\_VLANEndpoint**](msvm-vlanendpoint.md)
</dt> <dt>

[**Msvm\_VLANEndpointSettingData**](msvm-vlanendpointsettingdata.md)
</dt> <dt>

[**Msvm\_VmLANEndpoint**](msvm-vmlanendpoint.md)
</dt> </dl>

 

 




