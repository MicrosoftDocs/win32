---
title: Implementing Device Behavior
description: The behavior of a device is defined by the services it exposes.
ms.assetid: 5b352870-6de1-42f2-a178-ed7036b7afc9
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Device Behavior

The behavior of a device is defined by the services it exposes. Each service has a service description that lists its actions and state variables. Taken together, these service descriptions make up the service interface, which defines the way in which a control point can interact with a service. Each service must have at least one action.

To implement a service, a hosted device must provide a Component Object Model (COM) object that exposes the interface for the service. In the service description, the service interfaces are specified in UPnP Template Language (UTL); however, COM object interfaces typically are specified in Interface Definition Language (IDL). You can also specify the COM interface in a type library or header file. The Platform Software Development Kit (SDK) includes the Utl2idl tool, which translates a service description in UTL to a COM interface in IDL.

The following samples illustrate this conversion process. The service description is provided by the device developer and is written in UTL.

``` syntax
<?xml version="1.0" ?> 
  <scpd xmlns="urn:schemas-upnp-org:service-1-0">

    <specVersion>
      <major>1</major> 
      <minor>0</minor> 
    </specVersion>

    <serviceStateTable>
      <stateVariable>
        <name>Power</name> 
        <dataType>Boolean</dataType> 
        <defaultValue>0</defaultValue> 
      </stateVariable>

      <stateVariable>
        <name>Level</name> 
        <dataType>i4</dataType> 
        <allowedValueRange>
          <minimum>0</minimum> 
            <maximum>10</maximum> 
            <step>1</step> 
        </allowedValueRange>
        <defaultValue>0</defaultValue> 
      </stateVariable>

      <stateVariable>
        <name>State</name> 
        <dataType>string</dataType> 
        <allowedValueList>
          <allowedValue>ON</allowedValue> 
          <allowedValue>OFF</allowedValue> 
          <allowedValue>DIMMED</allowedValue> 
        </allowedValueList>
        <defaultValue>OFF</defaultValue> 
      </stateVariable>
    </serviceStateTable>

    <actionList>
      <action>
        <name>PowerOn</name> 
      </action>

      <action>
        <name>PowerOff</name> 
      </action>

      <action>
        <name>SetLevel</name> 
        <argumentList>
          <argument>
            <name>NewLevel</name> 
            <relatedStateVariable>Level</relatedStateVariable> 
            <direction>in</direction> 
          </argument>
          <argument>
            <name>NewState</name> 
            <relatedStateVariable>State</relatedStateVariable> 
            <direction>out</direction> 
          </argument>
        </argumentList>
      </action>

      <action>
        <name>IncreaseLevel</name> 
      </action>

      <action>
        <name>DecreaseLevel</name> 
      </action>
    </actionList>
</scpd>
```

The next step is to run the Utl2idl tool. It produces the IDL file that contains the COM interface. For more information about IDL files and the **interface** keyword, see [Interface Definition (IDL) File](/windows/desktop/Midl/interface-definition-idl-file) and [**interface**](/windows/desktop/Midl/interface) in the MIDL reference.

``` syntax
#include <windows.h>
typedef [v1_enum] enum SCPD_DISPIDS
{
     DISPID_POWER = 1,
     DISPID_LEVEL,
     DISPID_STATE,
     DISPID_POWERON,
     DISPID_POWEROFF,
     DISPID_SETLEVEL,
     DISPID_INCREASELEVEL,
     DISPID_DECREASELEVEL
} SCPD_DISPIDS;

[
     uuid(68369839-960d-4c8c-8d0d-c319c69e73be),
     oleautomation,
     pointer_default(unique)
]
interface IUPnPService_scpd : IUnknown 
{
     [propget, id(DISPID_POWER), helpstring("Property Power")]
     HRESULT Power(
          [out, retval] VARIANT_BOOL *pPower);

     [propget, id(DISPID_LEVEL), helpstring("Property Level")]
     HRESULT Level(
          [out, retval] long *pLevel);

     [propget, id(DISPID_STATE), helpstring("Property State")]
     HRESULT State(
          [out, retval] BSTR *pState);

     [ id(DISPID_POWERON), helpstring("Method PowerOn")]
     HRESULT PowerOn();

     [ id(DISPID_POWEROFF), helpstring("Method PowerOff")]
     HRESULT PowerOff();

     [ id(DISPID_SETLEVEL), helpstring("Method SetLevel")]
     HRESULT SetLevel(
          [in] long NewLevel,
          [in, out] BSTR *pNewState;
                                
     [ id(DISPID_INCREASELEVEL), helpstring("Method IncreaseLevel")]
     HRESULT IncreaseLevel();

     [ id(DISPID_DECREASELEVEL), helpstring("Method DecreaseLevel")]
     HRESULT DecreaseLevel();
};
```

