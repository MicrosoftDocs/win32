---
title: MI Interfaces
description: WMI provides the following interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9B9C2BEF-02E8-4C7D-96DB-236BF6F9B1F9
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MI Interfaces

WMI provides the following interfaces.

## In this section

<dl> <dt>

[**MI\_Application**](/windows/previous-versions/Mi/ns-mi-_mi_application?branch=master)
</dt> <dd>

Represents the initialized infrastructure.

</dd> <dt>

[**MI\_Application\_Close**](/windows/previous-versions/Mi/nf-mi-mi_application_close?branch=master)
</dt> <dd>

Deinitializes the management infrastructure client API that was initialized through a call to [**MI\_Application\_Initialize**](/windows/previous-versions/Mi/nf-mi-mi_application_initializev1?branch=master).

</dd> <dt>

[**MI\_Application\_Initialize**](/windows/previous-versions/Mi/nf-mi-mi_application_initializev1?branch=master)
</dt> <dd>

Initializes an application so that it can make Management Infrastructure (MI) client API calls.

</dd> <dt>

[**MI\_Application\_NewClass**](/windows/previous-versions/mi/nf-mi-mi_application_newclass?branch=master)
</dt> <dd>

Creates an [**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master) from an [**MI\_ClassDecl**](/windows/previous-versions/Mi/ns-mi-_mi_classdecl?branch=master) structure.

</dd> <dt>

[**MI\_Application\_NewDeserializer**](/windows/previous-versions/Mi/nf-mi-mi_application_newdeserializer?branch=master)
</dt> <dd>

Creates a deserializer object that can then be used to convert a serialized object back into a class or instance.

</dd> <dt>

[**MI\_Application\_NewDestinationOptions**](/windows/previous-versions/Mi/nf-mi-mi_application_newdestinationoptions?branch=master)
</dt> <dd>

Creates an [**MI\_DestinationOptions**](/windows/previous-versions/Mi/ns-mi-_mi_destinationoptions?branch=master) object that can be used with the [**MI\_Application\_NewSession**](/windows/previous-versions/Mi/nf-mi-mi_application_newsession?branch=master) function.

</dd> <dt>

[**MI\_Application\_NewHostedProvider**](/windows/previous-versions/Mi/nf-mi-mi_application_newhostedprovider?branch=master)
</dt> <dd>

Registers a hosted provider with the WMI engine on the local machine.

</dd> <dt>

[**MI\_Application\_NewInstance**](/windows/previous-versions/Mi/nf-mi-mi_application_newinstance?branch=master)
</dt> <dd>

Creates a new [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) object to be passed to various MI operation APIs that require instances.

</dd> <dt>

[**MI\_Application\_NewInstanceFromClass**](/windows/previous-versions/Mi/nf-mi-mi_application_newinstancefromclass?branch=master)
</dt> <dd>

Creates a new [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) object based on a class object.

</dd> <dt>

[**MI\_Application\_NewOperationOptions**](/windows/previous-versions/Mi/nf-mi-mi_application_newoperationoptions?branch=master)
</dt> <dd>

Creates an [**MI\_OperationOptions**](/windows/previous-versions/Mi/ns-mi-_mi_operationoptions?branch=master) object that can be used with the operation functions on the [**MI\_Session**](/windows/previous-versions/Mi/ns-mi-_mi_session?branch=master) object.

</dd> <dt>

[**MI\_Application\_NewParameterSet**](/windows/previous-versions/Mi/nf-mi-mi_application_newparameterset?branch=master)
</dt> <dd>

Creates a new parameter set.

</dd> <dt>

[**MI\_Application\_NewSerializer**](/windows/previous-versions/Mi/nf-mi-mi_application_newserializer?branch=master)
</dt> <dd>

Retrieves a serializer object that can then be used to serialize instances and classes into various different formats.

</dd> <dt>

[**MI\_Application\_NewSession**](/windows/previous-versions/Mi/nf-mi-mi_application_newsession?branch=master)
</dt> <dd>

Creates a session used to share connections for a set of operations to a single destination.

</dd> <dt>

[**MI\_Application\_NewSubscriptionDeliveryOptions**](/windows/previous-versions/Mi/nf-mi-mi_application_newsubscriptiondeliveryoptions?branch=master)
</dt> <dd>

Creates an [**MI\_SubscriptionDeliveryOptions**](/windows/previous-versions/Mi/ns-mi-_mi_subscriptiondeliveryoptions?branch=master) object that represents the configuration needed to carry out subscribe operations over certain protocols.

</dd> <dt>

