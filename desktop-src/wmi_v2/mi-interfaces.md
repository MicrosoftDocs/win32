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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MI Interfaces

WMI provides the following interfaces.

## In this section

<dl> <dt>

[**MI\_Application**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_application)
</dt> <dd>

Represents the initialized infrastructure.

</dd> <dt>

[**MI\_Application\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_close)
</dt> <dd>

Deinitializes the management infrastructure client API that was initialized through a call to [**MI\_Application\_Initialize**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_initializev1).

</dd> <dt>

[**MI\_Application\_Initialize**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_initializev1)
</dt> <dd>

Initializes an application so that it can make Management Infrastructure (MI) client API calls.

</dd> <dt>

[**MI\_Application\_NewClass**](/previous-versions/windows/desktop/api/mi/nf-mi-mi_application_newclass)
</dt> <dd>

Creates an [**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class) from an [**MI\_ClassDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_classdecl) structure.

</dd> <dt>

[**MI\_Application\_NewDeserializer**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newdeserializer)
</dt> <dd>

Creates a deserializer object that can then be used to convert a serialized object back into a class or instance.

</dd> <dt>

[**MI\_Application\_NewDestinationOptions**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newdestinationoptions)
</dt> <dd>

Creates an [**MI\_DestinationOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_destinationoptions) object that can be used with the [**MI\_Application\_NewSession**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newsession) function.

</dd> <dt>

[**MI\_Application\_NewHostedProvider**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newhostedprovider)
</dt> <dd>

Registers a hosted provider with the WMI engine on the local machine.

</dd> <dt>

[**MI\_Application\_NewInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newinstance)
</dt> <dd>

Creates a new [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) object to be passed to various MI operation APIs that require instances.

</dd> <dt>

[**MI\_Application\_NewInstanceFromClass**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newinstancefromclass)
</dt> <dd>

Creates a new [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) object based on a class object.

</dd> <dt>

[**MI\_Application\_NewOperationOptions**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newoperationoptions)
</dt> <dd>

Creates an [**MI\_OperationOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operationoptions) object that can be used with the operation functions on the [**MI\_Session**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_session) object.

</dd> <dt>

[**MI\_Application\_NewParameterSet**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newparameterset)
</dt> <dd>

Creates a new parameter set.

</dd> <dt>

[**MI\_Application\_NewSerializer**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newserializer)
</dt> <dd>

Retrieves a serializer object that can then be used to serialize instances and classes into various different formats.

</dd> <dt>

[**MI\_Application\_NewSession**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newsession)
</dt> <dd>

Creates a session used to share connections for a set of operations to a single destination.

</dd> <dt>

[**MI\_Application\_NewSubscriptionDeliveryOptions**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newsubscriptiondeliveryoptions)
</dt> <dd>

Creates an [**MI\_SubscriptionDeliveryOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_subscriptiondeliveryoptions) object that represents the configuration needed to carry out subscribe operations over certain protocols.

</dd> <dt>

