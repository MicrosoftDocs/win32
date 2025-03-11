---
description: Represents a DNS client.
ms.assetid: aa81aa4e-1114-4433-bd8e-0973cfaf23ca
title: MSFT\_DNSClient class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_DNSClient
- MSFT_DNSClient.InstanceId
- MSFT_DNSClient.Caption
- MSFT_DNSClient.ElementName
- MSFT_DNSClient.InstallDate
- MSFT_DNSClient.StatusDescriptions
- MSFT_DNSClient.Status
- MSFT_DNSClient.HealthState
- MSFT_DNSClient.CommunicationStatus
- MSFT_DNSClient.DetailedStatus
- MSFT_DNSClient.OperatingStatus
- MSFT_DNSClient.PrimaryStatus
- MSFT_DNSClient.OtherEnabledState
- MSFT_DNSClient.RequestedState
- MSFT_DNSClient.EnabledDefault
- MSFT_DNSClient.TransitioningToState
- MSFT_DNSClient.SystemCreationClassName
- MSFT_DNSClient.SystemName
- MSFT_DNSClient.CreationClassName
- MSFT_DNSClient.Description
- MSFT_DNSClient.Name
- MSFT_DNSClient.OperationalStatus
- MSFT_DNSClient.EnabledState
- MSFT_DNSClient.TimeOfLastStateChange
- MSFT_DNSClient.NameFormat
- MSFT_DNSClient.ProtocolType
- MSFT_DNSClient.ProtocolIFType
- MSFT_DNSClient.OtherTypeDescription
- MSFT_DNSClient.Hostname
- MSFT_DNSClient.DHCPOptionsToUse
- MSFT_DNSClient.InterfaceIndex
- MSFT_DNSClient.InterfaceAlias
- MSFT_DNSClient.ConnectionSpecificSuffix
- MSFT_DNSClient.ConnectionSpecificSuffixSearchList
- MSFT_DNSClient.RegisterThisConnectionsAddress
- MSFT_DNSClient.UseSuffixWhenRegistering
api_type: 
- DllExport
api_location: 
- DnsClientCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_DNSClient class