[**MI\_CancelCallback**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Cancels an operation.

</dd> <dt>

[**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master)
</dt> <dd>

Represents the schema of an instance.

</dd> <dt>

[**MI\_Class\_Clone**](/windows/previous-versions/Mi/nf-mi-mi_class_clone?branch=master)
</dt> <dd>

Clones an [**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master) object.

</dd> <dt>

[**MI\_Class\_Delete**](/windows/previous-versions/Mi/nf-mi-mi_class_delete?branch=master)
</dt> <dd>

Deletes an [**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master) object.

</dd> <dt>

[**MI\_Class\_GetClassName**](/windows/previous-versions/Mi/nf-mi-mi_class_getclassname?branch=master)
</dt> <dd>

Gets the class name of the specified class.

</dd> <dt>

[**MI\_Class\_GetClassQualifierSet**](/windows/previous-versions/Mi/nf-mi-mi_class_getclassqualifierset?branch=master)
</dt> <dd>

Gets the qualifier set that is associated with the specified class object.

</dd> <dt>

[**MI\_Class\_GetElement**](/windows/previous-versions/Mi/nf-mi-mi_class_getelement?branch=master)
</dt> <dd>

Gets all details of a specified named element from a class.

</dd> <dt>

[**MI\_Class\_GetElementAt**](/windows/previous-versions/Mi/nf-mi-mi_class_getelementat?branch=master)
</dt> <dd>

Gets details of a class element based on the element index.

</dd> <dt>

[**MI\_Class\_GetElementCount**](/windows/previous-versions/Mi/nf-mi-mi_class_getelementcount?branch=master)
</dt> <dd>

Gets the number of elements in a class.

</dd> <dt>

[**MI\_Class\_GetMethod**](/windows/previous-versions/Mi/nf-mi-mi_class_getmethod?branch=master)
</dt> <dd>

Gets details of a method based on the method name.

</dd> <dt>

[**MI\_Class\_GetMethodAt**](/windows/previous-versions/Mi/nf-mi-mi_class_getmethodat?branch=master)
</dt> <dd>

Gets details of a method based on the method index.

</dd> <dt>

[**MI\_Class\_GetMethodCount**](/windows/previous-versions/Mi/nf-mi-mi_class_getmethodcount?branch=master)
</dt> <dd>

Gets the number of methods in the class.

</dd> <dt>

[**MI\_Class\_GetNameSpace**](/windows/previous-versions/Mi/nf-mi-mi_class_getnamespace?branch=master)
</dt> <dd>

Gets the namespace name of the specified class.

</dd> <dt>

[**MI\_Class\_GetParentClass**](/windows/previous-versions/Mi/nf-mi-mi_class_getparentclass?branch=master)
</dt> <dd>

Gets the parent class for the specified class.

</dd> <dt>

[**MI\_Class\_GetParentClassName**](/windows/previous-versions/Mi/nf-mi-mi_class_getparentclassname?branch=master)
</dt> <dd>

Gets the parent class name of the specified class.

</dd> <dt>

[**MI\_Class\_GetServerName**](/windows/previous-versions/Mi/nf-mi-mi_class_getservername?branch=master)
</dt> <dd>

Gets the name of the server from the specified class.

</dd> <dt>

[**MI\_Context\_Canceled**](/windows/previous-versions/Mi/nf-mi-mi_context_canceled?branch=master)
</dt> <dd>

Determines whether the operation has been canceled. This function is reserved; instead, use the [**MI\_Context\_RegisterCancel**](/windows/previous-versions/Mi/nf-mi-mi_context_registercancel?branch=master) function.

</dd> <dt>

[**MI\_Context\_ConstructInstance**](/windows/previous-versions/Mi/nf-mi-mi_context_constructinstance?branch=master)
</dt> <dd>

Initializes an MI class instance on the stack or as a member of a structure.

</dd> <dt>

[**MI\_Context\_ConstructParameters**](/windows/previous-versions/Mi/nf-mi-mi_context_constructparameters?branch=master)
</dt> <dd>

A provider calls this function to initialize a parameter's instance.

</dd> <dt>

[**MI\_Context\_GetCustomOption**](/windows/previous-versions/Mi/nf-mi-mi_context_getcustomoption?branch=master)
</dt> <dd>

Retrieves an option set by the client.

</dd> <dt>

[**MI\_Context\_GetCustomOptionAt**](/windows/previous-versions/Mi/nf-mi-mi_context_getcustomoptionat?branch=master)
</dt> <dd>

Retrieves an option at a particular index that was set by the client.

</dd> <dt>

[**MI\_Context\_GetCustomOptionCount**](/windows/previous-versions/Mi/nf-mi-mi_context_getcustomoptioncount?branch=master)
</dt> <dd>

Gets the number of custom options available to the provider.

</dd> <dt>

[**MI\_Context\_GetLocale**](/windows/previous-versions/Mi/nf-mi-mi_context_getlocale?branch=master)
</dt> <dd>

Retrieves the requested locale information that the client specified for the operation.

</dd> <dt>

[**MI\_Context\_GetLocalSession**](/windows/previous-versions/Mi/nf-mi-mi_context_getlocalsession?branch=master)
</dt> <dd>

Gets the local session ([**MI\_Session**](/windows/previous-versions/Mi/ns-mi-_mi_session?branch=master)) which allows the provider to perform CIM operations against the local server hosting the provider.

</dd> <dt>

[**MI\_Context\_GetNumberOption**](/windows/previous-versions/Mi/nf-mi-mi_context_getnumberoption?branch=master)
</dt> <dd>

Gets the numeric option that the client sets, based on the operation name.

</dd> <dt>

[**MI\_Context\_GetStringOption**](/windows/previous-versions/Mi/nf-mi-mi_context_getstringoption?branch=master)
</dt> <dd>

Gets the string option that the client sets, based on the operation name.

</dd> <dt>

[**MI\_Context\_NewDynamicInstance**](/windows/previous-versions/Mi/nf-mi-mi_context_newdynamicinstance?branch=master)
</dt> <dd>

Creates a new dynamic instance (weakly typed instance without a class declaration) of a class.

</dd> <dt>

[**MI\_Context\_NewInstance**](/windows/previous-versions/Mi/nf-mi-mi_context_newinstance?branch=master)
</dt> <dd>

Creates a new instance of a class given a class declaration.

</dd> <dt>

[**MI\_Context\_NewParameters**](/windows/previous-versions/Mi/nf-mi-mi_context_newparameters?branch=master)
</dt> <dd>

Creates a new instance of a method given a method declaration.

</dd> <dt>

[**MI\_Context\_PostCimError**](/windows/previous-versions/Mi/nf-mi-mi_context_postcimerror?branch=master)
</dt> <dd>

Posts a return code and an error message (in the form of a [**CIM\_Error**](https://msdn.microsoft.com/library/mt445938) object) to the server in response to a request.

</dd> <dt>

[**MI\_Context\_PostError**](/windows/previous-versions/Mi/nf-mi-mi_context_posterror?branch=master)
</dt> <dd>

Providers call this function to post a return code to the client in response to a request.

</dd> <dt>

[**MI\_Context\_PostIndication**](/windows/previous-versions/Mi/nf-mi-mi_context_postindication?branch=master)
</dt> <dd>

Posts an indication result to the server in response to a subscribe operation request.

</dd> <dt>

[**MI\_Context\_PostInstance**](/windows/previous-versions/Mi/nf-mi-mi_context_postinstance?branch=master)
</dt> <dd>

Posts an instance back to the client (through the server) in response to a request.

</dd> <dt>

[**MI\_Context\_PostResult**](/windows/previous-versions/Mi/nf-mi-mi_context_postresult?branch=master)
</dt> <dd>

Posts the final terminating result code back to the client (through the server) in response to a request.

</dd> <dt>

[**MI\_Context\_PromptUser**](/windows/previous-versions/Mi/nf-mi-mi_context_promptuser?branch=master)
</dt> <dd>

Sends a prompt message to the client querying whether to continue the operation or cancel it.

</dd> <dt>

[**MI\_Context\_RefuseUnload**](/windows/previous-versions/Mi/nf-mi-mi_context_refuseunload?branch=master)
</dt> <dd>

Tells the provider infrastructure not to unload the provider.

</dd> <dt>

[**MI\_Context\_RegisterCancel**](/windows/previous-versions/Mi/nf-mi-mi_context_registercancel?branch=master)
</dt> <dd>

Registers a callback that is invoked when the operation is canceled.

</dd> <dt>

[**MI\_Context\_RequestUnload**](/windows/previous-versions/Mi/nf-mi-mi_context_requestunload?branch=master)
</dt> <dd>

Requests to unload the module or the provider.

</dd> <dt>

[**MI\_Context\_SetStringOption**](/windows/previous-versions/Mi/nf-mi-mi_context_setstringoption?branch=master)
</dt> <dd>

Sets a context-specific option.

</dd> <dt>

[**MI\_Context\_ShouldContinue**](/windows/previous-versions/Mi/nf-mi-mi_context_shouldcontinue?branch=master)
</dt> <dd>

Queries the client to determine if an operation should continue.

</dd> <dt>

[**MI\_Context\_ShouldProcess**](/windows/previous-versions/Mi/nf-mi-mi_context_shouldprocess?branch=master)
</dt> <dd>

Queries the client to determine if an operation should continue.

</dd> <dt>

[**MI\_Context\_WriteCimError**](/windows/previous-versions/Mi/nf-mi-mi_context_writecimerror?branch=master)
</dt> <dd>

Sends a CIM (informative) error instance to the client.

</dd> <dt>

[**MI\_Context\_WriteDebug**](/windows/previous-versions/Mi/nf-mi-mi_context_writedebug?branch=master)
</dt> <dd>

Sends a debug message to the client.

</dd> <dt>

[**MI\_Context\_WriteError**](/windows/previous-versions/Mi/nf-mi-mi_context_writeerror?branch=master)
</dt> <dd>

Sends an error code and error message to the client.

</dd> <dt>

[**MI\_Context\_WriteMessage**](/windows/previous-versions/Mi/nf-mi-mi_context_writemessage?branch=master)
</dt> <dd>

Sends an operational message to the client.

</dd> <dt>

[**MI\_Context\_WriteProgress**](/windows/previous-versions/Mi/nf-mi-mi_context_writeprogress?branch=master)
</dt> <dd>

Sends a progress message to the client.

</dd> <dt>

[**MI\_Context\_WriteStreamParameter**](/windows/previous-versions/Mi/nf-mi-mi_context_writestreamparameter?branch=master)
</dt> <dd>

Sends streamed parameter data to the client for a method invocation.

</dd> <dt>

[**MI\_Context\_WriteVerbose**](/windows/previous-versions/Mi/nf-mi-mi_context_writeverbose?branch=master)
</dt> <dd>

Writes a verbose message to the client.

</dd> <dt>

[**MI\_Context\_WriteWarning**](/windows/previous-versions/Mi/nf-mi-mi_context_writewarning?branch=master)
</dt> <dd>

Writes a warning message to the client.

</dd> <dt>

[**MI\_Deserializer\_Class\_GetClassName**](/windows/previous-versions/Mi/nf-mi-mi_deserializer_class_getclassname?branch=master)
</dt> <dd>

Gets the class name from a serialized class buffer.

</dd> <dt>

[**MI\_Deserializer\_Class\_GetParentClassName**](/windows/previous-versions/Mi/nf-mi-mi_deserializer_class_getparentclassname?branch=master)
</dt> <dd>

Gets the parent class name from a serialized class buffer.

</dd> <dt>

[*MI\_Deserializer\_ClassObjectNeeded*](/windows/previous-versions/Mi/nc-mi-mi_deserializer_classobjectneeded?branch=master)
</dt> <dd>

Used to provide requested class object during deserialization.

</dd> <dt>

[**MI\_Deserializer\_Close**](/windows/previous-versions/Mi/nf-mi-mi_deserializer_close?branch=master)
</dt> <dd>

Closes a deserializer object and deletes any associated memory that is held within the deserializer.

</dd> <dt>

[**MI\_Deserializer\_DeserializeClass**](/windows/previous-versions/Mi/nf-mi-mi_deserializer_deserializeclass?branch=master)
</dt> <dd>

Deserializes a serialized buffer into an [**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master) object.

</dd> <dt>

[**MI\_Deserializer\_DeserializeInstance**](/windows/previous-versions/Mi/nf-mi-mi_deserializer_deserializeinstance?branch=master)
</dt> <dd>

Deserializes a serialized buffer into a [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) object.

</dd> <dt>

[**MI\_Deserializer\_Instance\_GetClassName**](/windows/previous-versions/Mi/nf-mi-mi_deserializer_instance_getclassname?branch=master)
</dt> <dd>

Gets the class name associated with the serialized instance.

</dd> <dt>

[**MI\_DestinationOptions\_AddDestinationCredentials**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_adddestinationcredentials?branch=master)
</dt> <dd>

Sets the credentials for talking to the destination.

</dd> <dt>

[**MI\_DestinationOptions\_AddProxyCredentials**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_addproxycredentials?branch=master)
</dt> <dd>

Adds credentials to authenticate against a proxy.

</dd> <dt>

[**MI\_DestinationOptions\_Clone**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_clone?branch=master)
</dt> <dd>

Creates a copy of a [**MI\_DestinationOptions**](/windows/previous-versions/Mi/ns-mi-_mi_destinationoptions?branch=master) structure.

</dd> <dt>

[**MI\_DestinationOptions\_Delete**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_delete?branch=master)
</dt> <dd>

Deletes the destination options structure created by using the [**MI\_Application\_NewDestinationOptions**](/windows/previous-versions/Mi/nf-mi-mi_application_newdestinationoptions?branch=master) or [**MI\_DestinationOptions\_Clone**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_clone?branch=master) function.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertCACheck**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getcertcacheck?branch=master)
</dt> <dd>

Gets the server certificate CA check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertCNCheck**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getcertcncheck?branch=master)
</dt> <dd>

Gets the server certificate CN check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertRevocationCheck**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getcertrevocationcheck?branch=master)
</dt> <dd>