[**MI\_CancelCallback**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Cancels an operation.

</dd> <dt>

[**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class)
</dt> <dd>

Represents the schema of an instance.

</dd> <dt>

[**MI\_Class\_Clone**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_clone)
</dt> <dd>

Clones an [**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class) object.

</dd> <dt>

[**MI\_Class\_Delete**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_delete)
</dt> <dd>

Deletes an [**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class) object.

</dd> <dt>

[**MI\_Class\_GetClassName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getclassname)
</dt> <dd>

Gets the class name of the specified class.

</dd> <dt>

[**MI\_Class\_GetClassQualifierSet**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getclassqualifierset)
</dt> <dd>

Gets the qualifier set that is associated with the specified class object.

</dd> <dt>

[**MI\_Class\_GetElement**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getelement)
</dt> <dd>

Gets all details of a specified named element from a class.

</dd> <dt>

[**MI\_Class\_GetElementAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getelementat)
</dt> <dd>

Gets details of a class element based on the element index.

</dd> <dt>

[**MI\_Class\_GetElementCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getelementcount)
</dt> <dd>

Gets the number of elements in a class.

</dd> <dt>

[**MI\_Class\_GetMethod**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getmethod)
</dt> <dd>

Gets details of a method based on the method name.

</dd> <dt>

[**MI\_Class\_GetMethodAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getmethodat)
</dt> <dd>

Gets details of a method based on the method index.

</dd> <dt>

[**MI\_Class\_GetMethodCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getmethodcount)
</dt> <dd>

Gets the number of methods in the class.

</dd> <dt>

[**MI\_Class\_GetNameSpace**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getnamespace)
</dt> <dd>

Gets the namespace name of the specified class.

</dd> <dt>

[**MI\_Class\_GetParentClass**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getparentclass)
</dt> <dd>

Gets the parent class for the specified class.

</dd> <dt>

[**MI\_Class\_GetParentClassName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getparentclassname)
</dt> <dd>

Gets the parent class name of the specified class.

</dd> <dt>

[**MI\_Class\_GetServerName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_class_getservername)
</dt> <dd>

Gets the name of the server from the specified class.

</dd> <dt>

[**MI\_Context\_Canceled**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_canceled)
</dt> <dd>

Determines whether the operation has been canceled. This function is reserved; instead, use the [**MI\_Context\_RegisterCancel**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_registercancel) function.

</dd> <dt>

[**MI\_Context\_ConstructInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_constructinstance)
</dt> <dd>

Initializes an MI class instance on the stack or as a member of a structure.

</dd> <dt>

[**MI\_Context\_ConstructParameters**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_constructparameters)
</dt> <dd>

A provider calls this function to initialize a parameter's instance.

</dd> <dt>

[**MI\_Context\_GetCustomOption**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_getcustomoption)
</dt> <dd>

Retrieves an option set by the client.

</dd> <dt>

[**MI\_Context\_GetCustomOptionAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_getcustomoptionat)
</dt> <dd>

Retrieves an option at a particular index that was set by the client.

</dd> <dt>

[**MI\_Context\_GetCustomOptionCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_getcustomoptioncount)
</dt> <dd>

Gets the number of custom options available to the provider.

</dd> <dt>

[**MI\_Context\_GetLocale**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_getlocale)
</dt> <dd>

Retrieves the requested locale information that the client specified for the operation.

</dd> <dt>

[**MI\_Context\_GetLocalSession**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_getlocalsession)
</dt> <dd>

Gets the local session ([**MI\_Session**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_session)) which allows the provider to perform CIM operations against the local server hosting the provider.

</dd> <dt>

[**MI\_Context\_GetNumberOption**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_getnumberoption)
</dt> <dd>

Gets the numeric option that the client sets, based on the operation name.

</dd> <dt>

[**MI\_Context\_GetStringOption**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_getstringoption)
</dt> <dd>

Gets the string option that the client sets, based on the operation name.

</dd> <dt>

[**MI\_Context\_NewDynamicInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_newdynamicinstance)
</dt> <dd>

Creates a new dynamic instance (weakly typed instance without a class declaration) of a class.

</dd> <dt>

[**MI\_Context\_NewInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_newinstance)
</dt> <dd>

Creates a new instance of a class given a class declaration.

</dd> <dt>

[**MI\_Context\_NewParameters**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_newparameters)
</dt> <dd>

Creates a new instance of a method given a method declaration.

</dd> <dt>

[**MI\_Context\_PostCimError**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_postcimerror)
</dt> <dd>

Posts a return code and an error message (in the form of a [**CIM\_Error**](https://msdn.microsoft.com/library/mt445938) object) to the server in response to a request.

</dd> <dt>

[**MI\_Context\_PostError**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_posterror)
</dt> <dd>

Providers call this function to post a return code to the client in response to a request.

</dd> <dt>

[**MI\_Context\_PostIndication**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_postindication)
</dt> <dd>

Posts an indication result to the server in response to a subscribe operation request.

</dd> <dt>

[**MI\_Context\_PostInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_postinstance)
</dt> <dd>

Posts an instance back to the client (through the server) in response to a request.

</dd> <dt>

[**MI\_Context\_PostResult**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_postresult)
</dt> <dd>

Posts the final terminating result code back to the client (through the server) in response to a request.

</dd> <dt>

[**MI\_Context\_PromptUser**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_promptuser)
</dt> <dd>

Sends a prompt message to the client querying whether to continue the operation or cancel it.

</dd> <dt>

[**MI\_Context\_RefuseUnload**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_refuseunload)
</dt> <dd>

Tells the provider infrastructure not to unload the provider.

</dd> <dt>

[**MI\_Context\_RegisterCancel**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_registercancel)
</dt> <dd>

Registers a callback that is invoked when the operation is canceled.

</dd> <dt>

[**MI\_Context\_RequestUnload**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_requestunload)
</dt> <dd>

Requests to unload the module or the provider.

</dd> <dt>

[**MI\_Context\_SetStringOption**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_setstringoption)
</dt> <dd>

Sets a context-specific option.

</dd> <dt>

[**MI\_Context\_ShouldContinue**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_shouldcontinue)
</dt> <dd>

Queries the client to determine if an operation should continue.

</dd> <dt>

[**MI\_Context\_ShouldProcess**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_shouldprocess)
</dt> <dd>

Queries the client to determine if an operation should continue.

</dd> <dt>

[**MI\_Context\_WriteCimError**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writecimerror)
</dt> <dd>

Sends a CIM (informative) error instance to the client.

</dd> <dt>

[**MI\_Context\_WriteDebug**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writedebug)
</dt> <dd>

Sends a debug message to the client.

</dd> <dt>

[**MI\_Context\_WriteError**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writeerror)
</dt> <dd>

Sends an error code and error message to the client.

</dd> <dt>

[**MI\_Context\_WriteMessage**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writemessage)
</dt> <dd>

Sends an operational message to the client.

</dd> <dt>

[**MI\_Context\_WriteProgress**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writeprogress)
</dt> <dd>

Sends a progress message to the client.

</dd> <dt>

[**MI\_Context\_WriteStreamParameter**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writestreamparameter)
</dt> <dd>

Sends streamed parameter data to the client for a method invocation.

</dd> <dt>

[**MI\_Context\_WriteVerbose**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writeverbose)
</dt> <dd>

Writes a verbose message to the client.

</dd> <dt>

[**MI\_Context\_WriteWarning**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writewarning)
</dt> <dd>

Writes a warning message to the client.

</dd> <dt>

[**MI\_Deserializer\_Class\_GetClassName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_deserializer_class_getclassname)
</dt> <dd>

Gets the class name from a serialized class buffer.

</dd> <dt>

[**MI\_Deserializer\_Class\_GetParentClassName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_deserializer_class_getparentclassname)
</dt> <dd>

Gets the parent class name from a serialized class buffer.

</dd> <dt>

[*MI\_Deserializer\_ClassObjectNeeded*](/previous-versions/windows/desktop/api/Mi/nc-mi-mi_deserializer_classobjectneeded)
</dt> <dd>

Used to provide requested class object during deserialization.

</dd> <dt>

[**MI\_Deserializer\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_deserializer_close)
</dt> <dd>

Closes a deserializer object and deletes any associated memory that is held within the deserializer.

</dd> <dt>

[**MI\_Deserializer\_DeserializeClass**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_deserializer_deserializeclass)
</dt> <dd>

Deserializes a serialized buffer into an [**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class) object.

</dd> <dt>

[**MI\_Deserializer\_DeserializeInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_deserializer_deserializeinstance)
</dt> <dd>

Deserializes a serialized buffer into a [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) object.

</dd> <dt>

[**MI\_Deserializer\_Instance\_GetClassName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_deserializer_instance_getclassname)
</dt> <dd>

Gets the class name associated with the serialized instance.

</dd> <dt>

[**MI\_DestinationOptions\_AddDestinationCredentials**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_adddestinationcredentials)
</dt> <dd>

Sets the credentials for talking to the destination.

</dd> <dt>

[**MI\_DestinationOptions\_AddProxyCredentials**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_addproxycredentials)
</dt> <dd>

Adds credentials to authenticate against a proxy.

</dd> <dt>

[**MI\_DestinationOptions\_Clone**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_clone)
</dt> <dd>

Creates a copy of a [**MI\_DestinationOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_destinationoptions) structure.

</dd> <dt>

[**MI\_DestinationOptions\_Delete**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_delete)
</dt> <dd>

Deletes the destination options structure created by using the [**MI\_Application\_NewDestinationOptions**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newdestinationoptions) or [**MI\_DestinationOptions\_Clone**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_clone) function.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertCACheck**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getcertcacheck)
</dt> <dd>

Gets the server certificate CA check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertCNCheck**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getcertcncheck)
</dt> <dd>

Gets the server certificate CN check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertRevocationCheck**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getcertrevocationcheck)
</dt> <dd>

