---
title: Wecutil.exe
description: Wecutil.exe is a Windows Event Collector utility that enables an administrator to create and manage subscriptions to events forwarded from remote event sources that support the WS-Management protocol.
ms.assetid: 93ce25df-f829-43b9-96f2-7f2f291d100e
ms.tgt_platform: multiple
keywords:
- Wecutil.exe
topic_type:
- apiref
api_name:
- Wecutil.exe
api_type:
- NA
ms.topic: reference
ms.date: 08/25/2025
---

# Wecutil.exe

Wecutil.exe is a Windows Event Collector utility that enables an administrator to create and manage subscriptions to events forwarded from remote event sources that support the WS-Management protocol. Commands, options, and option values are case-insensitive for this utility.

If you receive a message that says "The RPC server is unavailable" or "The interface is unknown" when you try to run wecutil, then you need to start the Windows Event Collector service (wecsvc). To start wecsvc, at an elevated command prompt type **net start wecsvc**.

## List existing subscriptions

The following syntax is used to list existing remote event subscriptions.

``` syntax
wecutil { es | enum-subscription }
```

If you use a script to get the names of the subscriptions from the output, you will need to bypass the UTF-8 BOM characters in the first line of the output. The following script shows an example of how you might skip the BOM characters.

``` syntax
setlocal enabledelayedexpansion

set bomskipped=
for /f %%i in ('wecutil es') do (
    set sub=%%i
    if not defined bomskipped (
        set sub=!sub:~3!
        set bomskipped=yes
    )
    echo !sub!
)
goto :eof

endlocal
```

## Get subscription configuration

The following syntax is used to display remote event subscription configuration data.

``` syntax
wecutil { gs | get-subscription } SUBSCRIPTION_ID [/f:VALUE 
[/u:VALUE] ...]
```

## Get Configuration Parameters

<dl> <dt>

**SUBSCRIPTION\_ID**

A string that uniquely identifies a subscription. This identifier is specified in the **SubscriptionId** element in the XML configuration file used to create the subscription.


**/f:*VALUE***

A value that specifies the output of the subscription configuration data. *VALUE* can be "XML" or "Terse", and the default is "Terse". If *VALUE* is "XML", then the output is printed in "XML" format. If *VALUE* is "Terse", then the output is printed in name-value pairs.


**/u: *VALUE***

A value that specifies whether the output is in Unicode format. *VALUE* can be "true" or "false". If *VALUE* is "true", then the output is in Unicode format, and if *VALUE* is "false", then the output is not in Unicode format.

</dd> </dl>

## Get subscription runtime status

The following syntax is used to display the subscription runtime status.

``` syntax
wecutil { gr | get-subscriptionruntimestatus } SUBSCRIPTION_ID
 [EVENT_SOURCE [EVENT_SOURCE] ...]
```

## Get Status Parameters

<dl> <dt>

**SUBSCRIPTION\_ID**

A string that uniquely identifies a subscription. This identifier is specified in the **SubscriptionId** element in the XML configuration file used to create the subscription.


**EVENT\_SOURCE**

A value that identifies a computer that is an event source for an event subscription. This value can be the fully qualified domain name for the computer, NetBIOS name, or IP address.

</dd> </dl>

## Set Subscription Configuration Information

The following syntax is used to set subscription configuration data by changing subscription parameters from the command line or using an XML configuration file.

``` syntax
wecutil { ss | set_subscription } SUBSCRIPTION_ID [/e:VALUE] 
[/esa:EVENT_SOURCE [/ese:VALUE] [/aes] [/res] [/un:USERNAME] [/up:PASSWORD]] 
[/d:DESCRIPTION] [/uri:URI] [/cm:CONFIGURATION_MODE] [/ex:DATE_TIME] 
[/q:QUERY] [/dia:DIALECT] [/tn:TRANSPORTNAME] [/tp:TRANSPORTPORT] [/dm:MODE] 
[/dmi:NUMBER] [/dmlt:MS] [/hi:MS] [/cf:FORMAT] [/l:LOCALE] [/ree:[VALUE]] 
[/lf:FILENAME] [/pn:PUBLISHER] [/hn:NAME] [/ct:TYPE] 
[/cun:USERNAME] [/cup:PASSWORD] 
[/ica:THUMBPRINTS] [/as:ALLOWED] [/ds:DENIED] [/adc:SDDL]

wecutil {ss | set_subscription } /c:CONGIG_FILE [/cun:USERNAME] 
[/cup:PASSWORD]
```