Gets the server certificate's revocation check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsAt**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getcredentialsat?branch=master)
</dt> <dd>

Get the credentials at the specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsCount**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getcredentialscount?branch=master)
</dt> <dd>

Gets the number of previously added credentials.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsPasswordAt**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getcredentialspasswordat?branch=master)
</dt> <dd>

Gets a credentials password based on a specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetDataLocale**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getdatalocale?branch=master)
</dt> <dd>

Gets the data locale (as opposed to UI locale) set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_GetDestinationPort**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getdestinationport?branch=master)
</dt> <dd>

Gets the default port for transport.

</dd> <dt>

[**MI\_DestinationOptions\_GetEncodePortInSPN**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getencodeportinspn?branch=master)
</dt> <dd>

Gets the port's Service Principal Name encoding value.

</dd> <dt>

[**MI\_DestinationOptions\_GetHttpUrlPrefix**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_gethttpurlprefix?branch=master)
</dt> <dd>

Gets the HTTP URL prefix.

</dd> <dt>

[**MI\_DestinationOptions\_GetImpersonationType**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getimpersonationtype?branch=master)
</dt> <dd>

Gets the impersonation type.

</dd> <dt>

[**MI\_DestinationOptions\_GetMaxEnvelopeSize**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getmaxenvelopesize?branch=master)
</dt> <dd>

Gets the maximum size of the packet sent to a server or received by the client from the server.

</dd> <dt>

[**MI\_DestinationOptions\_GetNumber**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getnumber?branch=master)
</dt> <dd>

