---
title: MI Interfaces
description: WMI provides the following interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9B9C2BEF-02E8-4C7D-96DB-236BF6F9B1F9'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# MI Interfaces

WMI provides the following interfaces.

## In this section

<dl> <dt>

[**MI\_Application**](mi-application.md)
</dt> <dd>

Represents the initialized infrastructure.

</dd> <dt>

[**MI\_Application\_Close**](mi-application-close.md)
</dt> <dd>

Deinitializes the management infrastructure client API that was initialized through a call to [**MI\_Application\_Initialize**](mi-application-initialize.md).

</dd> <dt>

[**MI\_Application\_Initialize**](mi-application-initialize.md)
</dt> <dd>

Initializes an application so that it can make Management Infrastructure (MI) client API calls.

</dd> <dt>

[**MI\_Application\_NewClass**](mi-application-newclass.md)
</dt> <dd>

Creates an [**MI\_Class**](mi-class.md) from an [**MI\_ClassDecl**](mi-classdecl.md) structure.

</dd> <dt>

[**MI\_Application\_NewDeserializer**](mi-application-newdeserializer.md)
</dt> <dd>

Creates a deserializer object that can then be used to convert a serialized object back into a class or instance.

</dd> <dt>

[**MI\_Application\_NewDestinationOptions**](mi-application-newdestinationoptions.md)
</dt> <dd>

Creates an [**MI\_DestinationOptions**](mi-destinationoptions.md) object that can be used with the [**MI\_Application\_NewSession**](mi-application-newsession.md) function.

</dd> <dt>

[**MI\_Application\_NewHostedProvider**](mi-application-newhostedprovider.md)
</dt> <dd>

Registers a hosted provider with the WMI engine on the local machine.

</dd> <dt>

[**MI\_Application\_NewInstance**](mi-application-newinstance.md)
</dt> <dd>

Creates a new [**MI\_Instance**](mi-instance.md) object to be passed to various MI operation APIs that require instances.

</dd> <dt>

[**MI\_Application\_NewInstanceFromClass**](mi-application-newinstancefromclass.md)
</dt> <dd>

Creates a new [**MI\_Instance**](mi-instance.md) object based on a class object.

</dd> <dt>

[**MI\_Application\_NewOperationOptions**](mi-application-newoperationoptions.md)
</dt> <dd>

Creates an [**MI\_OperationOptions**](mi-operationoptions.md) object that can be used with the operation functions on the [**MI\_Session**](mi-session.md) object.

</dd> <dt>

[**MI\_Application\_NewParameterSet**](mi-application-newparameterset.md)
</dt> <dd>

Creates a new parameter set.

</dd> <dt>

[**MI\_Application\_NewSerializer**](mi-application-newserializer.md)
</dt> <dd>

Retrieves a serializer object that can then be used to serialize instances and classes into various different formats.

</dd> <dt>

[**MI\_Application\_NewSession**](mi-application-newsession.md)
</dt> <dd>

Creates a session used to share connections for a set of operations to a single destination.

</dd> <dt>

[**MI\_Application\_NewSubscriptionDeliveryOptions**](mi-application-newsubscriptiondeliveryoptions.md)
</dt> <dd>

Creates an [**MI\_SubscriptionDeliveryOptions**](mi-subscriptiondeliveryoptions.md) object that represents the configuration needed to carry out subscribe operations over certain protocols.

</dd> <dt>

[**MI\_CancelCallback**](mi-cancelcallback.md)
</dt> <dd>

Cancels an operation.

</dd> <dt>

[**MI\_Class**](mi-class.md)
</dt> <dd>

Represents the schema of an instance.

</dd> <dt>

[**MI\_Class\_Clone**](mi-class-clone.md)
</dt> <dd>

Clones an [**MI\_Class**](mi-class.md) object.

</dd> <dt>

[**MI\_Class\_Delete**](mi-class-delete.md)
</dt> <dd>

Deletes an [**MI\_Class**](mi-class.md) object.

</dd> <dt>

[**MI\_Class\_GetClassName**](mi-class-getclassname.md)
</dt> <dd>

Gets the class name of the specified class.

</dd> <dt>

[**MI\_Class\_GetClassQualifierSet**](mi-class-getclassqualifierset.md)
</dt> <dd>

Gets the qualifier set that is associated with the specified class object.

</dd> <dt>

[**MI\_Class\_GetElement**](mi-class-getelement.md)
</dt> <dd>

Gets all details of a specified named element from a class.

</dd> <dt>

[**MI\_Class\_GetElementAt**](mi-class-getelementat.md)
</dt> <dd>

Gets details of a class element based on the element index.

</dd> <dt>

[**MI\_Class\_GetElementCount**](mi-class-getelementcount.md)
</dt> <dd>

Gets the number of elements in a class.

</dd> <dt>

[**MI\_Class\_GetMethod**](mi-class-getmethod.md)
</dt> <dd>

Gets details of a method based on the method name.

</dd> <dt>

[**MI\_Class\_GetMethodAt**](mi-class-getmethodat.md)
</dt> <dd>

Gets details of a method based on the method index.

</dd> <dt>

[**MI\_Class\_GetMethodCount**](mi-class-getmethodcount.md)
</dt> <dd>

Gets the number of methods in the class.

</dd> <dt>

[**MI\_Class\_GetNameSpace**](mi-class-getnamespace.md)
</dt> <dd>

Gets the namespace name of the specified class.

</dd> <dt>

[**MI\_Class\_GetParentClass**](mi-class-getparentclass.md)
</dt> <dd>

Gets the parent class for the specified class.

</dd> <dt>

[**MI\_Class\_GetParentClassName**](mi-class-getparentclassname.md)
</dt> <dd>

Gets the parent class name of the specified class.

</dd> <dt>

[**MI\_Class\_GetServerName**](mi-class-getservername.md)
</dt> <dd>

Gets the name of the server from the specified class.

</dd> <dt>

[**MI\_Context\_Canceled**](mi-context-canceled.md)
</dt> <dd>

Determines whether the operation has been canceled. This function is reserved; instead, use the [**MI\_Context\_RegisterCancel**](mi-context-registercancel.md) function.

</dd> <dt>

