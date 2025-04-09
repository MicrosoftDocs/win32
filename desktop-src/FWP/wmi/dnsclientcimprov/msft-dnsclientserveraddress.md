---
description: Represents an interface to a DNS server that includes address information about the remote connection to the server.
ms.assetid: 6a62d066-faf5-4a36-b6cd-04b9864f3fa4
title: MSFT\_DNSClientServerAddress class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_DNSClientServerAddress
- MSFT_DNSClientServerAddress.RequestStateChange
- MSFT_DNSClientServerAddress.InstanceId
- MSFT_DNSClientServerAddress.Caption
- MSFT_DNSClientServerAddress.ElementName
- MSFT_DNSClientServerAddress.InstallDate
- MSFT_DNSClientServerAddress.OperationalStatus
- MSFT_DNSClientServerAddress.StatusDescriptions
- MSFT_DNSClientServerAddress.Status
- MSFT_DNSClientServerAddress.HealthState
- MSFT_DNSClientServerAddress.CommunicationStatus
- MSFT_DNSClientServerAddress.DetailedStatus
- MSFT_DNSClientServerAddress.OperatingStatus
- MSFT_DNSClientServerAddress.PrimaryStatus
- MSFT_DNSClientServerAddress.EnabledState
- MSFT_DNSClientServerAddress.OtherEnabledState
- MSFT_DNSClientServerAddress.RequestedState
- MSFT_DNSClientServerAddress.EnabledDefault
- MSFT_DNSClientServerAddress.TimeOfLastStateChange
- MSFT_DNSClientServerAddress.TransitioningToState
- MSFT_DNSClientServerAddress.Name
- MSFT_DNSClientServerAddress.SystemCreationClassName
- MSFT_DNSClientServerAddress.SystemName
- MSFT_DNSClientServerAddress.CreationClassName
- MSFT_DNSClientServerAddress.AccessInfo
- MSFT_DNSClientServerAddress.InfoFormat
- MSFT_DNSClientServerAddress.OtherInfoFormatDescription
- MSFT_DNSClientServerAddress.AccessContext
- MSFT_DNSClientServerAddress.OtherAccessContext
- MSFT_DNSClientServerAddress.InterfaceIndex
- MSFT_DNSClientServerAddress.InterfaceAlias
- MSFT_DNSClientServerAddress.ServerAddresses
- MSFT_DNSClientServerAddress.AddressFamily
api_type: 
- DllExport
api_location: 
- DnsClientCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_DNSClientServerAddress class