Gets a previously added custom number option.

</dd> <dt>

[**MI\_DestinationOptions\_GetOption**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getoption?branch=master)
</dt> <dd>

Gets a previously added option value based on the option name.

</dd> <dt>

[**MI\_DestinationOptions\_GetOptionAt**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getoptionat?branch=master)
</dt> <dd>

Gets a previously added option value based on the specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetOptionCount**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getoptioncount?branch=master)
</dt> <dd>

Gets the number of options previously added.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketEncoding**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getpacketencoding?branch=master)
</dt> <dd>

Gets the previously set packet encoding setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketIntegrity**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getpacketintegrity?branch=master)
</dt> <dd>

Gets the packet integrity setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketPrivacy**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getpacketprivacy?branch=master)
</dt> <dd>

Gets the packet privacy (encryption) setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetProxyType**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getproxytype?branch=master)
</dt> <dd>

Gets the proxy type set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_GetString**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getstring?branch=master)
</dt> <dd>

Gets a previously added custom string option.

</dd> <dt>

[**MI\_DestinationOptions\_GetTimeout**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_gettimeout?branch=master)
</dt> <dd>

Gets the default options timeout value.

</dd> <dt>

[**MI\_DestinationOptions\_GetTransport**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_gettransport?branch=master)
</dt> <dd>

Gets the transport setting that the client added.

</dd> <dt>

[**MI\_DestinationOptions\_GetUILocale**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_getuilocale?branch=master)
</dt> <dd>

Gets the user interface locale set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertCACheck**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setcertcacheck?branch=master)
</dt> <dd>

Enables or disables the CA certificate check for an SSL transport.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertCNCheck**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setcertcncheck?branch=master)
</dt> <dd>

Enables or disables the certificate CN check when an SSL transport is used.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertRevocationCheck**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setcertrevocationcheck?branch=master)
</dt> <dd>

Enables or disables the certificate revocation when communicating over SSL.

</dd> <dt>

[**MI\_DestinationOptions\_SetDataLocale**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setdatalocale?branch=master)
</dt> <dd>

Sets the default data locale to use for operations.

</dd> <dt>

[**MI\_DestinationOptions\_SetDestinationPort**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setdestinationport?branch=master)
</dt> <dd>

Set the port to use to communicate to the destination.

</dd> <dt>

[**MI\_DestinationOptions\_SetEncodePortInSPN**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setencodeportinspn?branch=master)
</dt> <dd>

Enables or disables the encoding of the port number in the Service Principal Name when establishing a connection to a remote machine.

</dd> <dt>

[**MI\_DestinationOptions\_SetHttpUrlPrefix**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_sethttpurlprefix?branch=master)
</dt> <dd>

Set the default HTTP URL prefix for transports that go over HTTP and HTTPS.

</dd> <dt>

[**MI\_DestinationOptions\_SetImpersonationType**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setimpersonationtype?branch=master)
</dt> <dd>

Sets the impersonation type.

</dd> <dt>

[**MI\_DestinationOptions\_SetMaxEnvelopeSize**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setmaxenvelopesize?branch=master)
</dt> <dd>

Sets the maximum packet size for transports.

</dd> <dt>

[**MI\_DestinationOptions\_SetNumber**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setnumber?branch=master)
</dt> <dd>

Sets a custom numeric option value.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketEncoding**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setpacketencoding?branch=master)
</dt> <dd>

Sets the encoding mechanism for certain protocol handles.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketIntegrity**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setpacketintegrity?branch=master)
</dt> <dd>

Enables or disables packet integrity (signing) of a protocol connection.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketPrivacy**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setpacketprivacy?branch=master)
</dt> <dd>

Enables or disables packet privacy (encryption).

</dd> <dt>

[**MI\_DestinationOptions\_SetProxyType**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setproxytype?branch=master)
</dt> <dd>

Sets the type of proxy settings to use when communicating to a destination through a proxy.

</dd> <dt>

[**MI\_DestinationOptions\_SetString**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setstring?branch=master)
</dt> <dd>

Sets a custom string option.

</dd> <dt>

[**MI\_DestinationOptions\_SetTimeout**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_settimeout?branch=master)
</dt> <dd>

Sets the default options timeout value.

</dd> <dt>

[**MI\_DestinationOptions\_SetTransport**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_settransport?branch=master)
</dt> <dd>

Sets the transport to be used to communicate with the destination machine.

</dd> <dt>

[**MI\_DestinationOptions\_SetUILocale**](/windows/previous-versions/Mi/nf-mi-mi_destinationoptions_setuilocale?branch=master)
</dt> <dd>

Sets the default UI locale for operations.

</dd> <dt>

[**MI\_Filter\_Evaluate**](/windows/previous-versions/Mi/nf-mi-mi_filter_evaluate?branch=master)
</dt> <dd>

The provider calls this function to evaluate an instance against a given filter.

</dd> <dt>

[**MI\_Filter\_GetExpression**](/windows/previous-versions/Mi/nf-mi-mi_filter_getexpression?branch=master)
</dt> <dd>

Gets the filter language and expression.

</dd> <dt>

[**MI\_HostedProvider\_Close**](/windows/previous-versions/Mi/nf-mi-mi_hostedprovider_close?branch=master)
</dt> <dd>

Close a hosted provider handle that was returned from [**MI\_Application\_NewHostedProvider**](/windows/previous-versions/Mi/nf-mi-mi_application_newhostedprovider?branch=master).

</dd> <dt>

[**MI\_HostedProvider\_GetApplication**](/windows/previous-versions/Mi/nf-mi-mi_hostedprovider_getapplication?branch=master)
</dt> <dd>

Gets the top-level application handle from which the hosted provider handle was created.

</dd> <dt>

[**MI\_Instance\_AddElement**](/windows/previous-versions/Mi/nf-mi-mi_instance_addelement?branch=master)
</dt> <dd>

Adds a new property to a dynamic instance (supported only by dynamic instances whose schema may be extended at run time).

</dd> <dt>

[**MI\_Instance\_ClearElement**](/windows/previous-versions/Mi/nf-mi-mi_instance_clearelement?branch=master)
</dt> <dd>

Clears the value of the named element (CIM property) and sets it to **NULL**.

</dd> <dt>

[**MI\_Instance\_ClearElementAt**](/windows/previous-versions/Mi/nf-mi-mi_instance_clearelementat?branch=master)
</dt> <dd>

Clears the value of the element (CIM property) at the specified index and sets it to **NULL**.

</dd> <dt>

[**MI\_Instance\_Clone**](/windows/previous-versions/Mi/nf-mi-mi_instance_clone?branch=master)
</dt> <dd>

Creates a copy of the specified instance on the heap.

</dd> <dt>