Represents a DNS client.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_DNSClient : CIM_DNSProtocolEndpoint
{
  string   InstanceId;
  string   Caption;
  string   ElementName;
  datetime InstallDate;
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus[];
  uint16   PrimaryStatus;
  string   OtherEnabledState;
  uint16   RequestedState;
  uint16   EnabledDefault;
  uint16   TransitioningToState;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  string   Description;
  string   Name;
  uint16   OperationalStatus[];
  uint16   EnabledState[];
  datetime TimeOfLastStateChange;
  string   NameFormat;
  uint16   ProtocolType[];
  uint16   ProtocolIFType;
  string   OtherTypeDescription;
  string   Hostname;
  uint16   DHCPOptionsToUse[];
  uint32   InterfaceIndex;
  string   InterfaceAlias;
  string   ConnectionSpecificSuffix;
  string   ConnectionSpecificSuffixSearchList[];
  boolean  RegisterThisConnectionsAddress;
  boolean  UseSuffixWhenRegistering;
};
```

## Members

The **MSFT\_DNSClient** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DNSClient** class has these methods.



| Method                                                          | Description                                                                                                                                                                     |
|:----------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Register**](register-msft-dnsclient.md)                     | Registers the addresses of the local machine with the DNS server.<br/>                                                                                                    |
| [**RequestStateChange**](msft-dnsclient-requeststatechange.md) | Initiates a requests to change the state of a DNS client. <br/> This method is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).<br/> |



 

### Properties

The **MSFT\_DNSClient** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64), [**Dynamic**](/windows/win32/wmisdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the short description of the DNS client.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates the ability of the DNS client to communicate with the underlying [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)) object.

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

**ConnectionSpecificSuffix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the DNS suffix for a connection to the interface.

</dd> <dt>

**ConnectionSpecificSuffixSearchList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets and sets an array that contains the DNS suffix for each connection to the interface.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **key**, **MaxLen** (256)
</dt> </dl>

Gets the class name of the DNS client instance.

This property is inherited from the **CIM\_ServiceAccessPoint** class.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Override** (Description)
</dt> </dl>

Gets a description of the DNS client.

This property is inherited from the **CIM\_ProtocolEndpoint** class.

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets information about the status of the DNS client, in addition to the information provided by the **PrimaryStatus** property.

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

**DHCPOptionsToUse**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_DHCPProtocolEndpoint.OptionsReceived, CIM\_DNSSettingData.DHCPOptionsToUse)
</dt> </dl>

Gets an array that contains the Dynamic Host Configuration Protocol (DHCP) options that the DNS client uses after a DHCP bind operation.

This property is inherited from the **CIM\_DNSProtocolEndpoint** class.

This property can contain the following values:



| Value                                                                                  | Meaning                       |
|----------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>8</dt> </dl>           | Domain Name Server<br/> |
| <dl> <dt>14</dt> </dl>          | Host Name<br/>          |
| <dl> <dt>17</dt> </dl>          | Domain Name<br/>        |
| <dl> <dt>18 32767</dt> </dl>    | DMTF Reserverd<br/>     |
| <dl> <dt>32768 65535</dt> </dl> | Vendor Reserved<br/>    |



 

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly name of the DNS client.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Indicates the default startup configuration for the **EnabledState** property.

Default value: "2". This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

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

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_EnabledLogicalElement.OtherEnabledState), **Override** (EnabledState)
</dt> </dl>

Gets an array that indicates whether the DNS client is enabled or in some other related state.

This property is inherited from the **CIM\_ProtocolEndpoint** class.

This property can contain one of the following values:



| Value                                                                                  | Meaning                        |
|----------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>0</dt> </dl>           | Unknown<br/>             |
| <dl> <dt>1</dt> </dl>           | Other<br/>               |
| <dl> <dt>2</dt> </dl>           | Enabled<br/>             |
| <dl> <dt>3</dt> </dl>           | Disabled<br/>            |
| <dl> <dt>4</dt> </dl>           | Shutting Down<br/>       |
| <dl> <dt>5</dt> </dl>           | Reboot<br/>              |
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

Indicates the current health of the DNS client.

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

**Hostname**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Gets the host name of the DNS client connection.

This property is inherited from the **CIM\_DNSProtocolEndpoint** class.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/win32/wmisdk/standard-wmi-qualifiers) (MIF.DMTF\|ComponentID\|001.5)
</dt> </dl>

Gets the **datetime** value that indicates when the DNS client was installed.

This property is inherited from **CIM\_ManagedSystemElement**.

</dd> <dt>

**InstanceId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the unique identifier of this object. The ID must be unique within the scope of the instantiating namespace.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly name of the interface.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly index to the interface.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (256), **key**, **Override** (Name)
</dt> </dl>

Gets the ID of the DNS client interface.

This property is inherited from the **CIM\_ProtocolEndpoint** class.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (256)
</dt> </dl>

Gets the structure of the **Name** property, which ensures that Name is a unique value.

This property is inherited from the **CIM\_ProtocolEndpoint** class.

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-wmi-qualifiers) (CIM\_EnabledLogicalElement.EnabledState)
</dt> </dl>

Gets an array that contains information about the operating status of the DNS client, in addition to the information provided by the **EnabledState** property.

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

Qualifiers: **ArrayType** (Indexed), **ModelCorrespondence** (CIM\_ManagedSystemElement.StatusDescriptions), **Override** (OperationalStatus)
</dt> </dl>

Gets the current statuses of the DNS client.

This property is inherited from the **CIM\_ProtocolEndpoint** class.

This property can contain one of the following values:



| Value                                                                                | Meaning                            |
|--------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>0</dt> </dl>         | Unknown<br/>                 |
| <dl> <dt>1</dt> </dl>         | Other<br/>                   |
| <dl> <dt>2</dt> </dl>         | OK<br/>                      |
| <dl> <dt>3</dt> </dl>         | Degraded<br/>                |
| <dl> <dt>4</dt> </dl>         | Stressed<br/>                |
| <dl> <dt>5</dt> </dl>         | Error<br/>                   |
| <dl> <dt>6</dt> </dl>         | Non-Recoverable Error<br/>   |
| <dl> <dt>7</dt> </dl>         | Starting<br/>                |
| <dl> <dt>8</dt> </dl>         | Stopping<br/>                |
| <dl> <dt>9</dt> </dl>         | Stopped<br/>                 |
| <dl> <dt>10</dt> </dl>        | In Service<br/>              |
| <dl> <dt>11</dt> </dl>        |                                    |
| <dl> <dt>12</dt> </dl>        | No Contact<br/>              |
| <dl> <dt>13</dt> </dl>        | Lost Communication<br/>      |
| <dl> <dt>14</dt> </dl>        | Aborted<br/>                 |
| <dl> <dt>15</dt> </dl>        | Dormant<br/>                 |
| <dl> <dt>16</dt> </dl>        | Supporting Entity Error<br/> |
| <dl> <dt>17</dt> </dl>        | Completed<br/>               |
| <dl> <dt>18</dt> </dl>        | Power Mode<br/>              |
| <dl> <dt>19 32767</dt> </dl>  | DMTF Reserved<br/>           |
| <dl> <dt>32768 ...</dt> </dl> | Vendor Reserved<br/>         |



 

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

**OtherTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64), **ModelCorrespondence** (CIM\_ProtocolEndpoint.ProtocolType, CIM\_ProtocolEndpoint.ProtocolIFType)
</dt> </dl>

Gets a string that describes the network protocol to use when the **ProtocolIFType** property is set to 1 (Other); otherwise, this value must be set to **null**.

This property is inherited from the **CIM\_ProtocolEndpoint** class.

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_ManagedSystemElement.DetailedStatus, CIM\_ManagedSystemElement.HealthState)
</dt> </dl>

Gets the high level status of the DNS client.

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

**ProtocolIFType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_ProtocolEndpoint.OtherTypeDescription)
</dt> </dl>

Gets the network protocols that are supported by the DNS client.

This property is inherited from the **CIM\_ProtocolEndpoint** class.

This property can contain the following values:



| Value                                                                                 | Meaning                                                             |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>          | Unknown<br/>                                                  |
| <dl> <dt>1</dt> </dl>          | Other<br/>                                                    |
| <dl> <dt>2</dt> </dl>          | Regular 1822<br/>                                             |
| <dl> <dt>3</dt> </dl>          | HDH 1822<br/>                                                 |
| <dl> <dt>4</dt> </dl>          | DDN X.25<br/>                                                 |
| <dl> <dt>5</dt> </dl>          | RFC877 X.25<br/>                                              |
| <dl> <dt>6</dt> </dl>          | Ethernet CSMA/CD<br/>                                         |
| <dl> <dt>7</dt> </dl>          | ISO 802.3 CSMA/CD<br/>                                        |
| <dl> <dt>8</dt> </dl>          | ISO 802.4 Token Bus<br/>                                      |
| <dl> <dt>9</dt> </dl>          | ISO 802.5 Token Ring<br/>                                     |
| <dl> <dt>10</dt> </dl>         | ISO 802.6 MAN<br/>                                            |
| <dl> <dt>11</dt> </dl>         | StarLAN<br/>                                                  |
| <dl> <dt>12</dt> </dl>         | "Proteon 10Mbit<br/>                                          |
| <dl> <dt>13</dt> </dl>         | Proteon 80Mbit<br/>                                           |
| <dl> <dt>14</dt> </dl>         | HyperChannel<br/>                                             |
| <dl> <dt>15</dt> </dl>         | FDDI<br/>                                                     |
| <dl> <dt>16</dt> </dl>         | LAP-B<br/>                                                    |
| <dl> <dt>17</dt> </dl>         | SDLC<br/>                                                     |
| <dl> <dt>18</dt> </dl>         | DS1<br/>                                                      |
| <dl> <dt>19</dt> </dl>         | E1<br/>                                                       |
| <dl> <dt>20</dt> </dl>         | Basic ISDN<br/>                                               |
| <dl> <dt>21</dt> </dl>         | Primary ISDN<br/>                                             |
| <dl> <dt>22</dt> </dl>         | Proprietary Point-to-Point Serial<br/>                        |
| <dl> <dt>23</dt> </dl>         | PPP<br/>                                                      |
| <dl> <dt>24</dt> </dl>         | Software Loopbac<br/>                                         |
| <dl> <dt>25</dt> </dl>         | EON<br/>                                                      |
| <dl> <dt>26</dt> </dl>         | Ethernet 3Mbit<br/>                                           |
| <dl> <dt>27</dt> </dl>         | NSIP<br/>                                                     |
| <dl> <dt>28</dt> </dl>         | SLIP<br/>                                                     |
| <dl> <dt>29</dt> </dl>         | Ultra<br/>                                                    |
| <dl> <dt>30</dt> </dl>         | DS3<br/>                                                      |
| <dl> <dt>31</dt> </dl>         | SIP<br/>                                                      |
| <dl> <dt>32</dt> </dl>         | Frame Relay<br/>                                              |
| <dl> <dt>33</dt> </dl>         | RS-232<br/>                                                   |
| <dl> <dt>34</dt> </dl>         | Parallel<br/>                                                 |
| <dl> <dt>35</dt> </dl>         | ARCNet<br/>                                                   |
| <dl> <dt>36</dt> </dl>         | ARCNet Plus<br/>                                              |
| <dl> <dt>37</dt> </dl>         | ATM<br/>                                                      |
| <dl> <dt>38</dt> </dl>         | MIO X.25<br/>                                                 |
| <dl> <dt>39</dt> </dl>         | SONET<br/>                                                    |
| <dl> <dt>40</dt> </dl>         | X.25 PLE<br/>                                                 |
| <dl> <dt>41</dt> </dl>         | ISO 802.211c<br/>                                             |
| <dl> <dt>42</dt> </dl>         | LocalTalk<br/>                                                |
| <dl> <dt>43</dt> </dl>         | SMDS DXI<br/>                                                 |
| <dl> <dt>44</dt> </dl>         | Frame Relay Service<br/>                                      |
| <dl> <dt>45</dt> </dl>         | V.35<br/>                                                     |
| <dl> <dt>46</dt> </dl>         | HSSI<br/>                                                     |
| <dl> <dt>47</dt> </dl>         | HIPPI<br/>                                                    |
| <dl> <dt>48</dt> </dl>         | Modem<br/>                                                    |
| <dl> <dt>49</dt> </dl>         | AAL5<br/>                                                     |
| <dl> <dt>50</dt> </dl>         | SONET Path<br/>                                               |
| <dl> <dt>51</dt> </dl>         | SONET VT<br/>                                                 |
| <dl> <dt>52</dt> </dl>         | SMDS ICIP<br/>                                                |
| <dl> <dt>53</dt> </dl>         | Proprietary Virtual/Internal<br/>                             |
| <dl> <dt>54</dt> </dl>         | Proprietary Multiplexor<br/>                                  |
| <dl> <dt>55</dt> </dl>         | IEEE 802.12<br/>                                              |
| <dl> <dt>56</dt> </dl>         | Fibre Channel<br/>                                            |
| <dl> <dt>57</dt> </dl>         | HIPPI Interface<br/>                                          |
| <dl> <dt>58</dt> </dl>         | Frame Relay Interconnect<br/>                                 |
| <dl> <dt>59</dt> </dl>         | ATM Emulated LAN for 802.3<br/>                               |
| <dl> <dt>60</dt> </dl>         | ATM Emulated LAN for 802.5<br/>                               |
| <dl> <dt>61</dt> </dl>         | ATM Emulated Circuit<br/>                                     |
| <dl> <dt>62</dt> </dl>         | Fast Ethernet (100BaseT)<br/>                                 |
| <dl> <dt>63</dt> </dl>         | ISDN<br/>                                                     |
| <dl> <dt>64</dt> </dl>         | V.11<br/>                                                     |
| <dl> <dt>65</dt> </dl>         | V.36<br/>                                                     |
| <dl> <dt>66</dt> </dl>         | G703 at 64K<br/>                                              |
| <dl> <dt>67</dt> </dl>         | G703 at 2Mb<br/>                                              |
| <dl> <dt>68</dt> </dl>         | QLLC<br/>                                                     |
| <dl> <dt>69</dt> </dl>         | Fast Ethernet 100BaseFX<br/>                                  |
| <dl> <dt>70</dt> </dl>         | Channel<br/>                                                  |
| <dl> <dt>71</dt> </dl>         | IEEE 802.11<br/>                                              |
| <dl> <dt>72</dt> </dl>         | IBM 260/370 OEMI Channel<br/>                                 |
| <dl> <dt>73</dt> </dl>         | ESCON<br/>                                                    |
| <dl> <dt>74</dt> </dl>         | Data Link Switching<br/>                                      |
| <dl> <dt>75</dt> </dl>         | ISDN S/T Interface<br/>                                       |
| <dl> <dt>76</dt> </dl>         | ISDN U Interface<br/>                                         |
| <dl> <dt>77</dt> </dl>         | LAP-D<br/>                                                    |
| <dl> <dt>78</dt> </dl>         | IP Switch<br/>                                                |
| <dl> <dt>79</dt> </dl>         | Remote Source Route Bridging<br/>                             |
| <dl> <dt>80</dt> </dl>         | ATM Logical<br/>                                              |
| <dl> <dt>81</dt> </dl>         | DS0<br/>                                                      |
| <dl> <dt>82</dt> </dl>         | DS0 Bundle<br/>                                               |
| <dl> <dt>83</dt> </dl>         | BSC<br/>                                                      |
| <dl> <dt>84</dt> </dl>         | Async<br/>                                                    |
| <dl> <dt>85</dt> </dl>         | Combat Net Radio<br/>                                         |
| <dl> <dt>86</dt> </dl>         | ISO 802.5r DTR<br/>                                           |
| <dl> <dt>87</dt> </dl>         | Ext Pos Loc Report System<br/>                                |
| <dl> <dt>88</dt> </dl>         | AppleTalk Remote Access Protocol<br/>                         |
| <dl> <dt>89</dt> </dl>         | Proprietary Connectionless<br/>                               |
| <dl> <dt>90</dt> </dl>         | ITU X.29 Host PAD<br/>                                        |
| <dl> <dt>91</dt> </dl>         | ITU X.3 Terminal PAD<br/>                                     |
| <dl> <dt>92</dt> </dl>         | Frame Relay MPI<br/>                                          |
| <dl> <dt>93</dt> </dl>         | ITU X.213<br/>                                                |
| <dl> <dt>94</dt> </dl>         | ADSL<br/>                                                     |
| <dl> <dt>95</dt> </dl>         | RADSL<br/>                                                    |
| <dl> <dt>96</dt> </dl>         | SDSL<br/>                                                     |
| <dl> <dt>97</dt> </dl>         | VDSL<br/>                                                     |
| <dl> <dt>98</dt> </dl>         | ISO 802.5 CRFP<br/>                                           |
| <dl> <dt>99</dt> </dl>         | Myrinet<br/>                                                  |
| <dl> <dt>100</dt> </dl>        | Voice Receive and Transmit<br/>                               |
| <dl> <dt>101</dt> </dl>        | Voice Foreign Exchange Office<br/>                            |
| <dl> <dt>102</dt> </dl>        | Voice Foreign Exchange Service<br/>                           |
| <dl> <dt>103</dt> </dl>        | Voice Encapsulation<br/>                                      |
| <dl> <dt>104</dt> </dl>        | Voice over IP<br/>                                            |
| <dl> <dt>105</dt> </dl>        | ATM DXI<br/>                                                  |
| <dl> <dt>106</dt> </dl>        | ATM FUNI<br/>                                                 |
| <dl> <dt>107</dt> </dl>        | ATM IMA<br/>                                                  |
| <dl> <dt>108</dt> </dl>        | PPP Multilink Bundle<br/>                                     |
| <dl> <dt>109</dt> </dl>        | IP over CDLC<br/>                                             |
| <dl> <dt>110</dt> </dl>        | IP over CLAW<br/>                                             |
| <dl> <dt>111</dt> </dl>        | Stack to Stack<br/>                                           |
| <dl> <dt>112</dt> </dl>        | Virtual IP Address<br/>                                       |
| <dl> <dt>113</dt> </dl>        | MPC<br/>                                                      |
| <dl> <dt>114</dt> </dl>        | IP over ATM<br/>                                              |
| <dl> <dt>115</dt> </dl>        | ISO 802.5j Fibre Token Ring<br/>                              |
| <dl> <dt>116</dt> </dl>        | TDLC<br/>                                                     |
| <dl> <dt>117</dt> </dl>        | Gigabit Ethernet<br/>                                         |
| <dl> <dt>118</dt> </dl>        | HDLC<br/>                                                     |
| <dl> <dt>119</dt> </dl>        | LAP-F<br/>                                                    |
| <dl> <dt>120</dt> </dl>        | V.37<br/>                                                     |
| <dl> <dt>121</dt> </dl>        | X.25 MLP<br/>                                                 |
| <dl> <dt>122</dt> </dl>        | X.25 Hunt Group<br/>                                          |
| <dl> <dt>123</dt> </dl>        | Transp HDLC<br/>                                              |
| <dl> <dt>124</dt> </dl>        | Interleave Channel<br/>                                       |
| <dl> <dt>125</dt> </dl>        | FAST Channel<br/>                                             |
| <dl> <dt>126</dt> </dl>        | IP (for APPN HPR in IP Networks)<br/>                         |
| <dl> <dt>127</dt> </dl>        | CATV MAC Layer<br/>                                           |
| <dl> <dt>128</dt> </dl>        | CATV Downstream<br/>                                          |
| <dl> <dt>129</dt> </dl>        | CATV Upstream<br/>                                            |
| <dl> <dt>130</dt> </dl>        | Avalon 12MPP Switch<br/>                                      |
| <dl> <dt>131</dt> </dl>        | Tunnel<br/>                                                   |
| <dl> <dt>132</dt> </dl>        | Coffee<br/>                                                   |
| <dl> <dt>133</dt> </dl>        | Circuit Emulation Service<br/>                                |
| <dl> <dt>134</dt> </dl>        | ATM SubInterface<br/>                                         |
| <dl> <dt>135</dt> </dl>        | Layer 2 VLAN using 802.1Q<br/>                                |
| <dl> <dt>136</dt> </dl>        | Layer 3 VLAN using IP<br/>                                    |
| <dl> <dt>137</dt> </dl>        | Layer 3 VLAN using IPX<br/>                                   |
| <dl> <dt>138</dt> </dl>        | Digital Power Line<br/>                                       |
| <dl> <dt>139</dt> </dl>        | Multimedia Mail over IP<br/>                                  |
| <dl> <dt>140</dt> </dl>        | DTM<br/>                                                      |
| <dl> <dt>141</dt> </dl>        | DCN<br/>                                                      |
| <dl> <dt>142</dt> </dl>        | IP Forwarding<br/>                                            |
| <dl> <dt>143</dt> </dl>        | MSDSL<br/>                                                    |
| <dl> <dt>144</dt> </dl>        | IEEE 1394<br/>                                                |
| <dl> <dt>145</dt> </dl>        | IF-GSN/HIPPI-6400<br/>                                        |
| <dl> <dt>146</dt> </dl>        | DVB-RCC MAC Layer<br/>                                        |
| <dl> <dt>147</dt> </dl>        | DVB-RCC Downstream<br/>                                       |
| <dl> <dt>148</dt> </dl>        | DVB-RCC Upstream<br/>                                         |
| <dl> <dt>149</dt> </dl>        | ATM Virtual<br/>                                              |
| <dl> <dt>150</dt> </dl>        | MPLS Tunnel<br/>                                              |
| <dl> <dt>151</dt> </dl>        | SRP<br/>                                                      |
| <dl> <dt>152</dt> </dl>        | Voice over ATM<br/>                                           |
| <dl> <dt>153</dt> </dl>        | Voice over Frame Relay<br/>                                   |
| <dl> <dt>154</dt> </dl>        | ISDL<br/>                                                     |
| <dl> <dt>155</dt> </dl>        | Composite Link<br/>                                           |
| <dl> <dt>156</dt> </dl>        | SS7 Signaling Link<br/>                                       |
| <dl> <dt>157</dt> </dl>        | Proprietary P2P Wireless<br/>                                 |
| <dl> <dt>158</dt> </dl>        | Frame Forward<br/>                                            |
| <dl> <dt>159</dt> </dl>        | RFC1483 Multiprotocol over ATM<br/>                           |
| <dl> <dt>160</dt> </dl>        | USB<br/>                                                      |
| <dl> <dt>161</dt> </dl>        | IEEE 802.3ad Link Aggregate<br/>                              |
| <dl> <dt>162</dt> </dl>        | BGP Policy Accounting<br/>                                    |
| <dl> <dt>163</dt> </dl>        | FRF .16 Multilink FR<br/>                                     |
| <dl> <dt>164</dt> </dl>        | H.323 Gatekeeper<br/>                                         |
| <dl> <dt>165</dt> </dl>        | H.323 Proxy<br/>                                              |
| <dl> <dt>166</dt> </dl>        | MPLS<br/>                                                     |
| <dl> <dt>167</dt> </dl>        | Multi-Frequency Signaling Link<br/>                           |
| <dl> <dt>168</dt> </dl>        | HDSL-2<br/>                                                   |
| <dl> <dt>169</dt> </dl>        | S-HDSL<br/>                                                   |
| <dl> <dt>170</dt> </dl>        | DS1 Facility Data Link<br/>                                   |
| <dl> <dt>171</dt> </dl>        | Packet over SONET/SDH<br/>                                    |
| <dl> <dt>172</dt> </dl>        | DVB-ASI Input<br/>                                            |
| <dl> <dt>173</dt> </dl>        | DVB-ASI Output<br/>                                           |
| <dl> <dt>174</dt> </dl>        | Power Line<br/>                                               |
| <dl> <dt>175</dt> </dl>        | Non Facility Associated Signaling<br/>                        |
| <dl> <dt>176</dt> </dl>        | TR008<br/>                                                    |
| <dl> <dt>177</dt> </dl>        | GR303 RDT<br/>                                                |
| <dl> <dt>178</dt> </dl>        | GR303 RDT<br/>                                                |
| <dl> <dt>179</dt> </dl>        | ISUP<br/>                                                     |
| <dl> <dt>180</dt> </dl>        | Proprietary Wireless MAC Layer<br/>                           |
| <dl> <dt>181</dt> </dl>        | Proprietary Wireless Downstream<br/>                          |
| <dl> <dt>182</dt> </dl>        | Proprietary Wireless Upstream<br/>                            |
| <dl> <dt>183</dt> </dl>        | HIPERLAN Type 2<br/>                                          |
| <dl> <dt>184</dt> </dl>        | Proprietary Broadband Wireless Access Point to Mulipoint<br/> |
| <dl> <dt>185</dt> </dl>        | SONET Overhead Channel<br/>                                   |
| <dl> <dt>186</dt> </dl>        | Digital Wrapper Overhead Channel<br/>                         |
| <dl> <dt>187</dt> </dl>        | ATM Adaptation Layer 2<br/>                                   |
| <dl> <dt>188</dt> </dl>        | Radio MAC<br/>                                                |
| <dl> <dt>189</dt> </dl>        | ATM Radio<br/>                                                |
| <dl> <dt>190</dt> </dl>        | Inter Machine Trunk<br/>                                      |
| <dl> <dt>191</dt> </dl>        | MVL DSL<br/>                                                  |
| <dl> <dt>192</dt> </dl>        | Long Read DSL<br/>                                            |
| <dl> <dt>193</dt> </dl>        | Frame Relay DLCI Endpoint<br/>                                |
| <dl> <dt>194</dt> </dl>        | ATM VCI Endpoint<br/>                                         |
| <dl> <dt>195</dt> </dl>        | Optical Channel<br/>                                          |
| <dl> <dt>196</dt> </dl>        | Optical Transport<br/>                                        |
| <dl> <dt>197</dt> </dl>        | Proprietary ATM<br/>                                          |
| <dl> <dt>198</dt> </dl>        | Voice over Cable<br/>                                         |
| <dl> <dt>199</dt> </dl>        | Infiniband<br/>                                               |
| <dl> <dt>200</dt> </dl>        | TE Link<br/>                                                  |
| <dl> <dt>201</dt> </dl>        | Q.2931<br/>                                                   |
| <dl> <dt>202</dt> </dl>        | Virtual Trunk Group<br/>                                      |
| <dl> <dt>203</dt> </dl>        | SIP Trunk Group<br/>                                          |
| <dl> <dt>204</dt> </dl>        | SIP Signaling<br/>                                            |
| <dl> <dt>205</dt> </dl>        | CATV Upstream Channel<br/>                                    |
| <dl> <dt>206</dt> </dl>        | Econet<br/>                                                   |
| <dl> <dt>207</dt> </dl>        | FSAN 155Mb PON<br/>                                           |
| <dl> <dt>208</dt> </dl>        | FSAN 622Mb PON<br/>                                           |
| <dl> <dt>209</dt> </dl>        | Transparent Bridge<br/>                                       |
| <dl> <dt>210</dt> </dl>        | Line Group<br/>                                               |
| <dl> <dt>211</dt> </dl>        | Voice E&M Feature Group<br/>                                  |
| <dl> <dt>212</dt> </dl>        | Voice FGD EANA<br/>                                           |
| <dl> <dt>213</dt> </dl>        | Voice DID<br/>                                                |
| <dl> <dt>214</dt> </dl>        | MPEG Transport<br/>                                           |
| <dl> <dt>215</dt> </dl>        | 6To4<br/>                                                     |
| <dl> <dt>216</dt> </dl>        | GTP<br/>                                                      |
| <dl> <dt>217</dt> </dl>        | Paradyne EtherLoop 1<br/>                                     |
| <dl> <dt>218</dt> </dl>        | Paradyne EtherLoop 2<br/>                                     |
| <dl> <dt>219</dt> </dl>        | Optical Channel Group<br/>                                    |
| <dl> <dt>220</dt> </dl>        | HomePNA<br/>                                                  |
| <dl> <dt>221</dt> </dl>        | GFP<br/>                                                      |
| <dl> <dt>222</dt> </dl>        | ciscoISLvlan<br/>                                             |
| <dl> <dt>223</dt> </dl>        | actelisMetaLOOP<br/>                                          |
| <dl> <dt>224</dt> </dl>        | Fcip<br/>                                                     |
| <dl> <dt>225 4095</dt> </dl>   | IANA Reserved<br/>                                            |
| <dl> <dt>4096</dt> </dl>       | IPv4<br/>                                                     |
| <dl> <dt>4097</dt> </dl>       | IPv6<br/>                                                     |
| <dl> <dt>4098</dt> </dl>       | IPv4/v6<br/>                                                  |
| <dl> <dt>4099</dt> </dl>       | IPX<br/>                                                      |
| <dl> <dt>4100</dt> </dl>       | DECnet<br/>                                                   |
| <dl> <dt>4101</dt> </dl>       | SNA<br/>                                                      |
| <dl> <dt>4102</dt> </dl>       | CONP<br/>                                                     |
| <dl> <dt>4103</dt> </dl>       | CLNP<br/>                                                     |
| <dl> <dt>4104</dt> </dl>       | VINES<br/>                                                    |
| <dl> <dt>4105</dt> </dl>       | XNS<br/>                                                      |
| <dl> <dt>4106</dt> </dl>       | ISDN B Channel Endpoint<br/>                                  |
| <dl> <dt>4107</dt> </dl>       | ISDN D Channel Endpoint<br/>                                  |
| <dl> <dt>4108</dt> </dl>       | BGP<br/>                                                      |
| <dl> <dt>4109</dt> </dl>       | OSPF<br/>                                                     |
| <dl> <dt>4110</dt> </dl>       | UDP<br/>                                                      |
| <dl> <dt>4111</dt> </dl>       | TCP<br/>                                                      |
| <dl> <dt>4112</dt> </dl>       | 802.11a<br/>                                                  |
| <dl> <dt>4113</dt> </dl>       | 802.11b<br/>                                                  |
| <dl> <dt>4114</dt> </dl>       | 802.11g<br/>                                                  |
| <dl> <dt>4115</dt> </dl>       | 802.11h<br/>                                                  |
| <dl> <dt>4200</dt> </dl>       | NFS<br/>                                                      |
| <dl> <dt>4201</dt> </dl>       | CIFS<br/>                                                     |
| <dl> <dt>4202</dt> </dl>       | DAFS<br/>                                                     |
| <dl> <dt>4203</dt> </dl>       | WebDAV<br/>                                                   |
| <dl> <dt>4204</dt> </dl>       | HTTP<br/>                                                     |
| <dl> <dt>4205</dt> </dl>       | FTP<br/>                                                      |
| <dl> <dt>4300</dt> </dl>       | NDMP<br/>                                                     |
| <dl> <dt>4400</dt> </dl>       | Telnet<br/>                                                   |
| <dl> <dt>4401</dt> </dl>       | SSH<br/>                                                      |
| <dl> <dt>4402</dt> </dl>       | SM CLP<br/>                                                   |
| <dl> <dt>4403</dt> </dl>       | SMTP<br/>                                                     |
| <dl> <dt>4404</dt> </dl>       | LDAP<br/>                                                     |
| <dl> <dt>4405</dt> </dl>       | RDP<br/>                                                      |
| <dl> <dt>4406</dt> </dl>       | HTTPS<br/>                                                    |
| <dl> <dt>4407 32767</dt> </dl> | DMTF Reserved<br/>                                            |
| <dl> <dt>32768 ...</dt> </dl>  | Vendor Reserved<br/>                                          |



 

</dd> <dt>

**ProtocolType**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_ProtocolEndpoint.OtherTypeDescription), **Override** (EnabledState), **Deprecated** (CIM\_ProtocolEndpoint.ProtocolIFType)
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead, we recommend that you use the **CIM\_ProtocolEndpoint.ProtocolIFType** property.

 

Gets the network protocols that are supported by the DNS client.

This property is inherited from the **CIM\_ProtocolEndpoint** class.

This property can contain the following values:



| Value                                                                         | Meaning                            |
|-------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>0</dt> </dl>  | Unknown<br/>                 |
| <dl> <dt>1</dt> </dl>  | Other<br/>                   |
| <dl> <dt>2</dt> </dl>  | IPv4<br/>                    |
| <dl> <dt>3</dt> </dl>  | IPv6<br/>                    |
| <dl> <dt>4</dt> </dl>  | IPX<br/>                     |
| <dl> <dt>5</dt> </dl>  | AppleTalk<br/>               |
| <dl> <dt>6</dt> </dl>  | DECnet<br/>                  |
| <dl> <dt>7</dt> </dl>  | SNA<br/>                     |
| <dl> <dt>8</dt> </dl>  | CONP<br/>                    |
| <dl> <dt>9</dt> </dl>  | CLNP<br/>                    |
| <dl> <dt>10</dt> </dl> | VINES<br/>                   |
| <dl> <dt>11</dt> </dl> | XNS<br/>                     |
| <dl> <dt>12</dt> </dl> | ATM<br/>                     |
| <dl> <dt>13</dt> </dl> | Frame Relay<br/>             |
| <dl> <dt>14</dt> </dl> | Ethernet<br/>                |
| <dl> <dt>15</dt> </dl> | TokenRing<br/>               |
| <dl> <dt>16</dt> </dl> | FDDI<br/>                    |
| <dl> <dt>17</dt> </dl> | Infiniband<br/>              |
| <dl> <dt>18</dt> </dl> | Fibre Channel<br/>           |
| <dl> <dt>19</dt> </dl> | ISDN BRI Endpoint<br/>       |
| <dl> <dt>20</dt> </dl> | ISDN B Channel Endpoint<br/> |
| <dl> <dt>21</dt> </dl> | ISDN D Channel Endpoint<br/> |
| <dl> <dt>22</dt> </dl> | IPv4/v6<br/>                 |
| <dl> <dt>23</dt> </dl> | BGP<br/>                     |
| <dl> <dt>24</dt> </dl> | OSPF<br/>                    |
| <dl> <dt>25</dt> </dl> | MPLS<br/>                    |
| <dl> <dt>26</dt> </dl> | UDP<br/>                     |
| <dl> <dt>27</dt> </dl> | TCP<br/>                     |



 

</dd> <dt>

**RegisterThisConnectionsAddress**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether to register the address of the current connection with DNS.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the last requested state of the DNS client. The actual state of the client is represented by the **EnabledState** property.

Default value: "12".

This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

This property contains one of the following values:



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

 

Gets the status of the DNS client.

This property is inherited from **CIM\_ManagedSystemElement**.

This property contains one of the following values:



| Value                                                                                 | Meaning                                                                                            |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>OK</dt> </dl>         | The DNS client is functioning without errors.<br/>                                           |
| <dl> <dt>Error</dt> </dl>      | The DNS client experienced an error.<br/>                                                    |
| <dl> <dt>Degraded</dt> </dl>   | The DNS client is functioning but some features are turned off.<br/>                         |
| <dl> <dt>Unknown</dt> </dl>    | The status of the DNS client is unknown.<br/>                                                |
| <dl> <dt>Pred Fail</dt> </dl>  | The DNS client experienced a predictive failure.<br/>                                        |
| <dl> <dt>Starting</dt> </dl>   | The DNS client is being started.<br/>                                                        |
| <dl> <dt>Stopping</dt> </dl>   | The DNS client is being shut down.<br/>                                                      |
| <dl> <dt>Service</dt> </dl>    | The DNS client is being serviced.<br/>                                                       |
| <dl> <dt>Stressed</dt> </dl>   | The DNS client is having performance issues.<br/>                                            |
| <dl> <dt>NonRecover</dt> </dl> | The DNS client has an error and cannot recover.<br/>                                         |
| <dl> <dt>No Contact</dt> </dl> | There is no contact with the DNS client.<br/>                                                |
| <dl> <dt>Lost Comm</dt> </dl>  | Communication with the DNS client has been lost.<br/>                                        |
| <dl> <dt>Stopped</dt> </dl>    | The DNS client is not running, however, it might be possible to restart the DNS client.<br/> |



 

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

Qualifiers: **key**, **MaxLen** (256), **Propagated** (CIM\_System.CreationClassName)
</dt> </dl>

Gets the class name of the system object that hosts the DNS client.

This property is inherited from the **CIM\_ServiceAccessPoint** class.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **key**, **MaxLen** (256), **Propagated** (CIM\_System.Name)
</dt> </dl>

Gets the name of the system that hosts the DNS client.

This property is inherited from the **CIM\_ServiceAccessPoint** class.

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Override** (TimeOfLastStateChange)
</dt> </dl>

Gets the **datetime** value that indicates when the **EnabledState** property was last changed.

</dd> <dt>

**TransitioningToState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_EnabledLogicalElement.RequestStateChange, CIM\_EnabledLogicalElement.RequestedState, CIM\_EnabledLogicalElement.EnabledState)
</dt> </dl>

Gets the state to which the DNS client will transition.

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



 

</dd> <dt>

**UseSuffixWhenRegistering**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether to use the DNS suffix for the connection during DNS registration.

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

[Dnsclientcim Provider Class](dns-client-classes.md)
</dt> </dl>

 