[**MI\_Context\_ConstructInstance**](mi-context-constructinstance.md)
</dt> <dd>

Initializes an MI class instance on the stack or as a member of a structure.

</dd> <dt>

[**MI\_Context\_ConstructParameters**](mi-context-constructparameters.md)
</dt> <dd>

A provider calls this function to initialize a parameter's instance.

</dd> <dt>

[**MI\_Context\_GetCustomOption**](mi-context-getcustomoption.md)
</dt> <dd>

Retrieves an option set by the client.

</dd> <dt>

[**MI\_Context\_GetCustomOptionAt**](mi-context-getcustomoptionat.md)
</dt> <dd>

Retrieves an option at a particular index that was set by the client.

</dd> <dt>

[**MI\_Context\_GetCustomOptionCount**](mi-context-getcustomoptioncount.md)
</dt> <dd>

Gets the number of custom options available to the provider.

</dd> <dt>

[**MI\_Context\_GetLocale**](mi-context-getlocale.md)
</dt> <dd>

Retrieves the requested locale information that the client specified for the operation.

</dd> <dt>

[**MI\_Context\_GetLocalSession**](mi-context-getlocalsession.md)
</dt> <dd>

Gets the local session ([**MI\_Session**](mi-session.md)) which allows the provider to perform CIM operations against the local server hosting the provider.

</dd> <dt>

[**MI\_Context\_GetNumberOption**](mi-context-getnumberoption.md)
</dt> <dd>

Gets the numeric option that the client sets, based on the operation name.

</dd> <dt>

[**MI\_Context\_GetStringOption**](mi-context-getstringoption.md)
</dt> <dd>

Gets the string option that the client sets, based on the operation name.

</dd> <dt>

[**MI\_Context\_NewDynamicInstance**](mi-context-newdynamicinstance.md)
</dt> <dd>

Creates a new dynamic instance (weakly typed instance without a class declaration) of a class.

</dd> <dt>

[**MI\_Context\_NewInstance**](mi-context-newinstance.md)
</dt> <dd>

Creates a new instance of a class given a class declaration.

</dd> <dt>

[**MI\_Context\_NewParameters**](mi-context-newparameters.md)
</dt> <dd>

Creates a new instance of a method given a method declaration.

</dd> <dt>

[**MI\_Context\_PostCimError**](mi-context-postcimerror.md)
</dt> <dd>

Posts a return code and an error message (in the form of a [**CIM\_Error**](https://msdn.microsoft.com/library/mt445938) object) to the server in response to a request.

</dd> <dt>

[**MI\_Context\_PostError**](mi-context-posterror.md)
</dt> <dd>

Providers call this function to post a return code to the client in response to a request.

</dd> <dt>

[**MI\_Context\_PostIndication**](mi-context-postindication.md)
</dt> <dd>

Posts an indication result to the server in response to a subscribe operation request.

</dd> <dt>

[**MI\_Context\_PostInstance**](mi-context-postinstance.md)
</dt> <dd>

Posts an instance back to the client (through the server) in response to a request.

</dd> <dt>

[**MI\_Context\_PostResult**](mi-context-postresult.md)
</dt> <dd>

Posts the final terminating result code back to the client (through the server) in response to a request.

</dd> <dt>

[**MI\_Context\_PromptUser**](mi-context-promptuser.md)
</dt> <dd>

Sends a prompt message to the client querying whether to continue the operation or cancel it.

</dd> <dt>

[**MI\_Context\_RefuseUnload**](mi-context-refuseunload.md)
</dt> <dd>

Tells the provider infrastructure not to unload the provider.

</dd> <dt>

[**MI\_Context\_RegisterCancel**](mi-context-registercancel.md)
</dt> <dd>

Registers a callback that is invoked when the operation is canceled.

</dd> <dt>

[**MI\_Context\_RequestUnload**](mi-context-requestunload.md)
</dt> <dd>

Requests to unload the module or the provider.

</dd> <dt>

[**MI\_Context\_SetStringOption**](mi-context-setstringoption.md)
</dt> <dd>

Sets a context-specific option.

</dd> <dt>

[**MI\_Context\_ShouldContinue**](mi-context-shouldcontinue.md)
</dt> <dd>

Queries the client to determine if an operation should continue.

</dd> <dt>

[**MI\_Context\_ShouldProcess**](mi-context-shouldprocess.md)
</dt> <dd>

Queries the client to determine if an operation should continue.

</dd> <dt>

[**MI\_Context\_WriteCimError**](mi-context-writecimerror.md)
</dt> <dd>

Sends a CIM (informative) error instance to the client.

</dd> <dt>

[**MI\_Context\_WriteDebug**](mi-context-writedebug.md)
</dt> <dd>

Sends a debug message to the client.

</dd> <dt>

[**MI\_Context\_WriteError**](mi-context-writeerror.md)
</dt> <dd>

Sends an error code and error message to the client.

</dd> <dt>

[**MI\_Context\_WriteMessage**](mi-context-writemessage.md)
</dt> <dd>

Sends an operational message to the client.

</dd> <dt>

[**MI\_Context\_WriteProgress**](mi-context-writeprogress.md)
</dt> <dd>

Sends a progress message to the client.

</dd> <dt>

[**MI\_Context\_WriteStreamParameter**](mi-context-writestreamparameter.md)
</dt> <dd>

Sends streamed parameter data to the client for a method invocation.

</dd> <dt>

[**MI\_Context\_WriteVerbose**](mi-context-writeverbose.md)
</dt> <dd>

Writes a verbose message to the client.

</dd> <dt>

[**MI\_Context\_WriteWarning**](mi-context-writewarning.md)
</dt> <dd>

Writes a warning message to the client.

</dd> <dt>

[**MI\_Deserializer\_Class\_GetClassName**](mi-deserializer-class-getclassname.md)
</dt> <dd>

Gets the class name from a serialized class buffer.

</dd> <dt>

[**MI\_Deserializer\_Class\_GetParentClassName**](mi-deserializer-class-getparentclassname.md)
</dt> <dd>

Gets the parent class name from a serialized class buffer.

</dd> <dt>

[*MI\_Deserializer\_ClassObjectNeeded*](mi-deserializer-classobjectneeded.md)
</dt> <dd>

Used to provide requested class object during deserialization.

</dd> <dt>

[**MI\_Deserializer\_Close**](mi-deserializer-close.md)
</dt> <dd>

Closes a deserializer object and deletes any associated memory that is held within the deserializer.

</dd> <dt>

[**MI\_Deserializer\_DeserializeClass**](mi-deserializer-deserializeclass.md)
</dt> <dd>

Deserializes a serialized buffer into an [**MI\_Class**](mi-class.md) object.

</dd> <dt>

[**MI\_Deserializer\_DeserializeInstance**](mi-deserializer-deserializeinstance.md)
</dt> <dd>

Deserializes a serialized buffer into a [**MI\_Instance**](mi-instance.md) object.

</dd> <dt>

[**MI\_Deserializer\_Instance\_GetClassName**](mi-deserializer-instance-getclassname.md)
</dt> <dd>

Gets the class name associated with the serialized instance.

</dd> <dt>

[**MI\_DestinationOptions\_AddDestinationCredentials**](mi-destinationoptions-adddestinationcredentials.md)
</dt> <dd>

Sets the credentials for talking to the destination.

</dd> <dt>

[**MI\_DestinationOptions\_AddProxyCredentials**](mi-destinationoptions-addproxycredentials.md)
</dt> <dd>

Adds credentials to authenticate against a proxy.

</dd> <dt>

[**MI\_DestinationOptions\_Clone**](mi-destinationoptions-clone.md)
</dt> <dd>

Creates a copy of a [**MI\_DestinationOptions**](mi-destinationoptions.md) structure.

</dd> <dt>

[**MI\_DestinationOptions\_Delete**](mi-destinationoptions-delete.md)
</dt> <dd>

Deletes the destination options structure created by using the [**MI\_Application\_NewDestinationOptions**](mi-application-newdestinationoptions.md) or [**MI\_DestinationOptions\_Clone**](mi-destinationoptions-clone.md) function.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertCACheck**](mi-destinationoptions-getcertcacheck.md)
</dt> <dd>

Gets the server certificate CA check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertCNCheck**](mi-destinationoptions-getcertcncheck.md)
</dt> <dd>