[**MI\_Instance\_Delete**](/windows/previous-versions/Mi/nf-mi-mi_instance_delete?branch=master)
</dt> <dd>

Deletes an instance that was created on the heap or cloned from another instance.

</dd> <dt>

[**MI\_Instance\_Destruct**](/windows/previous-versions/Mi/nf-mi-mi_instance_destruct?branch=master)
</dt> <dd>

Deletes an instance that was created on the stack or as a member of a structure.

</dd> <dt>

[**MI\_Instance\_GetClass**](/windows/previous-versions/Mi/nf-mi-mi_instance_getclass?branch=master)
</dt> <dd>

Gets the [**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master) associated with an instance.

</dd> <dt>

[**MI\_Instance\_GetClassName**](/windows/previous-versions/Mi/nf-mi-mi_instance_getclassname?branch=master)
</dt> <dd>

Gets the class name of the specified instance.

</dd> <dt>

[**MI\_Instance\_GetElement**](/windows/previous-versions/Mi/nf-mi-mi_instance_getelement?branch=master)
</dt> <dd>

Gets the value of the named element (CIM property).

</dd> <dt>

[**MI\_Instance\_GetElementAt**](/windows/previous-versions/Mi/nf-mi-mi_instance_getelementat?branch=master)
</dt> <dd>

Gets the value of the element (CIM property) at the specified index.

</dd> <dt>

[**MI\_Instance\_GetElementCount**](/windows/previous-versions/Mi/nf-mi-mi_instance_getelementcount?branch=master)
</dt> <dd>

Gets the number of elements in an instance.

</dd> <dt>

[**MI\_Instance\_GetNameSpace**](/windows/previous-versions/Mi/nf-mi-mi_instance_getnamespace?branch=master)
</dt> <dd>

Gets the namespace name of the specified instance.

</dd> <dt>

[**MI\_Instance\_GetServerName**](/windows/previous-versions/Mi/nf-mi-mi_instance_getservername?branch=master)
</dt> <dd>

Gets the server name from the specified instance.

</dd> <dt>

[**MI\_Instance\_IsA**](/windows/previous-versions/Mi/nf-mi-mi_instance_isa?branch=master)
</dt> <dd>

Determines if the instance *self* is an instance of the class given by *classDecl*.

</dd> <dt>

[**MI\_Instance\_Normalize**](/windows/previous-versions/mi/nf-mi-mi_instance_normalize?branch=master)
</dt> <dd>

Parses an [**MI\_Instance\_ExFT**](/windows/previous-versions/mi/ns-mi-_mi_instanceexft?branch=master) structure and then retrieves the [**MI\_InstanceFT**](/windows/previous-versions/Mi/ns-mi-_mi_instanceft?branch=master) function table.

</dd> <dt>

[**MI\_Instance\_SetElement**](/windows/previous-versions/Mi/nf-mi-mi_instance_setelement?branch=master)
</dt> <dd>

Set the value of the element with the given name in the given instance.

</dd> <dt>

[**MI\_Instance\_SetElementAt**](/windows/previous-versions/Mi/nf-mi-mi_instance_setelementat?branch=master)
</dt> <dd>

Set the value of the element at the given index of an instance.

</dd> <dt>

[**MI\_Instance\_SetNameSpace**](/windows/previous-versions/Mi/nf-mi-mi_instance_setnamespace?branch=master)
</dt> <dd>

Sets the namespace name of the specified instance.

</dd> <dt>

[**MI\_Instance\_SetServerName**](/windows/previous-versions/Mi/nf-mi-mi_instance_setservername?branch=master)
</dt> <dd>

Sets the server name of the specified instance.

</dd> <dt>