Gets the server certificate's revocation check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getcredentialsat)
</dt> <dd>

Get the credentials at the specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getcredentialscount)
</dt> <dd>

Gets the number of previously added credentials.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsPasswordAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getcredentialspasswordat)
</dt> <dd>

Gets a credentials password based on a specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetDataLocale**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getdatalocale)
</dt> <dd>

Gets the data locale (as opposed to UI locale) set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_GetDestinationPort**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getdestinationport)
</dt> <dd>

Gets the default port for transport.

</dd> <dt>

[**MI\_DestinationOptions\_GetEncodePortInSPN**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getencodeportinspn)
</dt> <dd>

Gets the port's Service Principal Name encoding value.

</dd> <dt>

[**MI\_DestinationOptions\_GetHttpUrlPrefix**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_gethttpurlprefix)
</dt> <dd>

Gets the HTTP URL prefix.

</dd> <dt>

[**MI\_DestinationOptions\_GetImpersonationType**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getimpersonationtype)
</dt> <dd>

Gets the impersonation type.

</dd> <dt>

[**MI\_DestinationOptions\_GetMaxEnvelopeSize**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getmaxenvelopesize)
</dt> <dd>

Gets the maximum size of the packet sent to a server or received by the client from the server.

</dd> <dt>

[**MI\_DestinationOptions\_GetNumber**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getnumber)
</dt> <dd>

Gets a previously added custom number option.

</dd> <dt>

[**MI\_DestinationOptions\_GetOption**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getoption)
</dt> <dd>

Gets a previously added option value based on the option name.

</dd> <dt>

[**MI\_DestinationOptions\_GetOptionAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getoptionat)
</dt> <dd>

Gets a previously added option value based on the specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetOptionCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getoptioncount)
</dt> <dd>

Gets the number of options previously added.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketEncoding**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getpacketencoding)
</dt> <dd>

Gets the previously set packet encoding setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketIntegrity**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getpacketintegrity)
</dt> <dd>

Gets the packet integrity setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketPrivacy**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getpacketprivacy)
</dt> <dd>

Gets the packet privacy (encryption) setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetProxyType**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getproxytype)
</dt> <dd>

Gets the proxy type set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_GetString**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getstring)
</dt> <dd>

Gets a previously added custom string option.

</dd> <dt>

[**MI\_DestinationOptions\_GetTimeout**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_gettimeout)
</dt> <dd>

Gets the default options timeout value.

</dd> <dt>

[**MI\_DestinationOptions\_GetTransport**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_gettransport)
</dt> <dd>

Gets the transport setting that the client added.