Gets the server certificate CN check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCertRevocationCheck**](mi-destinationoptions-getcertrevocationcheck.md)
</dt> <dd>

Gets the server certificate's revocation check value.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsAt**](mi-destinationoptions-getcredentialsat.md)
</dt> <dd>

Get the credentials at the specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsCount**](mi-destinationoptions-getcredentialscount.md)
</dt> <dd>

Gets the number of previously added credentials.

</dd> <dt>

[**MI\_DestinationOptions\_GetCredentialsPasswordAt**](mi-destinationoptions-getcredentialspasswordat.md)
</dt> <dd>

Gets a credentials password based on a specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetDataLocale**](mi-destinationoptions-getdatalocale.md)
</dt> <dd>

Gets the data locale (as opposed to UI locale) set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_GetDestinationPort**](mi-destinationoptions-getdestinationport.md)
</dt> <dd>

Gets the default port for transport.

</dd> <dt>

[**MI\_DestinationOptions\_GetEncodePortInSPN**](mi-destinationoptions-getencodeportinspn.md)
</dt> <dd>

Gets the port's Service Principal Name encoding value.

</dd> <dt>

[**MI\_DestinationOptions\_GetHttpUrlPrefix**](mi-destinationoptions-gethttpurlprefix.md)
</dt> <dd>

Gets the HTTP URL prefix.

</dd> <dt>

[**MI\_DestinationOptions\_GetImpersonationType**](mi-destinationoptions-getimpersonationtype.md)
</dt> <dd>

Gets the impersonation type.

</dd> <dt>

[**MI\_DestinationOptions\_GetMaxEnvelopeSize**](mi-destinationoptions-getmaxenvelopesize.md)
</dt> <dd>

Gets the maximum size of the packet sent to a server or received by the client from the server.

</dd> <dt>

[**MI\_DestinationOptions\_GetNumber**](mi-destinationoptions-getnumber.md)
</dt> <dd>

Gets a previously added custom number option.

</dd> <dt>

[**MI\_DestinationOptions\_GetOption**](mi-destinationoptions-getoption.md)
</dt> <dd>

Gets a previously added option value based on the option name.

</dd> <dt>

[**MI\_DestinationOptions\_GetOptionAt**](mi-destinationoptions-getoptionat.md)
</dt> <dd>

Gets a previously added option value based on the specified index.

</dd> <dt>

[**MI\_DestinationOptions\_GetOptionCount**](mi-destinationoptions-getoptioncount.md)
</dt> <dd>

Gets the number of options previously added.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketEncoding**](mi-destinationoptions-getpacketencoding.md)
</dt> <dd>

Gets the previously set packet encoding setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketIntegrity**](mi-destinationoptions-getpacketintegrity.md)
</dt> <dd>

Gets the packet integrity setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetPacketPrivacy**](mi-destinationoptions-getpacketprivacy.md)
</dt> <dd>

Gets the packet privacy (encryption) setting.

</dd> <dt>

[**MI\_DestinationOptions\_GetProxyType**](mi-destinationoptions-getproxytype.md)
</dt> <dd>

Gets the proxy type set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_GetString**](mi-destinationoptions-getstring.md)
</dt> <dd>

Gets a previously added custom string option.

</dd> <dt>

[**MI\_DestinationOptions\_GetTimeout**](mi-destinationoptions-gettimeout.md)
</dt> <dd>

Gets the default options timeout value.

</dd> <dt>

[**MI\_DestinationOptions\_GetTransport**](mi-destinationoptions-gettransport.md)
</dt> <dd>

Gets the transport setting that the client added.

</dd> <dt>

[**MI\_DestinationOptions\_GetUILocale**](mi-destinationoptions-getuilocale.md)
</dt> <dd>

Gets the user interface locale set by the user.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertCACheck**](mi-destinationoptions-setcertcacheck.md)
</dt> <dd>

Enables or disables the CA certificate check for an SSL transport.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertCNCheck**](mi-destinationoptions-setcertcncheck.md)
</dt> <dd>

Enables or disables the certificate CN check when an SSL transport is used.

</dd> <dt>