[**MI\_MethodDecl\_Invoke**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Calls the provider implementation of a CIM method represented by a [**MI\_MethodDecl**](/windows/previous-versions/Mi/ns-mi-_mi_methoddecl?branch=master) structure.

</dd> <dt>

[**MI\_Module\_Load**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Loads the main provider module.

</dd> <dt>

[**MI\_Module\_Unload**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Unloads the main provider module.

</dd> <dt>

[**MI\_Operation\_Cancel**](/windows/previous-versions/Mi/nf-mi-mi_operation_cancel?branch=master)
</dt> <dd>

Cancels a running operation.

</dd> <dt>

[**MI\_Operation\_Close**](/windows/previous-versions/Mi/nf-mi-mi_operation_close?branch=master)
</dt> <dd>

Closes an operation handle.

</dd> <dt>

[**MI\_Operation\_GetClass**](/windows/previous-versions/Mi/nf-mi-mi_operation_getclass?branch=master)
</dt> <dd>

Gets a synchronous result for a class operation.

</dd> <dt>

[**MI\_Operation\_GetIndication**](/windows/previous-versions/Mi/nf-mi-mi_operation_getindication?branch=master)
</dt> <dd>

Get the synchronous results from a subscription.

</dd> <dt>

[**MI\_Operation\_GetInstance**](/windows/previous-versions/Mi/nf-mi-mi_operation_getinstance?branch=master)
</dt> <dd>

Gets a synchronous result for an instance operation.

</dd> <dt>

[**MI\_Operation\_GetSession**](/windows/previous-versions/Mi/nf-mi-mi_operation_getsession?branch=master)
</dt> <dd>

Gets the session associated with an operation.

</dd> <dt>

[**MI\_OperationCallback\_Class**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Optional instance callback to get classes and class options from an operation.

</dd> <dt>

[**MI\_OperationCallback\_Indication**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Optional instance callback to get indication (subscribe) results from an operation.

</dd> <dt>

[**MI\_OperationCallback\_Instance**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Optional instance callback to get asynchronous results from an operation.

</dd> <dt>

[**MI\_OperationCallback\_PromptUser**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Optional callback to handle prompt user requests from the server.

</dd> <dt>

[**MI\_OperationCallback\_StreamedParameter**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Optional callback to get streamed parameter results from method invocation operations.

</dd> <dt>

[**MI\_OperationCallback\_WriteError**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Optional callback to receive write error messages from the server.

</dd> <dt>

[**MI\_OperationCallback\_WriteMessage**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Optional callback to receive write messages from the server.

</dd> <dt>

[**MI\_OperationCallback\_WriteProgress**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Optional callback to receive progress reports from the server.

</dd> <dt>

[**MI\_OperationOptions\_Clone**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_clone?branch=master)
</dt> <dd>

Creates a copy of a [**MI\_OperationOptions**](/windows/previous-versions/Mi/ns-mi-_mi_operationoptions?branch=master) structure.

</dd> <dt>

[**MI\_OperationOptions\_Delete**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_delete?branch=master)
</dt> <dd>

Deletes an option set and its associated memory.

</dd> <dt>

[**MI\_OperationOptions\_DisableChannel**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_disablechannel?branch=master)
</dt> <dd>

Uses [**MI\_Context\_WriteMessage**](/windows/previous-versions/Mi/nf-mi-mi_context_writemessage?branch=master) to disable logging to the specified channel.

</dd> <dt>

[**MI\_OperationOptions\_EnableChannel**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_enablechannel?branch=master)
</dt> <dd>

Uses [**MI\_Context\_WriteMessage**](/windows/previous-versions/Mi/nf-mi-mi_context_writemessage?branch=master) to enable logging to the specified channel.

</dd> <dt>

[**MI\_OperationOptions\_GetEnabledChannels**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getenabledchannels?branch=master)
</dt> <dd>

Gets the list of previously enabled channels.

</dd> <dt>

[**MI\_OperationOptions\_GetNumber**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getnumber?branch=master)
</dt> <dd>

Gets a previously added custom number option.

</dd> <dt>

[**MI\_OperationOptions\_GetOption**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getoption?branch=master)
</dt> <dd>

Gets a previously added option value based on the option name.

</dd> <dt>

[**MI\_OperationOptions\_GetOptionAt**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getoptionat?branch=master)
</dt> <dd>

Gets a previously added option value based on the specified index.

</dd> <dt>

[**MI\_OperationOptions\_GetOptionCount**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getoptioncount?branch=master)
</dt> <dd>

Gets the number of options previously added.

</dd> <dt>

[**MI\_OperationOptions\_GetPromptUserMode**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getpromptusermode?branch=master)
</dt> <dd>

Gets the value that tells the server how to respond to a provider's call to [**MI\_Context\_PromptUser**](/windows/previous-versions/Mi/nf-mi-mi_context_promptuser?branch=master).

</dd> <dt>

[**MI\_OperationOptions\_GetPromptUserRegularMode**](/windows/previous-versions/mi/nf-mi-mi_operationoptions_getpromptuserregularmode?branch=master)
</dt> <dd>

Gets the value that tells the server how to respond to a provider's call to [**MI\_Context\_PromptUser**](/windows/previous-versions/Mi/nf-mi-mi_context_promptuser?branch=master).

</dd> <dt>

[**MI\_OperationOptions\_GetProviderArchitecture**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getproviderarchitecture?branch=master)
</dt> <dd>

Gets the provider architecture for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetResourceUri**](/windows/previous-versions/mi/nf-mi-mi_operationoptions_getresourceuri?branch=master)
</dt> <dd>

Gets the resource URI being used for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetResourceUriPrefix**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getresourceuriprefix?branch=master)
</dt> <dd>

Gets the resource URI prefix being used for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetString**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getstring?branch=master)
</dt> <dd>

Gets a custom string option.

</dd> <dt>

[**MI\_OperationOptions\_GetTimeout**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_gettimeout?branch=master)
</dt> <dd>

Gets the operation timeout value.

</dd> <dt>

[**MI\_OperationOptions\_GetUseMachineID**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getusemachineid?branch=master)
</dt> <dd>

Gets the value that indicates whether to use machine identification information in the operation request.

</dd> <dt>

[**MI\_OperationOptions\_GetWriteErrorMode**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_getwriteerrormode?branch=master)
</dt> <dd>

Sets the error reporting mode.

</dd> <dt>

[**MI\_OperationOptions\_SetCustomOption**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_setcustomoption?branch=master)
</dt> <dd>

Sets a custom option for the operation.

</dd> <dt>

[**MI\_OperationOptions\_SetNumber**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_setnumber?branch=master)
</dt> <dd>

Sets a custom number option value.

</dd> <dt>

[**MI\_OperationOptions\_SetPromptUserMode**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_setpromptusermode?branch=master)
</dt> <dd>

Sets the value that tells the server how to respond to a provider's call to the [**MI\_Context\_PromptUser**](/windows/previous-versions/Mi/nf-mi-mi_context_promptuser?branch=master) function.

</dd> <dt>

[**MI\_OperationOptions\_SetPromptUserRegularMode**](/windows/previous-versions/mi/nf-mi-mi_operationoptions_setpromptuserregularmode?branch=master)
</dt> <dd>

Sets the value that tells the server how to respond to a provider's call to the [**MI\_Context\_PromptUser**](/windows/previous-versions/Mi/nf-mi-mi_context_promptuser?branch=master) function.

</dd> <dt>

[**MI\_OperationOptions\_SetProviderArchitecture**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_setproviderarchitecture?branch=master)
</dt> <dd>

Sets the provider architecture for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetResourceUri**](/windows/previous-versions/mi/nf-mi-mi_operationoptions_setresourceuri?branch=master)
</dt> <dd>

Sets the resource URI to use for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetResourceUriPrefix**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_setresourceuriprefix?branch=master)
</dt> <dd>

Sets the resource URI prefix to use for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetString**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_setstring?branch=master)
</dt> <dd>

Sets a custom string option.

</dd> <dt>

[**MI\_OperationOptions\_SetTimeout**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_settimeout?branch=master)
</dt> <dd>

Sets the operation timeout for a specific operation.

</dd> <dt>

[**MI\_OperationOptions\_SetUseMachineID**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_setusemachineid?branch=master)
</dt> <dd>

Enables or disables the sending of machine identification information in the operation request.

</dd> <dt>

[**MI\_OperationOptions\_SetWriteErrorMode**](/windows/previous-versions/Mi/nf-mi-mi_operationoptions_setwriteerrormode?branch=master)
</dt> <dd>

Sets the error reporting mode.

</dd> <dt>

[**MI\_ParameterSet\_GetMethodReturnType**](/windows/previous-versions/Mi/nf-mi-mi_parameterset_getmethodreturntype?branch=master)
</dt> <dd>

Gets the method return type and qualifier set for a specified parameter set.

</dd> <dt>

[**MI\_ParameterSet\_GetParameter**](/windows/previous-versions/Mi/nf-mi-mi_parameterset_getparameter?branch=master)
</dt> <dd>

Gets a method's parameter information based on a parameter name.

</dd> <dt>

[**MI\_ParameterSet\_GetParameterAt**](/windows/previous-versions/Mi/nf-mi-mi_parameterset_getparameterat?branch=master)
</dt> <dd>

Gets a method's parameter information at the specified index.

</dd> <dt>

[**MI\_ParameterSet\_GetParameterCount**](/windows/previous-versions/Mi/nf-mi-mi_parameterset_getparametercount?branch=master)
</dt> <dd>

Gets the number of parameters in a method's parameter set.

</dd> <dt>

[**MI\_PropertySet\_AddElement**](/windows/previous-versions/Mi/nf-mi-mi_propertyset_addelement?branch=master)
</dt> <dd>

Adds a name to the property list.

</dd> <dt>

[**MI\_PropertySet\_Clear**](/windows/previous-versions/Mi/nf-mi-mi_propertyset_clear?branch=master)
</dt> <dd>

Removes all names from the property list. Afterwards, the count is zero. This allows property lists to be reused (without having to be destructed and reconstructed).

</dd> <dt>

[**MI\_PropertySet\_Clone**](/windows/previous-versions/Mi/nf-mi-mi_propertyset_clone?branch=master)
</dt> <dd>

Creates a copy of the specified property set on the heap.

</dd> <dt>

[**MI\_PropertySet\_ContainsElement**](/windows/previous-versions/Mi/nf-mi-mi_propertyset_containselement?branch=master)
</dt> <dd>

Determines whether the property list contains the specified property name.

</dd> <dt>

[**MI\_PropertySet\_Delete**](/windows/previous-versions/Mi/nf-mi-mi_propertyset_delete?branch=master)
</dt> <dd>

Deletes the specified property list that was constructed on the heap.

</dd> <dt>

[**MI\_PropertySet\_Destruct**](/windows/previous-versions/Mi/nf-mi-mi_propertyset_destruct?branch=master)
</dt> <dd>

Deletes the specified property list that was constructed on the stack.

</dd> <dt>

[**MI\_PropertySet\_GetElementAt**](/windows/previous-versions/Mi/nf-mi-mi_propertyset_getelementat?branch=master)
</dt> <dd>

Gets the element of a property set at the specified index.

</dd> <dt>

[**MI\_PropertySet\_GetElementCount**](/windows/previous-versions/Mi/nf-mi-mi_propertyset_getelementcount?branch=master)
</dt> <dd>

Gets the number of elements in the specified property set.

</dd> <dt>

[**MI\_ProviderFT\_AssociatorInstances**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Finds all CIM instances associated with a specified CIM instance.

</dd> <dt>

[**MI\_ProviderFT\_CreateInstance**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Create a single CIM instance in the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_DeleteInstance**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Delete a single CIM instance from the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_DisableIndications**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Disable indications delivery from the provider.

</dd> <dt>

[**MI\_ProviderFT\_EnableIndications**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Enable indications delivery from the provider.

</dd> <dt>

[**MI\_ProviderFT\_EnumerateInstances**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Enumerate instances of a CIM class in the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_GetInstance**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Get a single CIM instance from the provider.

</dd> <dt>

[**MI\_ProviderFT\_Invoke**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Calls a CIM extrinsic method on behalf of a requestor.

</dd> <dt>

[**MI\_ProviderFT\_Load**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Initialize the provider.

</dd> <dt>

[**MI\_ProviderFT\_ModifyInstance**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Modify an existing CIM instance in the target namespace. The instance must already exist.

</dd> <dt>

[**MI\_ProviderFT\_ReferenceInstances**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Enumerate association instances that refer to a particular CIM instance.

</dd> <dt>

[**MI\_ProviderFT\_Subscribe**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

Subscribe to indications.

</dd> <dt>

[**MI\_ProviderFT\_Unload**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**MI\_ProviderFT\_Unsubscribe**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

unsubscribe from indications.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifier**](/windows/previous-versions/Mi/nf-mi-mi_qualifierset_getqualifier?branch=master)
</dt> <dd>

Gets the qualifier information based on the given qualifier name.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifierAt**](/windows/previous-versions/Mi/nf-mi-mi_qualifierset_getqualifierat?branch=master)
</dt> <dd>

Gets a qualifier at the specified index.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifierCount**](/windows/previous-versions/Mi/nf-mi-mi_qualifierset_getqualifiercount?branch=master)
</dt> <dd>

Gets the number of qualifiers in a qualifier set.

</dd> <dt>

[**MI\_Serializer\_Close**](/windows/previous-versions/Mi/nf-mi-mi_serializer_close?branch=master)
</dt> <dd>

Closes a serializer object and frees any internal memory associated with it.

</dd> <dt>

[**MI\_Serializer\_SerializeClass**](/windows/previous-versions/Mi/nf-mi-mi_serializer_serializeclass?branch=master)
</dt> <dd>

Serializes an [**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master) into a buffer in the format specified when the serializer was created. Options can be passed into the flags to control if the class and all its parent classes are serialized, or just the child-most class.

</dd> <dt>

[**MI\_Serializer\_SerializeInstance**](/windows/previous-versions/Mi/nf-mi-mi_serializer_serializeinstance?branch=master)
</dt> <dd>

Serializes an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) into a buffer in the format specified when the serializer was created. Options can be passed into the flags to control if the class is also serialized into the buffer as well as the instance.

</dd> <dt>

[*MI\_Server\_GetSystemName*](/windows/previous-versions/Mi/nf-mi-mi_server_getsystemname?branch=master)
</dt> <dd>

Gets the system name for the server.

</dd> <dt>

[*MI\_Server\_GetVersion*](/windows/previous-versions/Mi/nf-mi-mi_server_getversion?branch=master)
</dt> <dd>

Gets the value of the MI\_VERSION macro used when generating the provider.

</dd> <dt>

[**MI\_Session\_AssociatorInstances**](/windows/previous-versions/Mi/nf-mi-mi_session_associatorinstances?branch=master)
</dt> <dd>

Finds instances that are associated with the specific key instance.

</dd> <dt>

[**MI\_Session\_Close**](/windows/previous-versions/Mi/nf-mi-mi_session_close?branch=master)
</dt> <dd>

Closes a session and releases all associated memory.

</dd> <dt>

[**MI\_Session\_CreateInstance**](/windows/previous-versions/Mi/nf-mi-mi_session_createinstance?branch=master)
</dt> <dd>

Creates an instance on the server that the session represents.

</dd> <dt>

[**MI\_Session\_DeleteInstance**](/windows/previous-versions/Mi/nf-mi-mi_session_deleteinstance?branch=master)
</dt> <dd>

Deletes an instance on the server represented by the session.

</dd> <dt>

[**MI\_Session\_EnumerateClasses**](/windows/previous-versions/Mi/nf-mi-mi_session_enumerateclasses?branch=master)
</dt> <dd>

Enumerates the classes of a specified session.

</dd> <dt>

[**MI\_Session\_EnumerateInstances**](/windows/previous-versions/Mi/nf-mi-mi_session_enumerateinstances?branch=master)
</dt> <dd>

Enumerate all instances (on the server represented by the session) that are associated with a class.

</dd> <dt>

[**MI\_Session\_GetApplication**](/windows/previous-versions/Mi/nf-mi-mi_session_getapplication?branch=master)
</dt> <dd>

Gets the application handle that was used to create the specified session.

</dd> <dt>

[**MI\_Session\_GetClass**](/windows/previous-versions/Mi/nf-mi-mi_session_getclass?branch=master)
</dt> <dd>

Gets an [**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master) declaration based on a specific class name.

</dd> <dt>

[**MI\_Session\_GetInstance**](/windows/previous-versions/Mi/nf-mi-mi_session_getinstance?branch=master)
</dt> <dd>

Gets the specified instance from the server represented by the session.

</dd> <dt>

[**MI\_Session\_Invoke**](/windows/previous-versions/Mi/nf-mi-mi_session_invoke?branch=master)
</dt> <dd>

Invokes a method in the provider.

</dd> <dt>

[**MI\_Session\_ModifyInstance**](/windows/previous-versions/Mi/nf-mi-mi_session_modifyinstance?branch=master)
</dt> <dd>

Updates an existing instance in the server represented by the session.

</dd> <dt>

[**MI\_Session\_QueryInstances**](/windows/previous-versions/Mi/nf-mi-mi_session_queryinstances?branch=master)
</dt> <dd>

Queries for a set of instances based on a query expression.

</dd> <dt>

[**MI\_Session\_ReferenceInstances**](/windows/previous-versions/Mi/nf-mi-mi_session_referenceinstances?branch=master)
</dt> <dd>

Finds the association object that references the specified key instance.

</dd> <dt>

[**MI\_Session\_Subscribe**](/windows/previous-versions/Mi/nf-mi-mi_session_subscribe?branch=master)
</dt> <dd>

Subscribes to an indication on the server represented by the session.

</dd> <dt>

[**MI\_Session\_TestConnection**](/windows/previous-versions/Mi/nf-mi-mi_session_testconnection?branch=master)
</dt> <dd>

Tests a connection by communicating with the server represented by the session to determine whether it is responding.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_AddDeliveryCredentials**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_adddeliverycredentials?branch=master)
</dt> <dd>

Sets a subscription option for delivery credentials to use when connecting back to the client to deliver a push indication result.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_Clone**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_clone?branch=master)
</dt> <dd>

Creates a copy of a [**MI\_SubscriptionDeliveryOptions**](/windows/previous-versions/Mi/ns-mi-_mi_subscriptiondeliveryoptions?branch=master) structure.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_Delete**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_delete?branch=master)
</dt> <dd>

Deletes the specified subscription delivery options structure.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetBookmark**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getbookmark?branch=master)
</dt> <dd>

Gets a previously set subscription bookmark.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsAt**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getcredentialsat?branch=master)
</dt> <dd>

Gets a previously added credential based on a specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsCount**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getcredentialscount?branch=master)
</dt> <dd>

Gets the number of previously added credentials.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsPasswordAt**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getcredentialspasswordat?branch=master)
</dt> <dd>

Gets a previously added credential password based on a specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDateTime**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdatetime?branch=master)
</dt> <dd>

Gets a previously set datetime option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryDestination**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdeliverydestination?branch=master)
</dt> <dd>

Gets the previously set subscription delivery destination.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryPortNumber**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdeliveryportnumber?branch=master)
</dt> <dd>

Gets the previously set delivery port number.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryRetryAttempts**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdeliveryretryattempts?branch=master)
</dt> <dd>