</dd> <dt>

[**MI\_DestinationOptions\_GetUILocale**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_getuilocale)
</dt> <dd>

Gets the user interface locale set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertCACheck**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setcertcacheck)
</dt> <dd>

Enables or disables the CA certificate check for an SSL transport.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertCNCheck**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setcertcncheck)
</dt> <dd>

Enables or disables the certificate CN check when an SSL transport is used.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertRevocationCheck**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setcertrevocationcheck)
</dt> <dd>

Enables or disables the certificate revocation when communicating over SSL.

</dd> <dt>

[**MI\_DestinationOptions\_SetDataLocale**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setdatalocale)
</dt> <dd>

Sets the default data locale to use for operations.

</dd> <dt>

[**MI\_DestinationOptions\_SetDestinationPort**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setdestinationport)
</dt> <dd>

Set the port to use to communicate to the destination.

</dd> <dt>

[**MI\_DestinationOptions\_SetEncodePortInSPN**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setencodeportinspn)
</dt> <dd>

Enables or disables the encoding of the port number in the Service Principal Name when establishing a connection to a remote machine.

</dd> <dt>

[**MI\_DestinationOptions\_SetHttpUrlPrefix**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_sethttpurlprefix)
</dt> <dd>

Set the default HTTP URL prefix for transports that go over HTTP and HTTPS.

</dd> <dt>

[**MI\_DestinationOptions\_SetImpersonationType**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setimpersonationtype)
</dt> <dd>

Sets the impersonation type.

</dd> <dt>

[**MI\_DestinationOptions\_SetMaxEnvelopeSize**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setmaxenvelopesize)
</dt> <dd>

Sets the maximum packet size for transports.

</dd> <dt>

[**MI\_DestinationOptions\_SetNumber**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setnumber)
</dt> <dd>

Sets a custom numeric option value.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketEncoding**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setpacketencoding)
</dt> <dd>

Sets the encoding mechanism for certain protocol handles.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketIntegrity**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setpacketintegrity)
</dt> <dd>

Enables or disables packet integrity (signing) of a protocol connection.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketPrivacy**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setpacketprivacy)
</dt> <dd>

Enables or disables packet privacy (encryption).

</dd> <dt>

[**MI\_DestinationOptions\_SetProxyType**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setproxytype)
</dt> <dd>

Sets the type of proxy settings to use when communicating to a destination through a proxy.

</dd> <dt>

[**MI\_DestinationOptions\_SetString**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setstring)
</dt> <dd>

Sets a custom string option.

</dd> <dt>

[**MI\_DestinationOptions\_SetTimeout**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_settimeout)
</dt> <dd>

Sets the default options timeout value.

</dd> <dt>

[**MI\_DestinationOptions\_SetTransport**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_settransport)
</dt> <dd>

Sets the transport to be used to communicate with the destination machine.

</dd> <dt>

[**MI\_DestinationOptions\_SetUILocale**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_destinationoptions_setuilocale)
</dt> <dd>

Sets the default UI locale for operations.

</dd> <dt>

[**MI\_Filter\_Evaluate**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_filter_evaluate)
</dt> <dd>

The provider calls this function to evaluate an instance against a given filter.

</dd> <dt>

[**MI\_Filter\_GetExpression**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_filter_getexpression)
</dt> <dd>

Gets the filter language and expression.

</dd> <dt>

[**MI\_HostedProvider\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_hostedprovider_close)
</dt> <dd>

Close a hosted provider handle that was returned from [**MI\_Application\_NewHostedProvider**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newhostedprovider).

</dd> <dt>

[**MI\_HostedProvider\_GetApplication**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_hostedprovider_getapplication)
</dt> <dd>

Gets the top-level application handle from which the hosted provider handle was created.

</dd> <dt>

[**MI\_Instance\_AddElement**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_addelement)
</dt> <dd>

Adds a new property to a dynamic instance (supported only by dynamic instances whose schema may be extended at run time).

</dd> <dt>

[**MI\_Instance\_ClearElement**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_clearelement)
</dt> <dd>

Clears the value of the named element (CIM property) and sets it to **NULL**.

</dd> <dt>

[**MI\_Instance\_ClearElementAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_clearelementat)
</dt> <dd>

Clears the value of the element (CIM property) at the specified index and sets it to **NULL**.

</dd> <dt>

[**MI\_Instance\_Clone**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_clone)
</dt> <dd>

Creates a copy of the specified instance on the heap.

</dd> <dt>

[**MI\_Instance\_Delete**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_delete)
</dt> <dd>

Deletes an instance that was created on the heap or cloned from another instance.

</dd> <dt>

[**MI\_Instance\_Destruct**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_destruct)
</dt> <dd>

Deletes an instance that was created on the stack or as a member of a structure.

</dd> <dt>

[**MI\_Instance\_GetClass**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_getclass)
</dt> <dd>

Gets the [**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class) associated with an instance.

</dd> <dt>

[**MI\_Instance\_GetClassName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_getclassname)
</dt> <dd>

Gets the class name of the specified instance.

</dd> <dt>

[**MI\_Instance\_GetElement**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_getelement)
</dt> <dd>

Gets the value of the named element (CIM property).