[**MI\_DestinationOptions\_SetCertRevocationCheck**](mi-destinationoptions-setcertrevocationcheck.md)
</dt> <dd>

Enables or disables the certificate revocation when communicating over SSL.

</dd> <dt>

[**MI\_DestinationOptions\_SetDataLocale**](mi-destinationoptions-setdatalocale.md)
</dt> <dd>

Sets the default data locale to use for operations.

</dd> <dt>

[**MI\_DestinationOptions\_SetDestinationPort**](mi-destinationoptions-setdestinationport.md)
</dt> <dd>

Set the port to use to communicate to the destination.

</dd> <dt>

[**MI\_DestinationOptions\_SetEncodePortInSPN**](mi-destinationoptions-setencodeportinspn.md)
</dt> <dd>

Enables or disables the encoding of the port number in the Service Principal Name when establishing a connection to a remote machine.

</dd> <dt>

[**MI\_DestinationOptions\_SetHttpUrlPrefix**](mi-destinationoptions-sethttpurlprefix.md)
</dt> <dd>

Set the default HTTP URL prefix for transports that go over HTTP and HTTPS.

</dd> <dt>

[**MI\_DestinationOptions\_SetImpersonationType**](mi-destinationoptions-setimpersonationtype.md)
</dt> <dd>

Sets the impersonation type.

</dd> <dt>

[**MI\_DestinationOptions\_SetMaxEnvelopeSize**](mi-destinationoptions-setmaxenvelopesize.md)
</dt> <dd>

Sets the maximum packet size for transports.

</dd> <dt>

[**MI\_DestinationOptions\_SetNumber**](mi-destinationoptions-setnumber.md)
</dt> <dd>

Sets a custom numeric option value.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketEncoding**](mi-destinationoptions-setpacketencoding.md)
</dt> <dd>

Sets the encoding mechanism for certain protocol handles.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketIntegrity**](mi-destinationoptions-setpacketintegrity.md)
</dt> <dd>

Enables or disables packet integrity (signing) of a protocol connection.

</dd> <dt>

[**MI\_DestinationOptions\_SetPacketPrivacy**](mi-destinationoptions-setpacketprivacy.md)
</dt> <dd>

Enables or disables packet privacy (encryption).

</dd> <dt>

[**MI\_DestinationOptions\_SetProxyType**](mi-destinationoptions-setproxytype.md)
</dt> <dd>

Sets the type of proxy settings to use when communicating to a destination through a proxy.

</dd> <dt>

[**MI\_DestinationOptions\_SetString**](mi-destinationoptions-setstring.md)
</dt> <dd>

Sets a custom string option.

</dd> <dt>

[**MI\_DestinationOptions\_SetTimeout**](mi-destinationoptions-settimeout.md)
</dt> <dd>

Sets the default options timeout value.

</dd> <dt>

[**MI\_DestinationOptions\_SetTransport**](mi-destinationoptions-settransport.md)
</dt> <dd>

Sets the transport to be used to communicate with the destination machine.

</dd> <dt>

[**MI\_DestinationOptions\_SetUILocale**](mi-destinationoptions-setuilocale.md)
</dt> <dd>

Sets the default UI locale for operations.

</dd> <dt>

[**MI\_Filter\_Evaluate**](mi-filter-evaluate.md)
</dt> <dd>

The provider calls this function to evaluate an instance against a given filter.

</dd> <dt>

[**MI\_Filter\_GetExpression**](mi-filter-getexpression.md)
</dt> <dd>

Gets the filter language and expression.

</dd> <dt>

[**MI\_HostedProvider\_Close**](mi-hostedprovider-close.md)
</dt> <dd>

Close a hosted provider handle that was returned from [**MI\_Application\_NewHostedProvider**](mi-application-newhostedprovider.md).

</dd> <dt>

[**MI\_HostedProvider\_GetApplication**](mi-hostedprovider-getapplication.md)
</dt> <dd>

Gets the top-level application handle from which the hosted provider handle was created.

</dd> <dt>

[**MI\_Instance\_AddElement**](mi-instance-addelement.md)
</dt> <dd>

Adds a new property to a dynamic instance (supported only by dynamic instances whose schema may be extended at run time).

</dd> <dt>

[**MI\_Instance\_ClearElement**](mi-instance-clearelement.md)
</dt> <dd>

Clears the value of the named element (CIM property) and sets it to **NULL**.

</dd> <dt>

[**MI\_Instance\_ClearElementAt**](mi-instance-clearelementat.md)
</dt> <dd>

Clears the value of the element (CIM property) at the specified index and sets it to **NULL**.

</dd> <dt>

[**MI\_Instance\_Clone**](mi-instance-clone.md)
</dt> <dd>

Creates a copy of the specified instance on the heap.

</dd> <dt>

[**MI\_Instance\_Delete**](mi-instance-delete.md)
</dt> <dd>

Deletes an instance that was created on the heap or cloned from another instance.

</dd> <dt>

[**MI\_Instance\_Destruct**](mi-instance-destruct.md)
</dt> <dd>

Deletes an instance that was created on the stack or as a member of a structure.

</dd> <dt>

[**MI\_Instance\_GetClass**](mi-instance-getclass.md)
</dt> <dd>

Gets the [**MI\_Class**](mi-class.md) associated with an instance.

</dd> <dt>

[**MI\_Instance\_GetClassName**](mi-instance-getclassname.md)
</dt> <dd>

Gets the class name of the specified instance.

</dd> <dt>

[**MI\_Instance\_GetElement**](mi-instance-getelement.md)
</dt> <dd>

Gets the value of the named element (CIM property).

</dd> <dt>

[**MI\_Instance\_GetElementAt**](mi-instance-getelementat.md)
</dt> <dd>

Gets the value of the element (CIM property) at the specified index.

</dd> <dt>

[**MI\_Instance\_GetElementCount**](mi-instance-getelementcount.md)
</dt> <dd>

Gets the number of elements in an instance.

</dd> <dt>

[**MI\_Instance\_GetNameSpace**](mi-instance-getnamespace.md)
</dt> <dd>

Gets the namespace name of the specified instance.

</dd> <dt>

[**MI\_Instance\_GetServerName**](mi-instance-getservername.md)
</dt> <dd>