> [!Note]
> The return value is the first \[out\] parameter in the list of arguments in the service description; however, it is listed as the last parameter after translation.
> 
> All other parameters remain in the same order.

 

To provide the functionality of the service, implement this COM interface.

## Obtaining Information About an Endpoint

In the UPnP framework, endpoint information includes information about a request and its source. A device can examine this information in order to make a decision about the request.

Endpoint information is optionally available to the implemented service. The device host has access to endpoint information; however, the device host does not communicate the information to the implemented service by default. You can enable the device host to share the endpoint information with the implemented service by modifying the COM interface in the IDL file (produced by the Utl2idl tool). You can add an \[in\] parameter to each method that requires endpoint information. The additional \[in\] parameter must be the first one in the list of arguments, a pointer to an [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface, and explicitly named **punkRemoteEndpointInfo**. Modifications to the Service XML are not required, or recommended. The following example shows the new definition of the **PowerOn** method when it is amended so that it receives endpoint information:

"HRESULT PowerOn(\[in\] IUnknown \*punkRemoteEndpointInfo);"

A pointer to an endpoint information object, an [**IUPnPRemoteEndpointInfo**](/windows/desktop/api/Upnphost/nn-upnphost-iupnpremoteendpointinfo) interface, is passed through this new parameter by the device host. The **IUPnPRemoteEndpointInfo** interface provides three methods for accessing the endpoint information. You must call the appropriate method to get the endpoint information that is required by the service implementation.

As an alternative to manual modification of the COM interface, you can use the Utl2idl tool with the **-ci** switch. This switch causes the tool to add the endpoint information parameter to each of the methods in the COM interface. Using the **-ci** switch does not facilitate modification of individual methods. If endpoint information is not needed by all methods of an interface, you should add the parameter manually in order to produce the most efficient implementations.

## Implementing a Service Object

You must use the Utl2idl tool to translate each service description of a device.

An object that provides the functionality for a service is referred to as a [*service object*](s-gly.md). In addition to providing service functionality, service objects handle errors by using the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. For more information, see [Using the Device Host API with UPnP Technology](using-the-device-host-api-with-upnp-technology.md).

To ensure compatibility with Visual Basic, which does not support \[out\] parameters, the **direction**out**/direction** parameters in the service description are converted to \[in, out\] parameters in IDL. The server must free these \[in, out\] parameters.

## Implementing a Device Control Object

In addition to implementing service objects, you must implement a [*device control object*](d-gly.md). A device control object is the central point of management and control for the device's service objects. At registration time, the device control object is passed to the device host. When an event subscription or control request arrives for one of the device's services, the device host calls into this device control object to obtain the relevant service object. At that time, the device control object either creates an instance of the service object or returns the interface of an existing instance of the service object.

You can register a device description on multiple computers or multiple times on the same computer. Because the Unique Device Name (UDN) must be different for each instance of the device, the device host generates a unique UDN for each device and embedded device each time the device is registered. Use the UDN specified in the device description template to obtain the actual UDN generated by the device host and associated with the device. To unregister a device, you must use the ID provided by the UPnP framework when the device was registered.

Device control objects must implement the [**IUPnPDeviceControl**](/windows/desktop/api/Upnphost/nn-upnphost-iupnpdevicecontrol) interface. The device host invokes the [**IUPnPDeviceControl::Initialize**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpdevicecontrol-initialize) method of the device control object, passing in the UPnP-based device description that the device host previously published for the device and an initialization string that was specified at registration time (see [Registering a Hosted Device with the Device Host](registering-a-hosted-device-with-the-device-host.md)). From this device description, the device control object reads the UDNs assigned to each of the devices in the device tree. You can also use the [**IUPnPRegistrar::GetUniqueDeviceName**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-getuniquedevicename) method to obtain this information.

When the device host requires a pointer to a service object that implements a particular service, it invokes the [**IUPnPDeviceControl::GetServiceObject**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpdevicecontrol-getserviceobject) method on the device control object. The device host passes the UDN and the service ID of the service for which it is requesting a service object and the address of an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer at which the method is expected to return a pointer to the service object. The UDN parameter is necessary because the device control object manages services for the entire device tree, including nested devices. If the device host requests a nested device, **GetServiceObject** uses the UDN to identify it.

 

 