</dd> <dt>

[**MI\_Instance\_GetElementAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_getelementat)
</dt> <dd>

Gets the value of the element (CIM property) at the specified index.

</dd> <dt>

[**MI\_Instance\_GetElementCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_getelementcount)
</dt> <dd>

Gets the number of elements in an instance.

</dd> <dt>

[**MI\_Instance\_GetNameSpace**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_getnamespace)
</dt> <dd>

Gets the namespace name of the specified instance.

</dd> <dt>

[**MI\_Instance\_GetServerName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_getservername)
</dt> <dd>

Gets the server name from the specified instance.

</dd> <dt>

[**MI\_Instance\_IsA**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_isa)
</dt> <dd>

Determines if the instance *self* is an instance of the class given by *classDecl*.

</dd> <dt>

[**MI\_Instance\_Normalize**](/previous-versions/windows/desktop/api/mi/nf-mi-mi_instance_normalize)
</dt> <dd>

Parses an [**MI\_Instance\_ExFT**](/previous-versions/windows/desktop/api/mi/ns-mi-_mi_instanceexft) structure and then retrieves the [**MI\_InstanceFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instanceft) function table.

</dd> <dt>

[**MI\_Instance\_SetElement**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_setelement)
</dt> <dd>

Set the value of the element with the given name in the given instance.

</dd> <dt>

[**MI\_Instance\_SetElementAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_setelementat)
</dt> <dd>

Set the value of the element at the given index of an instance.

</dd> <dt>

[**MI\_Instance\_SetNameSpace**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_setnamespace)
</dt> <dd>

Sets the namespace name of the specified instance.

</dd> <dt>

[**MI\_Instance\_SetServerName**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_setservername)
</dt> <dd>

Sets the server name of the specified instance.

</dd> <dt>