Gets the server name from the specified instance.

</dd> <dt>

[**MI\_Instance\_IsA**](mi-instance-isa.md)
</dt> <dd>

Determines if the instance *self* is an instance of the class given by *classDecl*.

</dd> <dt>

[**MI\_Instance\_Normalize**](mi-instance-normalize.md)
</dt> <dd>

Parses an [**MI\_Instance\_ExFT**](mi-instanceexft.md) structure and then retrieves the [**MI\_InstanceFT**](mi-instanceft.md) function table.

</dd> <dt>

[**MI\_Instance\_SetElement**](mi-instance-setelement.md)
</dt> <dd>

Set the value of the element with the given name in the given instance.

</dd> <dt>

[**MI\_Instance\_SetElementAt**](mi-instance-setelementat.md)
</dt> <dd>

Set the value of the element at the given index of an instance.

</dd> <dt>

[**MI\_Instance\_SetNameSpace**](mi-instance-setnamespace.md)
</dt> <dd>

Sets the namespace name of the specified instance.

</dd> <dt>

[**MI\_Instance\_SetServerName**](mi-instance-setservername.md)
</dt> <dd>

Sets the server name of the specified instance.

</dd> <dt>

[**MI\_MethodDecl\_Invoke**](mi-methoddecl-invoke.md)
</dt> <dd>

Calls the provider implementation of a CIM method represented by a [**MI\_MethodDecl**](mi-methoddecl.md) structure.

</dd> <dt>

[**MI\_Module\_Load**](mi-module-load.md)
</dt> <dd>

Loads the main provider module.

</dd> <dt>

[**MI\_Module\_Unload**](mi-module-unload.md)
</dt> <dd>

Unloads the main provider module.

</dd> <dt>

[**MI\_Operation\_Cancel**](mi-operation-cancel.md)
</dt> <dd>

Cancels a running operation.

</dd> <dt>

[**MI\_Operation\_Close**](mi-operation-close.md)
</dt> <dd>

Closes an operation handle.

</dd> <dt>

[**MI\_Operation\_GetClass**](mi-operation-getclass.md)
</dt> <dd>

Gets a synchronous result for a class operation.

</dd> <dt>

[**MI\_Operation\_GetIndication**](mi-operation-getindication.md)
</dt> <dd>

Get the synchronous results from a subscription.

</dd> <dt>

[**MI\_Operation\_GetInstance**](mi-operation-getinstance.md)
</dt> <dd>

Gets a synchronous result for an instance operation.

</dd> <dt>

[**MI\_Operation\_GetSession**](mi-operation-getsession.md)
</dt> <dd>

Gets the session associated with an operation.

</dd> <dt>

[**MI\_OperationCallback\_Class**](mi-operationcallback-class.md)
</dt> <dd>

Optional instance callback to get classes and class options from an operation.

</dd> <dt>

[**MI\_OperationCallback\_Indication**](mi-operationcallback-indication.md)
</dt> <dd>

Optional instance callback to get indication (subscribe) results from an operation.

</dd> <dt>

[**MI\_OperationCallback\_Instance**](mi-operationcallback-instance.md)
</dt> <dd>

Optional instance callback to get asynchronous results from an operation.

</dd> <dt>

[**MI\_OperationCallback\_PromptUser**](mi-operationcallback-promptuser.md)
</dt> <dd>

Optional callback to handle prompt user requests from the server.

</dd> <dt>

[**MI\_OperationCallback\_StreamedParameter**](mi-operationcallback-streamedparameter.md)
</dt> <dd>

Optional callback to get streamed parameter results from method invocation operations.

</dd> <dt>

[**MI\_OperationCallback\_WriteError**](mi-operationcallback-writeerror.md)
</dt> <dd>

Optional callback to receive write error messages from the server.

</dd> <dt>

[**MI\_OperationCallback\_WriteMessage**](mi-operationcallback-writemessage.md)
</dt> <dd>

Optional callback to receive write messages from the server.

</dd> <dt>

[**MI\_OperationCallback\_WriteProgress**](mi-operationcallback-writeprogress.md)
</dt> <dd>

Optional callback to receive progress reports from the server.

</dd> <dt>

[**MI\_OperationOptions\_Clone**](mi-operationoptions-clone.md)
</dt> <dd>

Creates a copy of a [**MI\_OperationOptions**](mi-operationoptions.md) structure.

</dd> <dt>

[**MI\_OperationOptions\_Delete**](mi-operationoptions-delete.md)
</dt> <dd>

Deletes an option set and its associated memory.

</dd> <dt>

[**MI\_OperationOptions\_DisableChannel**](mi-operationoptions-disablechannel.md)
</dt> <dd>

Uses [**MI\_Context\_WriteMessage**](mi-context-writemessage.md) to disable logging to the specified channel.

</dd> <dt>

[**MI\_OperationOptions\_EnableChannel**](mi-operationoptions-enablechannel.md)
</dt> <dd>

Uses [**MI\_Context\_WriteMessage**](mi-context-writemessage.md) to enable logging to the specified channel.

</dd> <dt>

[**MI\_OperationOptions\_GetEnabledChannels**](mi-operationoptions-getenabledchannels.md)
</dt> <dd>

Gets the list of previously enabled channels.

</dd> <dt>

[**MI\_OperationOptions\_GetNumber**](mi-operationoptions-getnumber.md)
</dt> <dd>

Gets a previously added custom number option.

</dd> <dt>

[**MI\_OperationOptions\_GetOption**](mi-operationoptions-getoption.md)
</dt> <dd>

Gets a previously added option value based on the option name.

</dd> <dt>

[**MI\_OperationOptions\_GetOptionAt**](mi-operationoptions-getoptionat.md)
</dt> <dd>

Gets a previously added option value based on the specified index.

</dd> <dt>

[**MI\_OperationOptions\_GetOptionCount**](mi-operationoptions-getoptioncount.md)
</dt> <dd>

Gets the number of options previously added.

</dd> <dt>

[**MI\_OperationOptions\_GetPromptUserMode**](mi-operationoptions-getpromptusermode.md)
</dt> <dd>

Gets the value that tells the server how to respond to a provider's call to [**MI\_Context\_PromptUser**](mi-context-promptuser.md).