### Remarks

When an incorrect username or password is specified in the **wecutil ss** command, no error is reported until you view the runtime status of the subscription using the **wecutil gr** command.

## Set Configuration Parameters

**SUBSCRIPTION\_ID**

A string that uniquely identifies a subscription. This identifier is specified in the **SubscriptionId** element in the XML configuration file used to create the subscription.

**/c: *CONFIG\_FILE***

A value that specifies the path to the XML file that contains subscription configuration information. The path can be absolute or relative to the current directory. This parameter can only be used with the optional /cus and /cup parameters, and is mutually exclusive with all the other parameters.


**/e: *VALUE***

A value that determines whether to enable or disable the subscription. VALUE can be true or false. The default value is true, which enables the subscription.

> [!Note]  
> When you disable a collector initiated subscription, the event source becomes inactive instead of disabled. In a collector initiated subscription, you can disable an event source independent of the subscription.

 


**/d: *DESCRIPTION***

A value that specifies a description for the event subscription.


**/ex: *DATE\_TIME***

A value that specifies the subscription expiration time. *DATE\_TIME* is a value specified in standard XML or ISO8601 date-time format: "yyyy-MM-ddThh:mm:ss\[.sss\]\[Z\]" where "T" is the time separator and "Z" indicates UTC time. For example, if *DATE\_TIME* is "2007-01-12T01:20:00", then the subscription expiration time is January 12th, 2007, 01:20.


**/uri: *URI***

A value that specifies the type of events consumed by the subscription. The address of the event source computer along with the uniform resource identifier (URI) uniquely identifies the source of the events. The URI string is used for all event source addresses in the subscription.


**/cm: *CONFIGURATION\_MODE***

A value that specifies the configuration mode of the event subscription. *CONFIGURATION\_MODE* can be one of the following strings: "Normal", "Custom", "MinLatency", or "MinBandwidth". The [**EC\_SUBSCRIPTION\_CONFIGURATION\_MODE**](/windows/desktop/api/Evcoll/ne-evcoll-ec_subscription_configuration_mode) enumeration defines the configuration modes. The /dm, /dmi, /hi, and /dmlt parameters can only be specified if the configuration mode is set to Custom.


**/q: *QUERY***

A value that specifies the query string for the subscription. The format of this string can be different for different URI values and applies to all event sources in the subscription.


**/dia: *DIALECT***

A value that specifies the dialect the query string uses.


**/cf: *FORMAT***

A value that specifies the format of the returned events. *FORMAT* can be "Events" or "RenderedText". When the value is "RenderedText", the events are returned with the localized strings (such as event description strings) attached to the events. The default value of *FORMAT* is "RenderedText".


**/l: *LOCALE***

A value that specifies the locale for delivery of the localized strings in rendered text format. *LOCALE* is a language/country culture identifier, for example, "EN-us". This parameter is only valid when the /cf parameter is set to "RenderedText".


**/ree:\[*VALUE*\]**

A value that specifies which events are to be delivered for the subscription. *VALUE* can be true or false. When *VALUE* is true, all existing events are read from the subscription event sources. When *VALUE* is false, only future (arriving) events are delivered. The default is true when /ree is specified without a value, and the default is false if /ree is not specified.


**/lf: *FILENAME***

A value that specifies the local event log that is used to store events received from the event subscription.


**/pn: *PUBLISHER***

A value that specifies the event publisher (provider) name. It must be a publisher which owns or imports the log specified by the /lf parameter.