[**MI\_MethodDecl\_Invoke**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Calls the provider implementation of a CIM method represented by a [**MI\_MethodDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_methoddecl) structure.

</dd> <dt>

[**MI\_Module\_Load**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Loads the main provider module.

</dd> <dt>

[**MI\_Module\_Unload**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Unloads the main provider module.

</dd> <dt>

[**MI\_Operation\_Cancel**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operation_cancel)
</dt> <dd>

Cancels a running operation.

</dd> <dt>

[**MI\_Operation\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operation_close)
</dt> <dd>

Closes an operation handle.

</dd> <dt>

[**MI\_Operation\_GetClass**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operation_getclass)
</dt> <dd>

Gets a synchronous result for a class operation.

</dd> <dt>

[**MI\_Operation\_GetIndication**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operation_getindication)
</dt> <dd>

Get the synchronous results from a subscription.

</dd> <dt>

[**MI\_Operation\_GetInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operation_getinstance)
</dt> <dd>

Gets a synchronous result for an instance operation.

</dd> <dt>

[**MI\_Operation\_GetSession**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operation_getsession)
</dt> <dd>

Gets the session associated with an operation.

</dd> <dt>

[**MI\_OperationCallback\_Class**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Optional instance callback to get classes and class options from an operation.

</dd> <dt>

[**MI\_OperationCallback\_Indication**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Optional instance callback to get indication (subscribe) results from an operation.

</dd> <dt>

[**MI\_OperationCallback\_Instance**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Optional instance callback to get asynchronous results from an operation.

</dd> <dt>

[**MI\_OperationCallback\_PromptUser**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Optional callback to handle prompt user requests from the server.

</dd> <dt>

[**MI\_OperationCallback\_StreamedParameter**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Optional callback to get streamed parameter results from method invocation operations.

</dd> <dt>

[**MI\_OperationCallback\_WriteError**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Optional callback to receive write error messages from the server.

</dd> <dt>

[**MI\_OperationCallback\_WriteMessage**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Optional callback to receive write messages from the server.

</dd> <dt>

[**MI\_OperationCallback\_WriteProgress**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Optional callback to receive progress reports from the server.

</dd> <dt>

[**MI\_OperationOptions\_Clone**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_clone)
</dt> <dd>

Creates a copy of a [**MI\_OperationOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operationoptions) structure.

</dd> <dt>

[**MI\_OperationOptions\_Delete**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_delete)
</dt> <dd>

Deletes an option set and its associated memory.

</dd> <dt>

[**MI\_OperationOptions\_DisableChannel**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_disablechannel)
</dt> <dd>

Uses [**MI\_Context\_WriteMessage**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writemessage) to disable logging to the specified channel.

</dd> <dt>

[**MI\_OperationOptions\_EnableChannel**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_enablechannel)
</dt> <dd>

Uses [**MI\_Context\_WriteMessage**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_writemessage) to enable logging to the specified channel.

</dd> <dt>

[**MI\_OperationOptions\_GetEnabledChannels**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getenabledchannels)
</dt> <dd>

Gets the list of previously enabled channels.

</dd> <dt>

[**MI\_OperationOptions\_GetNumber**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getnumber)
</dt> <dd>

Gets a previously added custom number option.

</dd> <dt>

[**MI\_OperationOptions\_GetOption**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getoption)
</dt> <dd>

Gets a previously added option value based on the option name.

</dd> <dt>

[**MI\_OperationOptions\_GetOptionAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getoptionat)
</dt> <dd>

Gets a previously added option value based on the specified index.

</dd> <dt>

[**MI\_OperationOptions\_GetOptionCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getoptioncount)
</dt> <dd>

Gets the number of options previously added.

</dd> <dt>

[**MI\_OperationOptions\_GetPromptUserMode**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getpromptusermode)
</dt> <dd>

Gets the value that tells the server how to respond to a provider's call to [**MI\_Context\_PromptUser**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_promptuser).

</dd> <dt>

[**MI\_OperationOptions\_GetPromptUserRegularMode**](/previous-versions/windows/desktop/api/mi/nf-mi-mi_operationoptions_getpromptuserregularmode)
</dt> <dd>

Gets the value that tells the server how to respond to a provider's call to [**MI\_Context\_PromptUser**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_promptuser).

</dd> <dt>

[**MI\_OperationOptions\_GetProviderArchitecture**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getproviderarchitecture)
</dt> <dd>

Gets the provider architecture for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetResourceUri**](/previous-versions/windows/desktop/api/mi/nf-mi-mi_operationoptions_getresourceuri)
</dt> <dd>

Gets the resource URI being used for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetResourceUriPrefix**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getresourceuriprefix)
</dt> <dd>

Gets the resource URI prefix being used for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetString**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getstring)
</dt> <dd>

Gets a custom string option.

</dd> <dt>

[**MI\_OperationOptions\_GetTimeout**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_gettimeout)
</dt> <dd>

Gets the operation timeout value.

</dd> <dt>

[**MI\_OperationOptions\_GetUseMachineID**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getusemachineid)
</dt> <dd>

Gets the value that indicates whether to use machine identification information in the operation request.

</dd> <dt>

[**MI\_OperationOptions\_GetWriteErrorMode**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_getwriteerrormode)
</dt> <dd>

Sets the error reporting mode.

</dd> <dt>

[**MI\_OperationOptions\_SetCustomOption**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_setcustomoption)
</dt> <dd>

Sets a custom option for the operation.

</dd> <dt>

[**MI\_OperationOptions\_SetNumber**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_setnumber)
</dt> <dd>

Sets a custom number option value.

</dd> <dt>

[**MI\_OperationOptions\_SetPromptUserMode**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_setpromptusermode)
</dt> <dd>

Sets the value that tells the server how to respond to a provider's call to the [**MI\_Context\_PromptUser**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_promptuser) function.

</dd> <dt>

[**MI\_OperationOptions\_SetPromptUserRegularMode**](/previous-versions/windows/desktop/api/mi/nf-mi-mi_operationoptions_setpromptuserregularmode)
</dt> <dd>

Sets the value that tells the server how to respond to a provider's call to the [**MI\_Context\_PromptUser**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_context_promptuser) function.

</dd> <dt>

[**MI\_OperationOptions\_SetProviderArchitecture**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_setproviderarchitecture)
</dt> <dd>

Sets the provider architecture for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetResourceUri**](/previous-versions/windows/desktop/api/mi/nf-mi-mi_operationoptions_setresourceuri)
</dt> <dd>

Sets the resource URI to use for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetResourceUriPrefix**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_setresourceuriprefix)
</dt> <dd>

Sets the resource URI prefix to use for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetString**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_setstring)
</dt> <dd>

Sets a custom string option.

</dd> <dt>

[**MI\_OperationOptions\_SetTimeout**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_settimeout)
</dt> <dd>

Sets the operation timeout for a specific operation.

</dd> <dt>

[**MI\_OperationOptions\_SetUseMachineID**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_setusemachineid)
</dt> <dd>

Enables or disables the sending of machine identification information in the operation request.

</dd> <dt>

[**MI\_OperationOptions\_SetWriteErrorMode**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operationoptions_setwriteerrormode)
</dt> <dd>

Sets the error reporting mode.

</dd> <dt>

[**MI\_ParameterSet\_GetMethodReturnType**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_parameterset_getmethodreturntype)
</dt> <dd>

Gets the method return type and qualifier set for a specified parameter set.

</dd> <dt>

[**MI\_ParameterSet\_GetParameter**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_parameterset_getparameter)
</dt> <dd>

Gets a method's parameter information based on a parameter name.

</dd> <dt>

[**MI\_ParameterSet\_GetParameterAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_parameterset_getparameterat)
</dt> <dd>

Gets a method's parameter information at the specified index.

</dd> <dt>

[**MI\_ParameterSet\_GetParameterCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_parameterset_getparametercount)
</dt> <dd>

Gets the number of parameters in a method's parameter set.

</dd> <dt>

[**MI\_PropertySet\_AddElement**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_propertyset_addelement)
</dt> <dd>

Adds a name to the property list.

</dd> <dt>

[**MI\_PropertySet\_Clear**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_propertyset_clear)
</dt> <dd>

Removes all names from the property list. Afterwards, the count is zero. This allows property lists to be reused (without having to be destructed and reconstructed).

</dd> <dt>

[**MI\_PropertySet\_Clone**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_propertyset_clone)
</dt> <dd>

Creates a copy of the specified property set on the heap.

</dd> <dt>

[**MI\_PropertySet\_ContainsElement**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_propertyset_containselement)
</dt> <dd>

Determines whether the property list contains the specified property name.

</dd> <dt>

[**MI\_PropertySet\_Delete**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_propertyset_delete)
</dt> <dd>

Deletes the specified property list that was constructed on the heap.

</dd> <dt>

[**MI\_PropertySet\_Destruct**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_propertyset_destruct)
</dt> <dd>

Deletes the specified property list that was constructed on the stack.

</dd> <dt>

[**MI\_PropertySet\_GetElementAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_propertyset_getelementat)
</dt> <dd>

Gets the element of a property set at the specified index.

</dd> <dt>

[**MI\_PropertySet\_GetElementCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_propertyset_getelementcount)
</dt> <dd>

Gets the number of elements in the specified property set.

</dd> <dt>

[**MI\_ProviderFT\_AssociatorInstances**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Finds all CIM instances associated with a specified CIM instance.

</dd> <dt>

[**MI\_ProviderFT\_CreateInstance**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Create a single CIM instance in the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_DeleteInstance**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Delete a single CIM instance from the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_DisableIndications**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Disable indications delivery from the provider.

</dd> <dt>

[**MI\_ProviderFT\_EnableIndications**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Enable indications delivery from the provider.

</dd> <dt>

[**MI\_ProviderFT\_EnumerateInstances**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Enumerate instances of a CIM class in the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_GetInstance**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Get a single CIM instance from the provider.

</dd> <dt>

[**MI\_ProviderFT\_Invoke**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Calls a CIM extrinsic method on behalf of a requestor.

</dd> <dt>

[**MI\_ProviderFT\_Load**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Initialize the provider.

</dd> <dt>

[**MI\_ProviderFT\_ModifyInstance**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Modify an existing CIM instance in the target namespace. The instance must already exist.

</dd> <dt>

[**MI\_ProviderFT\_ReferenceInstances**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Enumerate association instances that refer to a particular CIM instance.

</dd> <dt>

[**MI\_ProviderFT\_Subscribe**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

Subscribe to indications.

</dd> <dt>

[**MI\_ProviderFT\_Unload**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

TBD

</dd> <dt>

[**MI\_ProviderFT\_Unsubscribe**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

unsubscribe from indications.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifier**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_qualifierset_getqualifier)
</dt> <dd>

Gets the qualifier information based on the given qualifier name.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifierAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_qualifierset_getqualifierat)
</dt> <dd>

Gets a qualifier at the specified index.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifierCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_qualifierset_getqualifiercount)
</dt> <dd>

Gets the number of qualifiers in a qualifier set.

</dd> <dt>

[**MI\_Serializer\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_serializer_close)
</dt> <dd>

Closes a serializer object and frees any internal memory associated with it.

</dd> <dt>

[**MI\_Serializer\_SerializeClass**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_serializer_serializeclass)
</dt> <dd>

Serializes an [**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class) into a buffer in the format specified when the serializer was created. Options can be passed into the flags to control if the class and all its parent classes are serialized, or just the child-most class.

</dd> <dt>

[**MI\_Serializer\_SerializeInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_serializer_serializeinstance)
</dt> <dd>

Serializes an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) into a buffer in the format specified when the serializer was created. Options can be passed into the flags to control if the class is also serialized into the buffer as well as the instance.

</dd> <dt>

[*MI\_Server\_GetSystemName*](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_server_getsystemname)
</dt> <dd>

Gets the system name for the server.

</dd> <dt>

[*MI\_Server\_GetVersion*](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_server_getversion)
</dt> <dd>

Gets the value of the MI\_VERSION macro used when generating the provider.

</dd> <dt>

[**MI\_Session\_AssociatorInstances**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_associatorinstances)
</dt> <dd>

Finds instances that are associated with the specific key instance.

</dd> <dt>

[**MI\_Session\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_close)
</dt> <dd>

Closes a session and releases all associated memory.

</dd> <dt>

[**MI\_Session\_CreateInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_createinstance)
</dt> <dd>

Creates an instance on the server that the session represents.

</dd> <dt>

[**MI\_Session\_DeleteInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_deleteinstance)
</dt> <dd>

Deletes an instance on the server represented by the session.

</dd> <dt>

[**MI\_Session\_EnumerateClasses**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_enumerateclasses)
</dt> <dd>

Enumerates the classes of a specified session.

</dd> <dt>

[**MI\_Session\_EnumerateInstances**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_enumerateinstances)
</dt> <dd>

Enumerate all instances (on the server represented by the session) that are associated with a class.

</dd> <dt>

[**MI\_Session\_GetApplication**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_getapplication)
</dt> <dd>

Gets the application handle that was used to create the specified session.

</dd> <dt>

[**MI\_Session\_GetClass**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_getclass)
</dt> <dd>

Gets an [**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class) declaration based on a specific class name.

</dd> <dt>

[**MI\_Session\_GetInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_getinstance)
</dt> <dd>

Gets the specified instance from the server represented by the session.

</dd> <dt>

[**MI\_Session\_Invoke**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_invoke)
</dt> <dd>

Invokes a method in the provider.

</dd> <dt>

[**MI\_Session\_ModifyInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_modifyinstance)
</dt> <dd>

Updates an existing instance in the server represented by the session.

</dd> <dt>

[**MI\_Session\_QueryInstances**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_queryinstances)
</dt> <dd>

Queries for a set of instances based on a query expression.

</dd> <dt>

[**MI\_Session\_ReferenceInstances**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_referenceinstances)
</dt> <dd>

Finds the association object that references the specified key instance.

</dd> <dt>

[**MI\_Session\_Subscribe**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_subscribe)
</dt> <dd>

Subscribes to an indication on the server represented by the session.

</dd> <dt>

[**MI\_Session\_TestConnection**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_testconnection)
</dt> <dd>

Tests a connection by communicating with the server represented by the session to determine whether it is responding.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_AddDeliveryCredentials**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_adddeliverycredentials)
</dt> <dd>

Sets a subscription option for delivery credentials to use when connecting back to the client to deliver a push indication result.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_Clone**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_clone)
</dt> <dd>

Creates a copy of a [**MI\_SubscriptionDeliveryOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_subscriptiondeliveryoptions) structure.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_Delete**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_delete)
</dt> <dd>

Deletes the specified subscription delivery options structure.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetBookmark**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getbookmark)
</dt> <dd>

Gets a previously set subscription bookmark.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getcredentialsat)
</dt> <dd>

Gets a previously added credential based on a specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getcredentialscount)
</dt> <dd>

Gets the number of previously added credentials.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsPasswordAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getcredentialspasswordat)
</dt> <dd>

Gets a previously added credential password based on a specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDateTime**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdatetime)
</dt> <dd>

Gets a previously set datetime option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryDestination**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdeliverydestination)
</dt> <dd>

Gets the previously set subscription delivery destination.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryPortNumber**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdeliveryportnumber)
</dt> <dd>

Gets the previously set delivery port number.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryRetryAttempts**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdeliveryretryattempts)
</dt> <dd>

Gets the number of delivery retry attempts.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryRetryInterval**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getdeliveryretryinterval)
</dt> <dd>