</dd> <dt>

[**MI\_OperationOptions\_GetPromptUserRegularMode**](mi-operationoptions-getpromptuserregularmode.md)
</dt> <dd>

Gets the value that tells the server how to respond to a provider's call to [**MI\_Context\_PromptUser**](mi-context-promptuser.md).

</dd> <dt>

[**MI\_OperationOptions\_GetProviderArchitecture**](mi-operationoptions-getproviderarchitecture.md)
</dt> <dd>

Gets the provider architecture for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetResourceUri**](mi-operationoptions-getresourceuri.md)
</dt> <dd>

Gets the resource URI being used for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetResourceUriPrefix**](mi-operationoptions-getresourceuriprefix.md)
</dt> <dd>

Gets the resource URI prefix being used for an operation.

</dd> <dt>

[**MI\_OperationOptions\_GetString**](mi-operationoptions-getstring.md)
</dt> <dd>

Gets a custom string option.

</dd> <dt>

[**MI\_OperationOptions\_GetTimeout**](mi-operationoptions-gettimeout.md)
</dt> <dd>

Gets the operation timeout value.

</dd> <dt>

[**MI\_OperationOptions\_GetUseMachineID**](mi-operationoptions-getusemachineid.md)
</dt> <dd>

Gets the value that indicates whether to use machine identification information in the operation request.

</dd> <dt>

[**MI\_OperationOptions\_GetWriteErrorMode**](mi-operationoptions-getwriteerrormode.md)
</dt> <dd>

Sets the error reporting mode.

</dd> <dt>

[**MI\_OperationOptions\_SetCustomOption**](mi-operationoptions-setcustomoption.md)
</dt> <dd>

Sets a custom option for the operation.

</dd> <dt>

[**MI\_OperationOptions\_SetNumber**](mi-operationoptions-setnumber.md)
</dt> <dd>

Sets a custom number option value.

</dd> <dt>

[**MI\_OperationOptions\_SetPromptUserMode**](mi-operationoptions-setpromptusermode.md)
</dt> <dd>

Sets the value that tells the server how to respond to a provider's call to the [**MI\_Context\_PromptUser**](mi-context-promptuser.md) function.

</dd> <dt>

[**MI\_OperationOptions\_SetPromptUserRegularMode**](mi-operationoptions-setpromptuserregularmode.md)
</dt> <dd>

Sets the value that tells the server how to respond to a provider's call to the [**MI\_Context\_PromptUser**](mi-context-promptuser.md) function.

</dd> <dt>

[**MI\_OperationOptions\_SetProviderArchitecture**](mi-operationoptions-setproviderarchitecture.md)
</dt> <dd>

Sets the provider architecture for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetResourceUri**](mi-operationoptions-setresourceuri.md)
</dt> <dd>

Sets the resource URI to use for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetResourceUriPrefix**](mi-operationoptions-setresourceuriprefix.md)
</dt> <dd>

Sets the resource URI prefix to use for an operation.

</dd> <dt>

[**MI\_OperationOptions\_SetString**](mi-operationoptions-setstring.md)
</dt> <dd>

Sets a custom string option.

</dd> <dt>

[**MI\_OperationOptions\_SetTimeout**](mi-operationoptions-settimeout.md)
</dt> <dd>

Sets the operation timeout for a specific operation.

</dd> <dt>

[**MI\_OperationOptions\_SetUseMachineID**](mi-operationoptions-setusemachineid.md)
</dt> <dd>

Enables or disables the sending of machine identification information in the operation request.

</dd> <dt>

[**MI\_OperationOptions\_SetWriteErrorMode**](mi-operationoptions-setwriteerrormode.md)
</dt> <dd>

Sets the error reporting mode.

</dd> <dt>

[**MI\_ParameterSet\_GetMethodReturnType**](mi-parameterset-getmethodreturntype.md)
</dt> <dd>

Gets the method return type and qualifier set for a specified parameter set.

</dd> <dt>

[**MI\_ParameterSet\_GetParameter**](mi-parameterset-getparameter.md)
</dt> <dd>

Gets a method's parameter information based on a parameter name.

</dd> <dt>

[**MI\_ParameterSet\_GetParameterAt**](mi-parameterset-getparameterat.md)
</dt> <dd>

Gets a method's parameter information at the specified index.

</dd> <dt>

[**MI\_ParameterSet\_GetParameterCount**](mi-parameterset-getparametercount.md)
</dt> <dd>

Gets the number of parameters in a method's parameter set.

</dd> <dt>

[**MI\_PropertySet\_AddElement**](mi-propertyset-addelement.md)
</dt> <dd>

Adds a name to the property list.

</dd> <dt>

[**MI\_PropertySet\_Clear**](mi-propertyset-clear.md)
</dt> <dd>

Removes all names from the property list. Afterwards, the count is zero. This allows property lists to be reused (without having to be destructed and reconstructed).

</dd> <dt>

[**MI\_PropertySet\_Clone**](mi-propertyset-clone.md)
</dt> <dd>

Creates a copy of the specified property set on the heap.

</dd> <dt>

[**MI\_PropertySet\_ContainsElement**](mi-propertyset-containselement.md)
</dt> <dd>

Determines whether the property list contains the specified property name.

</dd> <dt>

[**MI\_PropertySet\_Delete**](mi-propertyset-delete.md)
</dt> <dd>

Deletes the specified property list that was constructed on the heap.

</dd> <dt>

[**MI\_PropertySet\_Destruct**](mi-propertyset-destruct.md)
</dt> <dd>

Deletes the specified property list that was constructed on the stack.

</dd> <dt>

[**MI\_PropertySet\_GetElementAt**](mi-propertyset-getelementat.md)
</dt> <dd>

Gets the element of a property set at the specified index.

</dd> <dt>

[**MI\_PropertySet\_GetElementCount**](mi-propertyset-getelementcount.md)
</dt> <dd>

Gets the number of elements in the specified property set.

</dd> <dt>

[**MI\_ProviderFT\_AssociatorInstances**](mi-providerft-associatorinstances.md)
</dt> <dd>

Finds all CIM instances associated with a specified CIM instance.

</dd> <dt>