**/dm: *MODE***

A value that specifies the subscription delivery mode. *MODE* can be either push or pull. This option is only valid if the /cm parameter is set to Custom.


**/dmi: *NUMBER***

A value that specifies the maximum number of items for batched delivery in the event subscription. This option is only valid if the /cm parameter is set to Custom.


**/dmlt: *MS***

A value that specifies the maximum latency allowed in delivering a batch of events. MS is the number of milliseconds allowed. This parameter is only valid if the /cm parameter is set to Custom.


**/hi: *MS***

A value that specifies the heartbeat interval for the subscription. *MS* is the number of milliseconds used in the interval. This parameter is only valid if the /cm parameter is set to Custom.


**/tn: *TRANSPORTNAME***

A value that specifies the name of the transport used to connect to the remote event source computer.


**/esa: *EVENT\_SOURCE***

A value that specifies the address of an event source computer. *EVENT\_SOURCE* is a string that identifies an event source computer using the fully qualified domain name for the computer, NetBIOS name, or IP address. This parameter can be used with the /ese, /aes, /res, or /un and /up parameters.


**/ese: *VALUE***

A value that determines whether to enable or disable an event source. *VALUE* can be true or false. The default value is true, which enables the event source. This parameter is only used if the /esa parameter is used.


**/aes**

A value that adds the event source specified by the /esa parameter if the event source is not already part of the event subscription. If the computer specified by the /esa parameter is already a part of the subscription, then an error is displayed. This parameter is allowed only if the /esa parameter is used.


**/res**

A value that removes the event source specified by the /esa parameter if the event source is already part of the event subscription. If the computer specified by the /esa parameter is not part of the subscription, then an error is displayed. This parameter is allowed only if the /esa parameter is used.


**/un: *USERNAME***

A value that specifies the user name used in the credentials to connect to the event source specified in the /esa parameter. This parameter is allowed only if the /esa parameter is used.


**/up: *PASSWORD***

A value that specifies the password for the user name specified in the /un parameter. The user name and password credentials are used to connect to the event source specified in the /esa parameter. This parameter is allowed only if the /un parameter is used.


**/tp: *TRANSPORTPORT***

A value that specifies the port number used by the transport when connecting to a remote event source computer.


**/hn: *NAME***

A value that specifies the DNS name of the local computer. This name is used by remote event sources to push back events and must be used for push subscriptions only.


**/ct: *TYPE***

A value that specifies the credential type used for accessing remote event sources. *TYPE* can be "default", "negotiate", "digest", "basic", or "localmachine". The default is "default". These values are defined in the [**EC\_SUBSCRIPTION\_CREDENTIALS\_TYPE**](/windows/desktop/api/Evcoll/ne-evcoll-ec_subscription_credentials_type) enumeration.


**/cun: *USERNAME***

A value that sets the shared user credentials used for event sources that do not have their own user credentials.

> [!Note]  
> If this parameter is used with the /c option, then user name and password settings for individual event sources from the configuration file are ignored. If you want to use different credentials for a specific event source, you can override this value by specifying the /un and /up parameters for a specific event source on the command line of another set-subscription command.

 


**/cup: *PASSWORD***

A value that sets the user password for the shared user credentials. When *PASSWORD* is set to \* (asterisk), then the password is read from the console. This option is only valid when the /cun parameter is specified.


**/ica: *THUMBPRINTS***

A value that sets the list of issuer certificate thumb prints, in a comma-separated list.

> [!Note]  
> This option is specific to source initiated subscriptions only.

 


**/as: *ALLOWED***

A value that sets a comma-separated list of string that specify the DNS names of non-domain computers that are allowed to initiate subscriptions. The names can be specified using wildcards, such as "\*.mydomain.com". By default, this list is empty.

> [!Note]  
> This option is specific to source initiated subscriptions only.

 


**/ds: *DENIED***