Gets the delivery retry interval—the amount of time to wait before retrying the delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetExpirationTime**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getexpirationtime)
</dt> <dd>

Gets the delivery expiration value (which can be expressed as a timestamp or an interval).

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetHeartbeatInterval**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getheartbeatinterval)
</dt> <dd>

Gets the delivery heartbeat interval.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetInterval**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getinterval)
</dt> <dd>

Gets the delivery interval for a specified option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetMaximumLatency**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getmaximumlatency)
</dt> <dd>

Gets the maximum amount of time that the server will hold a result before delivering it to the client.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetNumber**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getnumber)
</dt> <dd>

Gets the value of the named numeric option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOption**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getoption)
</dt> <dd>

Gets the value of the named option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOptionAt**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getoptionat)
</dt> <dd>

Gets the option at the specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOptionCount**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getoptioncount)
</dt> <dd>

Gets the number of previously set options.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetString**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_getstring)
</dt> <dd>

Gets the value of the named string option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetBookmark**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setbookmark)
</dt> <dd>

Sets a bookmark for subscription indication delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDateTime**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdatetime)
</dt> <dd>

Sets the value of a named DateTime option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryDestination**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdeliverydestination)
</dt> <dd>

Sets the destination endpoint that an indication will be delivered to.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryPortNumber**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdeliveryportnumber)
</dt> <dd>