[**MI\_ProviderFT\_CreateInstance**](mi-providerft-createinstance.md)
</dt> <dd>

Create a single CIM instance in the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_DeleteInstance**](mi-providerft-deleteinstance.md)
</dt> <dd>

Delete a single CIM instance from the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_DisableIndications**](mi-providerft-disableindications.md)
</dt> <dd>

Disable indications delivery from the provider.

</dd> <dt>

[**MI\_ProviderFT\_EnableIndications**](mi-providerft-enableindications.md)
</dt> <dd>

Enable indications delivery from the provider.

</dd> <dt>

[**MI\_ProviderFT\_EnumerateInstances**](mi-providerft-enumerateinstances.md)
</dt> <dd>

Enumerate instances of a CIM class in the target namespace.

</dd> <dt>

[**MI\_ProviderFT\_GetInstance**](mi-providerft-getinstance.md)
</dt> <dd>

Get a single CIM instance from the provider.

</dd> <dt>

[**MI\_ProviderFT\_Invoke**](mi-providerft-invoke.md)
</dt> <dd>

Calls a CIM extrinsic method on behalf of a requestor.

</dd> <dt>

[**MI\_ProviderFT\_Load**](mi-providerft-load.md)
</dt> <dd>

Initialize the provider.

</dd> <dt>

[**MI\_ProviderFT\_ModifyInstance**](mi-providerft-modifyinstance.md)
</dt> <dd>

Modify an existing CIM instance in the target namespace. The instance must already exist.

</dd> <dt>

[**MI\_ProviderFT\_ReferenceInstances**](mi-providerft-referenceinstances.md)
</dt> <dd>

Enumerate association instances that refer to a particular CIM instance.

</dd> <dt>

[**MI\_ProviderFT\_Subscribe**](mi-providerft-subscribe.md)
</dt> <dd>

Subscribe to indications.

</dd> <dt>

[**MI\_ProviderFT\_Unload**](mi-providerft-unload.md)
</dt> <dd>

TBD

</dd> <dt>

[**MI\_ProviderFT\_Unsubscribe**](mi-providerft-unsubscribe.md)
</dt> <dd>

unsubscribe from indications.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifier**](mi-qualifierset-getqualifier.md)
</dt> <dd>

Gets the qualifier information based on the given qualifier name.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifierAt**](mi-qualifierset-getqualifierat.md)
</dt> <dd>

Gets a qualifier at the specified index.

</dd> <dt>

[**MI\_QualifierSet\_GetQualifierCount**](mi-qualifierset-getqualifiercount.md)
</dt> <dd>

Gets the number of qualifiers in a qualifier set.

</dd> <dt>

[**MI\_Serializer\_Close**](mi-serializer-close.md)
</dt> <dd>

Closes a serializer object and frees any internal memory associated with it.

</dd> <dt>

[**MI\_Serializer\_SerializeClass**](mi-serializer-serializeclass.md)
</dt> <dd>

Serializes an [**MI\_Class**](mi-class.md) into a buffer in the format specified when the serializer was created. Options can be passed into the flags to control if the class and all its parent classes are serialized, or just the child-most class.

</dd> <dt>

[**MI\_Serializer\_SerializeInstance**](mi-serializer-serializeinstance.md)
</dt> <dd>

Serializes an [**MI\_Instance**](mi-instance.md) into a buffer in the format specified when the serializer was created. Options can be passed into the flags to control if the class is also serialized into the buffer as well as the instance.

</dd> <dt>

[*MI\_Server\_GetSystemName*](mi-server-getsystemname.md)
</dt> <dd>

Gets the system name for the server.

</dd> <dt>

[*MI\_Server\_GetVersion*](mi-server-getversion.md)
</dt> <dd>

Gets the value of the MI\_VERSION macro used when generating the provider.

</dd> <dt>

[**MI\_Session\_AssociatorInstances**](mi-session-associatorinstances.md)
</dt> <dd>

Finds instances that are associated with the specific key instance.

</dd> <dt>

[**MI\_Session\_Close**](mi-session-close.md)
</dt> <dd>

Closes a session and releases all associated memory.

</dd> <dt>

[**MI\_Session\_CreateInstance**](mi-session-createinstance.md)
</dt> <dd>

Creates an instance on the server that the session represents.

</dd> <dt>

[**MI\_Session\_DeleteInstance**](mi-session-deleteinstance.md)
</dt> <dd>

Deletes an instance on the server represented by the session.

</dd> <dt>

[**MI\_Session\_EnumerateClasses**](mi-session-enumerateclasses.md)
</dt> <dd>

Enumerates the classes of a specified session.

</dd> <dt>

[**MI\_Session\_EnumerateInstances**](mi-session-enumerateinstances.md)
</dt> <dd>

Enumerate all instances (on the server represented by the session) that are associated with a class.

</dd> <dt>

[**MI\_Session\_GetApplication**](mi-session-getapplication.md)
</dt> <dd>

Gets the application handle that was used to create the specified session.

</dd> <dt>

[**MI\_Session\_GetClass**](mi-session-getclass.md)
</dt> <dd>

Gets an [**MI\_Class**](mi-class.md) declaration based on a specific class name.

</dd> <dt>

[**MI\_Session\_GetInstance**](mi-session-getinstance.md)
</dt> <dd>

Gets the specified instance from the server represented by the session.

</dd> <dt>

[**MI\_Session\_Invoke**](mi-session-invoke.md)
</dt> <dd>

Invokes a method in the provider.

</dd> <dt>

[**MI\_Session\_ModifyInstance**](mi-session-modifyinstance.md)
</dt> <dd>

Updates an existing instance in the server represented by the session.

</dd> <dt>

[**MI\_Session\_QueryInstances**](mi-session-queryinstances.md)
</dt> <dd>

Queries for a set of instances based on a query expression.

</dd> <dt>

[**MI\_Session\_ReferenceInstances**](mi-session-referenceinstances.md)
</dt> <dd>

Finds the association object that references the specified key instance.

</dd> <dt>

[**MI\_Session\_Subscribe**](mi-session-subscribe.md)
</dt> <dd>

Subscribes to an indication on the server represented by the session.

</dd> <dt>

[**MI\_Session\_TestConnection**](mi-session-testconnection.md)
</dt> <dd>