Represents an interface to a DNS server that includes address information about the remote connection to the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_DNSClientServerAddress : CIM_RemoteServiceAccessPoint
{
  string   InstanceId;
  string   Caption;
  string   ElementName;
  datetime InstallDate;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus[];
  uint16   PrimaryStatus;
  uint16   EnabledState;
  string   OtherEnabledState;
  uint16   RequestedState;
  uint16   EnabledDefault;
  datetime TimeOfLastStateChange;
  uint16   TransitioningToState;
  string   Name;
  string   SystemCreationClassName;
  string   SystemName[];
  string   CreationClassName;
  string   AccessInfo;
  uint16   InfoFormat;
  string   OtherInfoFormatDescription;
  uint16   AccessContext;
  string   OtherAccessContext;
  uint32   InterfaceIndex;
  string   InterfaceAlias;
  string   ServerAddresses[];
  uint16   AddressFamily;
};
```

## Members

The **MSFT\_DNSClientServerAddress** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DNSClientServerAddress** class has these methods.



| Method                 | Description                                                                    |
|:-----------------------|:-------------------------------------------------------------------------------|
| **RequestStateChange** | Initiates a requests to change the state of a DNS server interface.<br/> |



 

### Properties

The **MSFT\_DNSClientServerAddress** class has these properties.

<dl> <dt>

**AccessContext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_RemoteServiceAccessPoint.OtherAccessContext)
</dt> </dl>

Gets a description of the role that the server plays in the local system.

This property is inherited from **CIM\_RemoteServiceAccessPoint**.

This property contains one of the following values. The default value is "0" (unknown).



| Value                                                                                | Meaning                                       |
|--------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>0</dt> </dl>         | Unknown<br/>                            |
| <dl> <dt>1</dt> </dl>         | Other<br/>                              |
| <dl> <dt>2</dt> </dl>         | Default Gateway<br/>                    |
| <dl> <dt>3</dt> </dl>         | DNS Server<br/>                         |
| <dl> <dt>4</dt> </dl>         | SNMP Trap Destination<br/>              |
| <dl> <dt>5</dt> </dl>         | MPLS Tunnel Destination<br/>            |
| <dl> <dt>6</dt> </dl>         | DHCP Server<br/>                        |
| <dl> <dt>7</dt> </dl>         | SMTP Server<br/>                        |
| <dl> <dt>8</dt> </dl>         | LDAP Server<br/>                        |
| <dl> <dt>9</dt> </dl>         | Network Time Protocol (NTP) Server<br/> |
| <dl> <dt>10</dt> </dl>        | Management Service<br/>                 |
| <dl> <dt>207 32767</dt> </dl> | DMTF Reserved<br/>                      |
| <dl> <dt>32768 ...</dt> </dl> | Vendor Reserved<br/>                    |



 

</dd> <dt>

**AccessInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_RemoteServiceAccessPoint.InfoFormat)
</dt> </dl>

Gets the access and addressing information for the remote connection.

This property is inherited from **CIM\_RemoteServiceAccessPoint**.

</dd> <dt>

**AddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the address family of the server address.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64), [**Dynamic**](/windows/win32/wmisdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the short description of the server.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates the ability of the server interface to communicate with the underlying [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)) object.

This property is inherited from **CIM\_ManagedSystemElement**.

This property contains one of the following values:



| Value                                                                                   | Meaning                       |
|-----------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>0</dt> </dl>            | Unknown<br/>            |
| <dl> <dt>1</dt> </dl>            | Not Available<br/>      |
| <dl> <dt>2</dt> </dl>            | Communication OK<br/>   |
| <dl> <dt>3</dt> </dl>            | Lost Communication<br/> |
| <dl> <dt>4</dt> </dl>            | No Contact<br/>         |
| <dl> <dt>5 32767</dt> </dl>      | DMTF Reserved<br/>      |
| <dl> <dt>32768 65535 </dt> </dl> | Vendor Reserved<br/>    |



 

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (256)
</dt> </dl>

Gets the name of the class that was used to create this **MSFT\_DNSClientServerAddress** object. You can use this to create unique identifiers for class instances.

This property is inherited from **CIM\_ServiceAccessPoint**.

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets information about the status of the server, in addition to the information provided by the **PrimaryStatus** property.

This property is inherited from **CIM\_ManagedSystemElement**.

This property contains one of the following values:



| Value                                                                                   | Meaning                               |
|-----------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>0</dt> </dl>            | Not Available<br/>              |
| <dl> <dt>1</dt> </dl>            | No Additional Information<br/>  |
| <dl> <dt>2</dt> </dl>            | Stressed<br/>                   |
| <dl> <dt>3</dt> </dl>            | Predictive Failure<br/>         |
| <dl> <dt>4</dt> </dl>            | Non-Recoverable Error<br/>      |
| <dl> <dt>5</dt> </dl>            | Supporting Entity in Error<br/> |
| <dl> <dt>5 32767</dt> </dl>      | DMTF Reserved<br/>              |
| <dl> <dt>32768 65535 </dt> </dl> | Vendor Reserved<br/>            |



 

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly name of the server.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Indicates the default startup configuration for the **EnabledState** property.

Default value: "2" (enabled). This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

This property contains one of the following values:



| Value                                                                                  | Meaning                        |
|----------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>2</dt> </dl>           | Enabled<br/>             |
| <dl> <dt>3</dt> </dl>           | Disabled<br/>            |
| <dl> <dt>5</dt> </dl>           | Not Applicable<br/>      |
| <dl> <dt>6</dt> </dl>           | Enabled but Offline<br/> |
| <dl> <dt>7</dt> </dl>           | No Default<br/>          |
| <dl> <dt>8</dt> </dl>           | Quiesce<br/>             |
| <dl> <dt>9 32767</dt> </dl>     | DMTF Reserved<br/>       |
| <dl> <dt>32768 65535</dt> </dl> | Vendor Reserved<br/>     |



 

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) (CIM\_EnabledLogicalElement.OtherEnabledState)
</dt> </dl>

Indicates whether the server is enabled, or in a related state.

This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

This property contains one of the following values. The default value is "5" (not applicable).



| Value                                                                                  | Meaning                        |
|----------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>0</dt> </dl>           | Unknown<br/>             |
| <dl> <dt>1</dt> </dl>           | Other<br/>               |
| <dl> <dt>2</dt> </dl>           | Enabled<br/>             |
| <dl> <dt>3</dt> </dl>           | Disabled<br/>            |
| <dl> <dt>4</dt> </dl>           | Shutting Down<br/>       |
| <dl> <dt>5</dt> </dl>           | Not Applicable<br/>      |
| <dl> <dt>6</dt> </dl>           | Enabled but Offline<br/> |
| <dl> <dt>7</dt> </dl>           | In Test<br/>             |
| <dl> <dt>8</dt> </dl>           | Deferred<br/>            |
| <dl> <dt>9</dt> </dl>           | Quiesce<br/>             |
| <dl> <dt>10</dt> </dl>          | Starting<br/>            |
| <dl> <dt>11 32767</dt> </dl>    | DMTF Reserved<br/>       |
| <dl> <dt>32768 65535</dt> </dl> | Vendor Reserved<br/>     |



 

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](/windows/win32/wmisdk/standard-qualifiers)
</dt> </dl>

Indicates the current health of the server.

This property is inherited from **CIM\_ManagedSystemElement**.

This property contains one of the following values:



| Value                                                                                   | Meaning                          |
|-----------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>0</dt> </dl>            | Unknown<br/>               |
| <dl> <dt>5</dt> </dl>            | OK<br/>                    |
| <dl> <dt>10</dt> </dl>           | Degraded/Warning<br/>      |
| <dl> <dt>15</dt> </dl>           | Minor failure<br/>         |
| <dl> <dt>20</dt> </dl>           | Major failure<br/>         |
| <dl> <dt>25</dt> </dl>           | Critical failure<br/>      |
| <dl> <dt>30</dt> </dl>           | Non-recoverable error<br/> |
| <dl> <dt>31 32767</dt> </dl>     | DMTF Reserved<br/>         |
| <dl> <dt>32768 65535 </dt> </dl> | Vendor Specific<br/>       |



 

</dd> <dt>

**InfoFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_RemoteServiceAccessPoint.OtherInfoFormatDescription)
</dt> </dl>

Gets an integer that identifies a description of the **AccessInfo** property value.

This property is inherited from **CIM\_RemoteServiceAccessPoint**.



| Value                                                                                | Meaning                             |
|--------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>1</dt> </dl>         | Other<br/>                    |
| <dl> <dt>2</dt> </dl>         | Host Name<br/>                |
| <dl> <dt>3</dt> </dl>         | IPv4 Address<br/>             |
| <dl> <dt>4</dt> </dl>         | IPv6 Address<br/>             |
| <dl> <dt>5</dt> </dl>         | IPX Address<br/>              |
| <dl> <dt>6</dt> </dl>         | DECnet Address<br/>           |
| <dl> <dt>7</dt> </dl>         | SNA Address<br/>              |
| <dl> <dt>8</dt> </dl>         | Autonomous System Number<br/> |
| <dl> <dt>9</dt> </dl>         | MPLS Label<br/>               |
| <dl> <dt>10</dt> </dl>        | IPv4 Subnet Address<br/>      |
| <dl> <dt>11</dt> </dl>        | IPv6 Subnet Address<br/>      |
| <dl> <dt>12</dt> </dl>        | IPv4 Address Range<br/>       |
| <dl> <dt>13</dt> </dl>        | IPv6 Address Range<br/>       |
| <dl> <dt>100</dt> </dl>       | Dial String<br/>              |
| <dl> <dt>101</dt> </dl>       | Ethernet Address<br/>         |
| <dl> <dt>102</dt> </dl>       | Token Ring Address<br/>       |
| <dl> <dt>103</dt> </dl>       | ATM Address<br/>              |
| <dl> <dt>104</dt> </dl>       | Frame Relay Address<br/>      |
| <dl> <dt>200</dt> </dl>       | URL<br/>                      |
| <dl> <dt>201</dt> </dl>       | FQDN<br/>                     |
| <dl> <dt>202</dt> </dl>       | User FQDN<br/>                |
| <dl> <dt>203</dt> </dl>       | DER ASN1 DN<br/>              |
| <dl> <dt>204</dt> </dl>       | DER ASN1 GN<br/>              |
| <dl> <dt>205</dt> </dl>       | Key ID<br/>                   |
| <dl> <dt>206</dt> </dl>       | Parameterized URL<br/>        |
| <dl> <dt>207 32767</dt> </dl> | DMTF Reserved<br/>            |
| <dl> <dt>32768 ...</dt> </dl> | Vendor Reserved<br/>          |



 

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/win32/wmisdk/standard-wmi-qualifiers) (MIF.DMTF\|ComponentID\|001.5)
</dt> </dl>

Gets the **datetime** value that indicates when this object was created.

This property is inherited from **CIM\_ManagedSystemElement**.

</dd> <dt>

**InstanceId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique identifier of this object. The ID must be unique within the scope of the instantiating namespace.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly name of the server interface.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly index of the server interface.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **key**, **MaxLen** (256), **Override** (Name)
</dt> </dl>

Gets the unique ID of this object.

This property is inherited from **CIM\_ServiceAccessPoint**.

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-wmi-qualifiers) (CIM\_EnabledLogicalElement.EnabledState)
</dt> </dl>

Gets an array that contains information about the operating status of the server, in addition to the information provided by the **EnabledState** property.

This property is inherited from **CIM\_ManagedSystemElement**.

This property can contain the following values:



| Value                                                                                | Meaning                    |
|--------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl>         | Unknown<br/>         |
| <dl> <dt>1</dt> </dl>         | Not Available<br/>   |
| <dl> <dt>2</dt> </dl>         | Servicing<br/>       |
| <dl> <dt>3</dt> </dl>         | Starting<br/>        |
| <dl> <dt>4</dt> </dl>         | Stopping<br/>        |
| <dl> <dt>5</dt> </dl>         | Stopped<br/>         |
| <dl> <dt>6</dt> </dl>         | Aborted<br/>         |
| <dl> <dt>7</dt> </dl>         | Dormant<br/>         |
| <dl> <dt>8</dt> </dl>         | Completed<br/>       |
| <dl> <dt>9</dt> </dl>         | Migrating<br/>       |
| <dl> <dt>10</dt> </dl>        | Emigrating<br/>      |
| <dl> <dt>11</dt> </dl>        | Immigrating<br/>     |
| <dl> <dt>12</dt> </dl>        | Snapshotting<br/>    |
| <dl> <dt>13</dt> </dl>        | Shutting Down<br/>   |
| <dl> <dt>14</dt> </dl>        | In Test<br/>         |
| <dl> <dt>15</dt> </dl>        | Transitioning<br/>   |
| <dl> <dt>16</dt> </dl>        | In Service<br/>      |
| <dl> <dt>17 32767</dt> </dl>  | DMTF Reserved<br/>   |
| <dl> <dt>32768 ...</dt> </dl> | Vendor Reserved<br/> |



 

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/win32/wmisdk/standard-wmi-qualifiers) (Indexed), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-wmi-qualifiers) (CIM\_ManagedSystemElement.StatusDescriptions)
</dt> </dl>

Gets an array that contains the status of the server.

This property is inherited from **CIM\_ManagedSystemElement**.

This property can contain the following values:



| Value                                                                         | Meaning                               |
|-------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>0</dt> </dl>  | Unknown<br/>                    |
| <dl> <dt>1</dt> </dl>  | Other<br/>                      |
| <dl> <dt>2</dt> </dl>  | OK<br/>                         |
| <dl> <dt>3</dt> </dl>  | Degraded<br/>                   |
| <dl> <dt>4</dt> </dl>  | Stressed<br/>                   |
| <dl> <dt>5</dt> </dl>  | Predictive Failure<br/>         |
| <dl> <dt>6</dt> </dl>  | Error<br/>                      |
| <dl> <dt>7</dt> </dl>  | Non-Recoverable Error<br/>      |
| <dl> <dt>8</dt> </dl>  | Starting<br/>                   |
| <dl> <dt>9</dt> </dl>  | Stopping<br/>                   |
| <dl> <dt>10</dt> </dl> | Stopped<br/>                    |
| <dl> <dt>11</dt> </dl> | In Service<br/>                 |
| <dl> <dt>12</dt> </dl> | No Contact<br/>                 |
| <dl> <dt>13</dt> </dl> | Lost Communication<br/>         |
| <dl> <dt>14</dt> </dl> | Aborted<br/>                    |
| <dl> <dt>15</dt> </dl> | Dormant<br/>                    |
| <dl> <dt>16</dt> </dl> | Supporting Entity in Error<br/> |
| <dl> <dt>17</dt> </dl> | Completed<br/>                  |
| <dl> <dt>18</dt> </dl> | Power Mode<br/>                 |
| <dl> <dt>19</dt> </dl> | DMTF Reserved<br/>              |
| <dl> <dt>20</dt> </dl> | Vendor Reserved<br/>            |



 

</dd> <dt>

**OtherAccessContext**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_RemoteServiceAccessPoint.AccessContext)
</dt> </dl>

Gets a description of the role of the server when the **AccessContext** property is set to "1" (other).

This property is inherited from **CIM\_RemoteServiceAccessPoint**.

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) (CIM\_EnabledLogicalElement.EnabledState)
</dt> </dl>

Gets a description of the value of the **EnabledState** property when it is set to "1" (other).

This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

</dd> <dt>

**OtherInfoFormatDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_RemoteServiceAccessPoint.InfoFormat)
</dt> </dl>

Gets a description to use when the **InfoFormat** property is set to "1" (other).

This property is inherited from **CIM\_RemoteServiceAccessPoint**.

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_ManagedSystemElement.DetailedStatus, CIM\_ManagedSystemElement.HealthState)
</dt> </dl>

Gets the high level status of the server.

This property is inherited from **CIM\_ManagedSystemElement**.

This property contains one of the following values:



| Value                                                                                   | Meaning                    |
|-----------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl>            | Unknown<br/>         |
| <dl> <dt>1</dt> </dl>            | OK<br/>              |
| <dl> <dt>2</dt> </dl>            | Degraded<br/>        |
| <dl> <dt>3</dt> </dl>            | Error<br/>           |
| <dl> <dt>4 32767</dt> </dl>      | DMTF Reserved<br/>   |
| <dl> <dt>32768 65535 </dt> </dl> | Vendor Reserved<br/> |



 

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the last requested state of the server. The actual state of the client is represented by the **EnabledState** property.

This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

This property contains one of the following values. The default value is "12" (not applicable).



| Value                                                                                  | Meaning                    |
|----------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl>           | Unknown<br/>         |
| <dl> <dt>2</dt> </dl>           | Enabled<br/>         |
| <dl> <dt>3</dt> </dl>           | Disabled<br/>        |
| <dl> <dt>4</dt> </dl>           | Shut Down<br/>       |
| <dl> <dt>5</dt> </dl>           | No Change<br/>       |
| <dl> <dt>6</dt> </dl>           | Offline<br/>         |
| <dl> <dt>7</dt> </dl>           | Test<br/>            |
| <dl> <dt>8</dt> </dl>           | Deferred<br/>        |
| <dl> <dt>9</dt> </dl>           | Quiesce<br/>         |
| <dl> <dt>10</dt> </dl>          | Reboot<br/>          |
| <dl> <dt>11</dt> </dl>          | Reset<br/>           |
| <dl> <dt>12</dt> </dl>          | Not Applicable<br/>  |
| <dl> <dt>13 32767</dt> </dl>    | DMTF Reserved<br/>   |
| <dl> <dt>32768 65535</dt> </dl> | Vendor Reserved<br/> |



 

</dd> <dt>

**ServerAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets an array that contains the IP addresses of the servers.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (10), [**Deprecated**](/windows/win32/wmisdk/standard-qualifiers) (CIM\_ManagedSystemElement.OperationalStatus)
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead, use **OperationalStatus**.

 

Gets the status of the server.

This property is inherited from **CIM\_ManagedSystemElement**.

This property contains one of the following values:



| Value                                                                                 | Meaning                                                                                    |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| <dl> <dt>OK</dt> </dl>         | The server is functioning without errors.<br/>                                       |
| <dl> <dt>Error</dt> </dl>      | The server experienced an error.<br/>                                                |
| <dl> <dt>Degraded</dt> </dl>   | The server is functioning but some features are turned off.<br/>                     |
| <dl> <dt>Unknown</dt> </dl>    | The status of the server is unknown.<br/>                                            |
| <dl> <dt>Pred Fail</dt> </dl>  | The server experienced a predictive failure.<br/>                                    |
| <dl> <dt>Starting</dt> </dl>   | The server is being started.<br/>                                                    |
| <dl> <dt>Stopping</dt> </dl>   | The server is being shut down.<br/>                                                  |
| <dl> <dt>Service</dt> </dl>    | The server is being serviced.<br/>                                                   |
| <dl> <dt>Stressed</dt> </dl>   | The server is having performance issues.<br/>                                        |
| <dl> <dt>NonRecover</dt> </dl> | The server has an error and cannot recover.<br/>                                     |
| <dl> <dt>No Contact</dt> </dl> | There is no contact with the server.<br/>                                            |
| <dl> <dt>Lost Comm</dt> </dl>  | Communication with the server been lost.<br/>                                        |
| <dl> <dt>Stopped</dt> </dl>    | The server is not running, however, it might be possible to restart the server.<br/> |



 

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/win32/wmisdk/standard-wmi-qualifiers) (Indexed), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-wmi-qualifiers) (CIM\_ManagedSystemElement.OperationalStatus)
</dt> </dl>

Gets an array of strings that describe the details of the corresponding array values in the **OperationalStatus** property.

This property is inherited from **CIM\_ManagedSystemElement**.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (256), **Propagated** (CIM\_System.CreationClassName)
</dt> </dl>

Gets the name of the class that represents the local system.

This property is inherited from **CIM\_ServiceAccessPoint**.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (256), **Propagated** (CIM\_System.Name)
</dt> </dl>

Gets the name of the local system.

This property is inherited from **CIM\_ServiceAccessPoint**.

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the date and time of the last change to the value of the **EnabledState** property.

This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

</dd> <dt>

**TransitioningToState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_EnabledLogicalElement.RequestStateChange, CIM\_EnabledLogicalElement.RequestedState, CIM\_EnabledLogicalElement.EnabledState)
</dt> </dl>

Gets the state to which the server will transition.

This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).



| Value                                                                             | Meaning                   |
|-----------------------------------------------------------------------------------|---------------------------|
| <dl> <dt>0</dt> </dl>      | Unknown<br/>        |
| <dl> <dt>2</dt> </dl>      | Enabled<br/>        |
| <dl> <dt>3</dt> </dl>      | Disabled<br/>       |
| <dl> <dt>4</dt> </dl>      | Shut Down<br/>      |
| <dl> <dt>5</dt> </dl>      | No Change<br/>      |
| <dl> <dt>6</dt> </dl>      | Offline<br/>        |
| <dl> <dt>7</dt> </dl>      | Test<br/>           |
| <dl> <dt>8</dt> </dl>      | Defer<br/>          |
| <dl> <dt>9</dt> </dl>      | Quiesce<br/>        |
| <dl> <dt>10</dt> </dl>     | Reboot<br/>         |
| <dl> <dt>11</dt> </dl>     | Reset<br/>          |
| <dl> <dt>12</dt> </dl>     | Not Applicable<br/> |
| <dl> <dt>13 ...</dt> </dl> | DMTF Reserved<br/>  |



 

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DnsClientCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientCim.dll</dt> </dl> |



## See also

<dl> <dt>

[Dnsclientcim Provider Classes](dns-client-classes.md)
</dt> </dl>

 