A value that sets a comma-separated list of string that specify the DNS names of non-domain computers that are not allowed to initiate subscriptions. The names can be specified using wildcards, such as "\*.mydomain.com". By default, this list is empty.

> [!Note]  
> This option is specific to source initiated subscriptions only.

 


**/adc: *SDDL***

A value that sets a string, in SDDL format, that specifies which domain computers are allowed or not allowed to initiate subscriptions. The default is to allow all domain computers to initiate subscriptions.

> [!Note]  
> This option is specific to source initiated subscriptions only.

 

</dd> </dl>

## Create a New Subscription

The following syntax is used to create an event subscription for events on a remote computer.

``` syntax
wecutil {cs | create-subscription } CONFIGURATION_FILE [/cun:USERNAME]
[/cup:PASSWORD] 
```

### Remarks

When an incorrect username or password is specified in the **wecutil cs** command, no error is reported until you view the runtime status of the subscription using the **wecutil gr** command.

## Creation Parameters

<dl> <dt>

**CONFIGURATION\_FILE**

A value that specifies the path to the XML file that contains subscription configuration information. The path can be absolute or relative to the current directory.

The following XML is an example of a subscription configuration file that creates a collector initiated subscription to forward events from the Application event log of a remote computer to the ForwardedEvents log.


```XML
<Subscription xmlns="http://schemas.microsoft.com/2006/03/windows/events/subscription">
    <SubscriptionId>SampleCISubscription</SubscriptionId>
    <SubscriptionType>CollectorInitiated</SubscriptionType>
    <Description>Collector Initiated Subscription Sample</Description>
    <Enabled>true</Enabled>
    <Uri>http://schemas.microsoft.com/wbem/wsman/1/windows/EventLog</Uri>

    <!-- Use Normal (default), Custom, MinLatency, MinBandwidth -->
    <ConfigurationMode>Custom</ConfigurationMode>

    <Delivery Mode="Push">
        <Batching>
            <MaxItems>20</MaxItems>
            <MaxLatencyTime>60000</MaxLatencyTime>
        </Batching>
        <PushSettings>
            <HostName>thisMachine.myDomain.com</HostName>
            <Heartbeat Interval="60000"/>
        </PushSettings>
    </Delivery>

    <Expires>2010-01-01T00:00:00.000Z</Expires>

    <Query>
        <![CDATA[
            <QueryList>
                <Query Path="Application">
                    <Select>*</Select>
                </Query>
            </QueryList>
        ]]>
    </Query>

    <ReadExistingEvents>false</ReadExistingEvents>
    <TransportName>http</TransportName>
    <ContentFormat>RenderedText</ContentFormat>
    <Locale Language="en-US"/>
    <LogFile>ForwardedEvents</LogFile>
    <CredentialsType>Default</CredentialsType>

    <EventSources>
        <EventSource Enabled="true">
            <Address>mySource.myDomain.com</Address>
            <UserName>myUserName</UserName>
        </EventSource>
    </EventSources>
</Subscription>
```



The following XML is an example of a subscription configuration file that creates a source initiated subscription to forward events from the Application event log of a remote computer to the ForwardedEvents log.


```XML
<Subscription xmlns="http://schemas.microsoft.com/2006/03/windows/events/subscription">
    <SubscriptionId>SampleSISubscription</SubscriptionId>
    <SubscriptionType>SourceInitiated</SubscriptionType>
    <Description>Source Initiated Subscription Sample</Description>
    <Enabled>true</Enabled>
    <Uri>http://schemas.microsoft.com/wbem/wsman/1/windows/EventLog</Uri>

    <!-- Use Normal (default), Custom, MinLatency, MinBandwidth -->
    <ConfigurationMode>Custom</ConfigurationMode>

    <Delivery Mode="Push">
        <Batching>
            <MaxItems>1</MaxItems>
            <MaxLatencyTime>1000</MaxLatencyTime>
        </Batching>
        <PushSettings>
            <Heartbeat Interval="60000"/>
        </PushSettings>
    </Delivery>

    <Expires>2018-01-01T00:00:00.000Z</Expires>

    <Query>
        <![CDATA[
            <QueryList>
                <Query Path="Application">
                    <Select>Event[System/EventID='999']</Select>
                </Query>
            </QueryList>
        ]]>
    </Query>

    <ReadExistingEvents>true</ReadExistingEvents>
    <TransportName>http</TransportName>
    <ContentFormat>RenderedText</ContentFormat>
    <Locale Language="en-US"/>
    <LogFile>ForwardedEvents</LogFile>
    <AllowedSourceNonDomainComputers></AllowedSourceNonDomainComputers>
    <AllowedSourceDomainComputers>O:NSG:NSD:(A;;GA;;;DC)(A;;GA;;;NS)</AllowedSourceDomainComputers>
</Subscription>
```