Sets the subscription delivery port number.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryRetryAttempts**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdeliveryretryattempts)
</dt> <dd>

Sets the number of times a push delivery subscription will try to deliver a result.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryRetryInterval**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setdeliveryretryinterval)
</dt> <dd>

Sets the delivery retry interval for subscriptions that are for push delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetExpirationTime**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setexpirationtime)
</dt> <dd>

Sets the subscription expiration time (when the subscription will shut down).

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetHeartbeatInterval**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setheartbeatinterval)
</dt> <dd>

Sets the heartbeat interval.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetInterval**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setinterval)
</dt> <dd>

Sets the value of a named interval option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetMaximumLatency**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setmaximumlatency)
</dt> <dd>

Sets the maximum amount of time that the server will hold a result before delivering it to the client.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetNumber**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setnumber)
</dt> <dd>

Sets the value of a named numeric option that is not covered by a dedicated function.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetString**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_subscriptiondeliveryoptions_setstring)
</dt> <dd>

Sets the value of a named string option that is not covered by a dedicated function.

</dd> <dt>

[**MI\_Utilities\_CimErrorFromErrorCode**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_utilities_cimerrorfromerrorcode)
</dt> <dd>

Maps an operating-system specific error code to a CIM error instance.

</dd> <dt>

[**MI\_Utilities\_MapErrorToExtendedError**](/previous-versions/windows/desktop/api/Mi/)
</dt> <dd>

[**MI\_Utilities\_MapErrorToExtendedError**](/previous-versions/windows/desktop/api/Mi/) is not supported.

</dd> <dt>

[**MI\_Utilities\_MapErrorToMiErrorCategory**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_utilities_maperrortomierrorcategory)
</dt> <dd>

Maps an operating system specific error code to an error category.

</dd> </dl>

 

 