Tests a connection by communicating with the server represented by the session to determine whether it is responding.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_AddDeliveryCredentials**](mi-subscriptiondeliveryoptions-adddeliverycredentials.md)
</dt> <dd>

Sets a subscription option for delivery credentials to use when connecting back to the client to deliver a push indication result.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_Clone**](mi-subscriptiondeliveryoptions-clone.md)
</dt> <dd>

Creates a copy of a [**MI\_SubscriptionDeliveryOptions**](mi-subscriptiondeliveryoptions.md) structure.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_Delete**](mi-subscriptiondeliveryoptions-delete.md)
</dt> <dd>

Deletes the specified subscription delivery options structure.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetBookmark**](mi-subscriptiondeliveryoptions-getbookmark.md)
</dt> <dd>

Gets a previously set subscription bookmark.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsAt**](mi-subscriptiondeliveryoptions-getcredentialsat.md)
</dt> <dd>

Gets a previously added credential based on a specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsCount**](mi-subscriptiondeliveryoptions-getcredentialscount.md)
</dt> <dd>

Gets the number of previously added credentials.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetCredentialsPasswordAt**](mi-subscriptiondeliveryoptions-getcredentialspasswordat.md)
</dt> <dd>

Gets a previously added credential password based on a specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDateTime**](mi-subscriptiondeliveryoptions-getdatetime.md)
</dt> <dd>

Gets a previously set datetime option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryDestination**](mi-subscriptiondeliveryoptions-getdeliverydestination.md)
</dt> <dd>

Gets the previously set subscription delivery destination.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryPortNumber**](mi-subscriptiondeliveryoptions-getdeliveryportnumber.md)
</dt> <dd>

Gets the previously set delivery port number.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryRetryAttempts**](mi-subscriptiondeliveryoptions-getdeliveryretryattempts.md)
</dt> <dd>

Gets the number of delivery retry attempts.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetDeliveryRetryInterval**](mi-subscriptiondeliveryoptions-getdeliveryretryinterval.md)
</dt> <dd>

Gets the delivery retry interval—the amount of time to wait before retrying the delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetExpirationTime**](mi-subscriptiondeliveryoptions-getexpirationtime.md)
</dt> <dd>

Gets the delivery expiration value (which can be expressed as a timestamp or an interval).

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetHeartbeatInterval**](mi-subscriptiondeliveryoptions-getheartbeatinterval.md)
</dt> <dd>

Gets the delivery heartbeat interval.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetInterval**](mi-subscriptiondeliveryoptions-getinterval.md)
</dt> <dd>

Gets the delivery interval for a specified option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetMaximumLatency**](mi-subscriptiondeliveryoptions-getmaximumlatency.md)
</dt> <dd>

Gets the maximum amount of time that the server will hold a result before delivering it to the client.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetNumber**](mi-subscriptiondeliveryoptions-getnumber.md)
</dt> <dd>

Gets the value of the named numeric option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOption**](mi-subscriptiondeliveryoptions-getoption.md)
</dt> <dd>

Gets the value of the named option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOptionAt**](mi-subscriptiondeliveryoptions-getoptionat.md)
</dt> <dd>

Gets the option at the specified index.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetOptionCount**](mi-subscriptiondeliveryoptions-getoptioncount.md)
</dt> <dd>

Gets the number of previously set options.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_GetString**](mi-subscriptiondeliveryoptions-getstring.md)
</dt> <dd>

Gets the value of the named string option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetBookmark**](mi-subscriptiondeliveryoptions-setbookmark.md)
</dt> <dd>

Sets a bookmark for subscription indication delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDateTime**](mi-subscriptiondeliveryoptions-setdatetime.md)
</dt> <dd>

Sets the value of a named DateTime option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryDestination**](mi-subscriptiondeliveryoptions-setdeliverydestination.md)
</dt> <dd>

Sets the destination endpoint that an indication will be delivered to.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryPortNumber**](mi-subscriptiondeliveryoptions-setdeliveryportnumber.md)
</dt> <dd>

Sets the subscription delivery port number.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryRetryAttempts**](mi-subscriptiondeliveryoptions-setdeliveryretryattempts.md)
</dt> <dd>

Sets the number of times a push delivery subscription will try to deliver a result.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetDeliveryRetryInterval**](mi-subscriptiondeliveryoptions-setdeliveryretryinterval.md)
</dt> <dd>

Sets the delivery retry interval for subscriptions that are for push delivery.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetExpirationTime**](mi-subscriptiondeliveryoptions-setexpirationtime.md)
</dt> <dd>

Sets the subscription expiration time (when the subscription will shut down).

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetHeartbeatInterval**](mi-subscriptiondeliveryoptions-setheartbeatinterval.md)
</dt> <dd>

Sets the heartbeat interval.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetInterval**](mi-subscriptiondeliveryoptions-setinterval.md)
</dt> <dd>

Sets the value of a named interval option.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetMaximumLatency**](mi-subscriptiondeliveryoptions-setmaximumlatency.md)
</dt> <dd>

Sets the maximum amount of time that the server will hold a result before delivering it to the client.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetNumber**](mi-subscriptiondeliveryoptions-setnumber.md)
</dt> <dd>

Sets the value of a named numeric option that is not covered by a dedicated function.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions\_SetString**](mi-subscriptiondeliveryoptions-setstring.md)
</dt> <dd>

Sets the value of a named string option that is not covered by a dedicated function.

</dd> <dt>

[**MI\_Utilities\_CimErrorFromErrorCode**](mi-utilities-cimerrorfromerrorcode.md)
</dt> <dd>

Maps an operating-system specific error code to a CIM error instance.

</dd> <dt>

[**MI\_Utilities\_MapErrorToExtendedError**](mi-utilities-maperrortoextendederror.md)
</dt> <dd>

[**MI\_Utilities\_MapErrorToExtendedError**](mi-utilities-maperrortoextendederror.md) is not supported.

</dd> <dt>

[**MI\_Utilities\_MapErrorToMiErrorCategory**](mi-utilities-maperrortomierrorcategory.md)
</dt> <dd>

Maps an operating system specific error code to an error category.

</dd> </dl>

 

 