> [!Note]  
> When creating a source initiated subscription, if **AllowedSourceDomainComputers**, **AllowedSourceNonDomainComputers**/**IssuerCAList**, **AllowedSubjectList**, and **DeniedSubjectList** are all empty, then a default will be provided for **AllowedSourceDomainComputers** - "O:NSG:NSD:(A;;GA;;;DC)(A;;GA;;;NS)". This SDDL default grants members of the Domain Computers domain group, as well as the local Network Service group (for the local forwarder), the ability to raise events for this subscription.

 


**/cun: *USERNAME***

A value that sets the shared user credentials used for event sources that do not have their own user credentials. This value applies to collector initiated subscriptions only.

> [!Note]  
> If this parameter is specified, then user name and password settings for individual event sources from the configuration file are ignored. If you want to use different credentials for a specific event source, you can override this value by specifying the /un and /up parameters for a specific event source on the command line of another set-subscription command.

 


**/cup: *PASSWORD***

A value that sets the user password for the shared user credentials. When *PASSWORD* is set to "\*" (asterisk), then the password is read from the console. This option is only valid when the /cun parameter is specified.

</dd> </dl>

## Delete a Subscription

The following syntax is used to delete an event subscription.

``` syntax
wecutil { ds | delete-subscription } SUBSCRIPTION_ID
```

## Deletion Parameters

<dl> <dt>

**SUBSCRIPTION\_ID**

A string that uniquely identifies a subscription. This identifier is specified in the **SubscriptionId** element in the XML configuration file used to create the subscription. The subscription identified in this parameter will be deleted.

</dd> </dl>

## Retry a subscription

The following syntax is used to retry an inactive subscription by attempting to reactivate all or specified event sources by establishing a connection to each event source and sending a remote subscription request to the event source. Disabled event sources are not retried.

``` syntax
wecutil { rs | retry-subscription } SUBSCRIPTION_ID 
[EVENT_SOURCE [EVENT_SOURCE] ...]
```

## Retry Parameters

<dl> <dt>

**SUBSCRIPTION\_ID**

A string that uniquely identifies a subscription. This identifier is specified in the **SubscriptionId** element in the XML configuration file used to create the subscription. The subscription identified in this parameter will be retried.


**EVENT\_SOURCE**

A value that identifies a computer that is an event source for an event subscription. This value can be the fully qualified domain name for the computer, NetBIOS name, or IP address.

</dd> </dl>

## Configure the Windows Event Collector Service

The following syntax is used to configure the Windows Event Collector service to ensure event subscriptions can be created and sustained through computer restarts. This includes the following procedure:

**To configure the Windows Event Collector service**

1.  Enable the ForwardedEvents channel if it is disabled.
2.  Delay the start of the Windows Event Collector service.
3.  Start the Windows Event Collector service if it is not running.

``` syntax
wecutil { qc | quick-config } /q:VALUE
```

## Configure Event Collector Parameters

<dl> <dt>

**/q: *VALUE***

A value that determines whether the quick-config command will prompt for confirmation. VALUE can be true or false. If VALUE is true, then the command will prompt for confirmation. The default value is false.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

 