Gets the number of delivery retry attempts.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryRetryInterval**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdeliveryretryinterval?branch=master)
</dt> <dd>

Gets the delivery retry interval—the amount of time to wait before retrying the delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetExpirationTime**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getexpirationtime?branch=master)
</dt> <dd>

Gets the delivery expiration value (which can be expressed as a timestamp or an interval).

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetHeartbeatInterval**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getheartbeatinterval?branch=master)
</dt> <dd>

Gets the delivery heartbeat interval.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetInterval**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getinterval?branch=master)
</dt> <dd>

Gets the delivery interval for a specified option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetMaximumLatency**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getmaximumlatency?branch=master)
</dt> <dd>

Gets the maximum amount of time that the server will hold a result before delivering it to the client.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetNumber**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getnumber?branch=master)
</dt> <dd>

Gets the value of the named numeric option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOption**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getoption?branch=master)
</dt> <dd>

Gets the value of the named option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOptionAt**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getoptionat?branch=master)
</dt> <dd>

Gets the option at the specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOptionCount**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getoptioncount?branch=master)
</dt> <dd>

Gets the number of previously set options.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetString**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_getstring?branch=master)
</dt> <dd>

Gets the value of the named string option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetBookmark**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setbookmark?branch=master)
</dt> <dd>

Sets a bookmark for subscription indication delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDateTime**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdatetime?branch=master)
</dt> <dd>

Sets the value of a named DateTime option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryDestination**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdeliverydestination?branch=master)
</dt> <dd>

Sets the destination endpoint that an indication will be delivered to.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryPortNumber**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdeliveryportnumber?branch=master)
</dt> <dd>

Sets the subscription delivery port number.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryRetryAttempts**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdeliveryretryattempts?branch=master)
</dt> <dd>

Sets the number of times a push delivery subscription will try to deliver a result.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryRetryInterval**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdeliveryretryinterval?branch=master)
</dt> <dd>

Sets the delivery retry interval for subscriptions that are for push delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetExpirationTime**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setexpirationtime?branch=master)
</dt> <dd>

Sets the subscription expiration time (when the subscription will shut down).

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetHeartbeatInterval**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setheartbeatinterval?branch=master)
</dt> <dd>

Sets the heartbeat interval.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetInterval**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setinterval?branch=master)
</dt> <dd>

Sets the value of a named interval option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetMaximumLatency**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setmaximumlatency?branch=master)
</dt> <dd>

Sets the maximum amount of time that the server will hold a result before delivering it to the client.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetNumber**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setnumber?branch=master)
</dt> <dd>

Sets the value of a named numeric option that is not covered by a dedicated function.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetString**](/windows/previous-versions/Mi/nf-mi-mi_subscriptiondeliveryoptions_setstring?branch=master)
</dt> <dd>

Sets the value of a named string option that is not covered by a dedicated function.

</dd> <dt>

[**MI\_Utilities\_CimErrorFromErrorCode**](/windows/previous-versions/Mi/nf-mi-mi_utilities_cimerrorfromerrorcode?branch=master)
</dt> <dd>

Maps an operating-system specific error code to a CIM error instance.

</dd> <dt>

[**MI\_Utilities\_MapErrorToExtendedError**](/windows/previous-versions/Mi/?branch=master)
</dt> <dd>

[**MI\_Utilities\_MapErrorToExtendedError**](/windows/previous-versions/Mi/?branch=master) is not supported.

</dd> <dt>

[**MI\_Utilities\_MapErrorToMiErrorCategory**](/windows/previous-versions/Mi/nf-mi-mi_utilities_maperrortomierrorcategory?branch=master)
</dt> <dd>

Maps an operating system specific error code to an error category.

</dd> </dl>

 

 




