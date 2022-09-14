---
title: COM Glossary
description: Glossary page
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 9e2c56a2-0572-48b6-a2ef-650f1cf1b62e
ms.topic: article
ms.date: 05/31/2018
---

# COM Glossary

<dl> <dt>

<span id="com.activation_gloss"></span><span id="COM.ACTIVATION_GLOSS"></span>**activation**
</dt> <dd>

The process of loading an object in memory, which puts it into the running state.

</dd> <dt>

<span id="com.active_state_gloss"></span><span id="COM.ACTIVE_STATE_GLOSS"></span>**active state**
</dt> <dd>

A COM object that is in the running state and has a visible user interface.

</dd> <dt>

<span id="com.absolute_moniker_gloss"></span><span id="COM.ABSOLUTE_MONIKER_GLOSS"></span>**absolute moniker**
</dt> <dd>

A moniker that specifies the absolute location of an object. An absolute moniker is analogous to a full path.

</dd> <dt>

<span id="com.advisory_holder_gloss"></span><span id="COM.ADVISORY_HOLDER_GLOSS"></span>**advisory holder**
</dt> <dd>

A COM object that caches, manages, and sends notifications of changes to container applications' advisory sinks.

</dd> <dt>

<span id="com.advisory_sink_gloss"></span><span id="COM.ADVISORY_SINK_GLOSS"></span>**advisory sink**
</dt> <dd>

A COM object that can receive notifications of changes in an embedded object or linked object because it implements the [**IAdviseSink**](/windows/desktop/api/ObjIdl/nn-objidl-iadvisesink) or [**IAdviseSink2**](/windows/desktop/api/ObjIdl/nn-objidl-iadvisesink2) interface. Containers that need to be notified of changes in objects implement an advisory sink. Notifications originate in the server, which uses an advisory holder object to cache and manage notifications to containers.

</dd> <dt>

<span id="com.aggregate_object_gloss"></span><span id="COM.AGGREGATE_OBJECT_GLOSS"></span>**aggregate object**
</dt> <dd>

A COM object that is made up of one or more other COM objects. One object in the aggregate is designated the controlling object, which controls which interfaces in the aggregate are exposed and which are private. This controlling object has a special implementation of [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) called the controlling **IUnknown**. All objects in the aggregate must pass calls to **IUnknown** methods through the controlling **IUnknown**.

</dd> <dt>

<span id="com.aggregation_gloss"></span><span id="COM.AGGREGATION_GLOSS"></span>**aggregation**
</dt> <dd>

A composition technique for implementing COM objects. It allows you to build a new object by reusing one or more existing objects' interface implementations. The aggregate object chooses which interfaces to expose to clients, and the interfaces are exposed as if they were implemented by the aggregate object. Clients of the aggregate object communicate only with the aggregate object.

</dd> <dt>

<span id="com.ambient_property_gloss"></span><span id="COM.AMBIENT_PROPERTY_GLOSS"></span>**ambient property**
</dt> <dd>

A run-time property that is managed and exposed by the container. Typically, an ambient property represents a characteristic of a form, such as background color, that needs to be communicated to a control so that the control can assume the look and feel of its surrounding environment.

</dd> <dt>

<span id="com.anti_moniker_gloss"></span><span id="COM.ANTI_MONIKER_GLOSS"></span>**anti-moniker**
</dt> <dd>

The inverse of a file, item, or pointer moniker. An anti-moniker is added to the end of a file, item, or pointer moniker to nullify it. Anti-monikers are used in the construction of relative monikers.

</dd> <dt>

<span id="com.artificial_reference_counting_gloss"></span><span id="COM.ARTIFICIAL_REFERENCE_COUNTING_GLOSS"></span>**artificial reference counting**
</dt> <dd>

A technique used to help protect an object before calling a function or method that could prematurely destroy it. A program calls **IUnknown::AddRef** to increment the object's reference count before making the call that could free the object. After the function returns, the program calls **IUnknown::Release** to decrement the count.

</dd> <dt>

<span id="com.asynchronous_binding_gloss"></span><span id="COM.ASYNCHRONOUS_BINDING_GLOSS"></span>**asynchronous binding**
</dt> <dd>

A type of binding in which it is necessary for the process to occur asynchronously to avoid performance degradation for the end user. Typically, asynchronous binding is used in distributed environments such as the World Wide Web. OLE supports asynchronous moniker classes and callback mechanisms that allow the process of locating and initializing an object in a distributed environment to occur while other operations are being carried out.

</dd> <dt>

<span id="com.asynchronous_call_gloss"></span><span id="COM.ASYNCHRONOUS_CALL_GLOSS"></span>**asynchronous call**
</dt> <dd>

A call to a function that is executed separately so that the caller can continue processing instructions without waiting for the function to return.

</dd> <dt>

<span id="com.asynchronous_moniker_gloss"></span><span id="COM.ASYNCHRONOUS_MONIKER_GLOSS"></span>**asynchronous moniker**
</dt> <dd>

A moniker that supports asynchronous binding. For example, instances of the system-supplied URL moniker class are asynchronous monikers.

</dd> <dt>

<span id="com.automation_gloss"></span><span id="COM.AUTOMATION_GLOSS"></span>**automation**
</dt> <dd>

A way to manipulate an application's objects from outside the application. Automation is typically used to create applications that expose objects to programming tools and macro languages, create and manipulate one application's objects from another applications, or to create tools for accessing and manipulating objects.

</dd> <dt>

<span id="com.bind_context_gloss"></span><span id="COM.BIND_CONTEXT_GLOSS"></span>**bind context**
</dt> <dd>

A COM object that implements the [**IBindCtx**](/windows/desktop/api/ObjIdl/nn-objidl-ibindctx) interface. Bind contexts are used in moniker operations to hold references to the objects activated when a moniker is bound. The bind context contains parameters that apply to all operations during the binding of a generic composite moniker and provides the moniker implementation with access to information about its environment.

</dd> <dt>

<span id="com.binding_gloss"></span><span id="COM.BINDING_GLOSS"></span>**binding**
</dt> <dd>

Associating a name with its referent. Specifically, locating the object named by a moniker, putting it into its running state if it isn't already, and returning an interface pointer to it. Objects can be bound at run time (also called late binding or dynamic binding) or at compile time (also called static binding).

</dd> <dt>

<span id="com.cache_gloss"></span><span id="COM.CACHE_GLOSS"></span>**cache**
</dt> <dd>

A (usually temporary) local store of information. In OLE, a cache contains information that defines the presentation of a linked or embedded object when the container is opened.

</dd> <dt>

<span id="com.cache_initialization_gloss"></span><span id="COM.CACHE_INITIALIZATION_GLOSS"></span>**cache initialization**
</dt> <dd>

Filling a linked or embedded object's cache with presentation data. The [**IOleCache**](/windows/desktop/api/OleIdl/nn-oleidl-iolecache) interface provides methods that a container can call to control the data that gets cached for linked or embedded objects.

</dd> <dt>

<span id="com.class_gloss"></span><span id="COM.CLASS_GLOSS"></span>**class**
</dt> <dd>

The definition of an object in code. In C++, the class of an object is defined as a data type, but this is not the case in other languages. Because OLE can be coded in any language, class is used to refer to the general object definition.

</dd> <dt>

<span id="com.class_factory_gloss"></span><span id="COM.CLASS_FACTORY_GLOSS"></span>**class factory**
</dt> <dd>

A COM object that implements the [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) interface and that creates one or more instances of an object identified by a given class identifier(CLSID).

</dd> <dt>

<span id="com.class_identifier_gloss"></span><span id="COM.CLASS_IDENTIFIER_GLOSS"></span>**class identifier (CLSID)**
</dt> <dd>

A globally unique identifier (GUID) associated with an OLE class object. If a class object will be used to create more than one instance of an object, the associated server application should register its CLSID in the system registry so that clients can locate and load the executable code associated with the object(s). Every OLE server or container that allows linking to its embedded objects must register a CLSID for each supported object definition.

</dd> <dt>

<span id="com.class_object_gloss"></span><span id="COM.CLASS_OBJECT_GLOSS"></span>**class object**
</dt> <dd>

In object-oriented programming, an object whose state is shared by all the objects in a class and whose behavior acts on that classwide state data. In COM, class objects are called class factories, and typically have no behavior except to create new instances of the class.

</dd> <dt>

<span id="com.client_gloss"></span><span id="COM.CLIENT_GLOSS"></span>**client**
</dt> <dd>

A COM object that requests services from another object.

</dd> <dt>

<span id="com.client_site_gloss"></span><span id="COM.CLIENT_SITE_GLOSS"></span>**client site**
</dt> <dd>

The display site for an embedded or linked object within a compound document. The client site is the principal means by which an object requests services from its container.

</dd> <dt>

<span id="com.clsid_gloss"></span><span id="COM.CLSID_GLOSS"></span>**CLSID**
</dt> <dd>

A globally unique identifier (GUID) associated with an OLE class object. If a class object will be used to create more than one instance of an object, the associated server application should register its CLSID in the system registry so that clients can locate and load the executable code associated with the object(s). Every OLE server or container that allows linking to its embedded objects must register a CLSID for each supported object definition.

</dd> <dt>

<span id="com.commit_gloss"></span><span id="COM.COMMIT_GLOSS"></span>**commit**
</dt> <dd>

To persistently save any changes made to a storage or stream object since it was opened or changes were last saved.

</dd> <dt>

<span id="com.component_gloss"></span><span id="COM.COMPONENT_GLOSS"></span>**component**
</dt> <dd>

An object that encapsulates both data and code, and provides a well-specified set of publicly available services.

</dd> <dt>

<span id="com.component_object_model_gloss"></span><span id="COM.COMPONENT_OBJECT_MODEL_GLOSS"></span>**Component Object Model (COM)**
</dt> <dd>

The OLE object-oriented programming model that defines how objects interact within a single process or between processes. In COM, clients have access to an object through interfaces implemented on the object.

</dd> <dt>

<span id="com.composite_menu_bar_gloss"></span><span id="COM.COMPOSITE_MENU_BAR_GLOSS"></span>**composite menu bar**
</dt> <dd>

A shared menu bar composed of menu groups from both a container application and an in-place-activated server application.

</dd> <dt>

<span id="com.composite_moniker_gloss"></span><span id="COM.COMPOSITE_MONIKER_GLOSS"></span>**composite moniker**
</dt> <dd>

A moniker that consists of two or more monikers that are treated as a unit. A composite moniker can be non-generic, meaning that its component monikers have special knowledge of each other, or generic, meaning that its component monikers know nothing about each other except that they are monikers

</dd> <dt>

<span id="com.compound_document_gloss"></span><span id="COM.COMPOUND_DOCUMENT_GLOSS"></span>**compound document**
</dt> <dd>

A document that includes linked or embedded objects, as well as its own native data.

</dd> <dt>

<span id="com.compound_file_gloss"></span><span id="COM.COMPOUND_FILE_GLOSS"></span>**compound file**
</dt> <dd>

An OLE-provided Structured Storage implementation.

</dd> <dt>

<span id="com.com_object_gloss"></span><span id="COM.COM_OBJECT_GLOSS"></span>**COM object**
</dt> <dd>

An object that conforms to the OLE Component Object Model (COM). A COM object is an instance of an object definition, which specifies the object's data and one or more implementations of interfaces on the object. Clients interact with a COM object only through its interfaces.

</dd> <dt>

<span id="com.connectable_object_gloss"></span><span id="COM.CONNECTABLE_OBJECT_GLOSS"></span>**connectable object**
</dt> <dd>

A COM object that implements, at a minimum, the [**IConnectionPointContainer**](/windows/desktop/api/OCIdl/nn-ocidl-iconnectionpointcontainer) interface, for the management of connection point objects. Connectable objects support communication from the server to the client. A connectable object creates and manages one or more connection point subobjects, which receive events from interfaces implemented on other objects and send them on to the client.

</dd> <dt>

<span id="com.connection_point_object_gloss"></span><span id="COM.CONNECTION_POINT_OBJECT_GLOSS"></span>**connection point object**
</dt> <dd>

A COM object that is managed by a connectable object and that implements the [**IConnectionPoint**](/windows/desktop/api/OCIdl/nn-ocidl-iconnectionpoint) interface. One or more connection point objects can be created and managed by a connectable object. Each connection point object manages incoming events from a specific interface on another object and sends those events on to the client.

</dd> <dt>

<span id="com.container_application_gloss"></span><span id="COM.CONTAINER_APPLICATION_GLOSS"></span>**container application**
</dt> <dd>

An application that supports compound documents. The container application provides storage for an embedded or linked object, a site for its display, access to the display site, and an advisory sink for receiving notifications of changes in the object.

</dd> <dt>

<span id="com.containment_gloss"></span><span id="COM.CONTAINMENT_GLOSS"></span>**containment**
</dt> <dd>

A composition technique for implementing COM objects. It allows one object to reuse some or all of the interface implementations of one or more other objects. The outer object acts as a client to the other objects, delegating implementation when it wishes to use the services of one of the contained objects.

</dd> <dt>

<span id="com.context_gloss"></span><span id="COM.CONTEXT_GLOSS"></span>**context**
</dt> <dd>

In COM+, a set of run-time properties associated with one or more COM objects that are used to provide services for those objects.

</dd> <dt>

<span id="com.control_gloss"></span><span id="COM.CONTROL_GLOSS"></span>**control**
</dt> <dd>

An embeddable, reusable COM object that supports, at a minimum, the [**IOleControl**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrol) interface. Controls are typically associated with the user interface. They also support communication with a container and can be reused by multiple clients, depending upon licensing criteria.

</dd> <dt>

<span id="com.control_container_gloss"></span><span id="COM.CONTROL_CONTAINER_GLOSS"></span>**control container**
</dt> <dd>

An application that supports embedding of controls by implementing the [**IOleControlSite**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrolsite) interface.

</dd> <dt>

<span id="com.control_property_gloss"></span><span id="COM.CONTROL_PROPERTY_GLOSS"></span>**control property**
</dt> <dd>

A run-time property that is exposed and managed by the control itself. For example, the font and text size used by the control are control properties.

</dd> <dt>

<span id="com.controlling_object_gloss"></span><span id="COM.CONTROLLING_OBJECT_GLOSS"></span>**controlling object**
</dt> <dd>

The object within an aggregate object that controls which interfaces within the aggregate object are exposed and which are private. The [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface of the controlling object is called the controlling **IUnknown**. Calls to **IUnknown** methods of other objects in the aggregate must be passed to the controlling **IUnknown**.

</dd> <dt>

<span id="com.control_site_gloss"></span><span id="COM.CONTROL_SITE_GLOSS"></span>**control site**
</dt> <dd>

A structure implemented by a control container for managing the display and storage of a control. Within a given container, each control has a corresponding control site.

</dd> <dt>

<span id="com.data_transfer_object_gloss"></span><span id="COM.DATA_TRANSFER_OBJECT_GLOSS"></span>**data transfer object**
</dt> <dd>

An object that implements the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) interface and contains data to be transferred from one object to another through either the Clipboard or drag-and-drop operations.

</dd> <dt>

<span id="com.default_object_handler_gloss"></span><span id="COM.DEFAULT_OBJECT_HANDLER_GLOSS"></span>**default object handler**
</dt> <dd>

A DLL provided with OLE that acts as a surrogate in the processing space of the container application for the real object.

With the default object handler, it is possible to look at an object's stored data without actually activating the object. The default object handler performs other tasks, such as rendering an object from its cached state when the object is loaded into memory.

</dd> <dt>

<span id="com.dependent_object_gloss"></span><span id="COM.DEPENDENT_OBJECT_GLOSS"></span>**dependent object**
</dt> <dd>

A COM object that is typically initialized by another object (the host object). Although the dependent object's lifetime may only make sense during the lifetime of the host object, the host object does not function as the controlling [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) for the dependent object. In contrast, an object is an aggregated object when its lifetime (by means of its reference count) is completely controlled by the managing object.

</dd> <dt>

<span id="com.direct_access_mode_gloss"></span><span id="COM.DIRECT_ACCESS_MODE_GLOSS"></span>**direct access mode**
</dt> <dd>

One of two access modes in which a storage object can be opened. In direct mode, all changes are immediately committed to the root storage object.

</dd> <dt>

<span id="com.document_object_gloss"></span><span id="COM.DOCUMENT_OBJECT_GLOSS"></span>**document object**
</dt> <dd>

An OLE document that can display one or more in-place activated views of its data within a native or foreign frame, such as a browser, while retaining full control over its user interface. In addition to implementing the usual OLE document and in-place activation interfaces, a document object must implement [**IOleDocument**](/windows/desktop/api/DocObj/nn-docobj-ioledocument), and each of its views (in the form of a document view object) must implement [**IOleDocumentView**](/windows/desktop/api/DocObj/nn-docobj-ioledocumentview).

</dd> <dt>

<span id="com.document_object_container_gloss"></span><span id="COM.DOCUMENT_OBJECT_CONTAINER_GLOSS"></span>**document object container**
</dt> <dd>

A container application capable of displaying one or more views of one or more document objects and of managing all contained document objects within a file. Each document object is associated with a document site, and each document site contains one or more document view sites corresponding to the views supported by the document object. A document object container also includes a container frame, which handles menu and toolbar negotiation and the enumeration of contained objects.

</dd> <dt>

<span id="com.document_object_server_gloss"></span><span id="COM.DOCUMENT_OBJECT_SERVER_GLOSS"></span>**document object server**
</dt> <dd>

A server application capable of providing document objects.

</dd> <dt>

<span id="com.document_site_gloss"></span><span id="COM.DOCUMENT_SITE_GLOSS"></span>**document site**
</dt> <dd>

A client site implemented by a document object container for managing the display and storage of a document object. Each document object in a container has a corresponding document site.

</dd> <dt>

<span id="com.document_site_object_gloss"></span><span id="COM.DOCUMENT_SITE_OBJECT_GLOSS"></span>**document site object**
</dt> <dd>

A COM object that implements the [**IOleDocumentSite**](/windows/desktop/api/DocObj/nn-docobj-ioledocumentsite) interface, in addition to the usual client-site interfaces (such as [**IOleClientSite**](/windows/desktop/api/OleIdl/nn-oleidl-ioleclientsite)).

</dd> <dt>

<span id="com.document_view_gloss"></span><span id="COM.DOCUMENT_VIEW_GLOSS"></span>**document view**
</dt> <dd>

A particular presentation of a document's data. A single document object can have one or more views, but a single document view can belong to one and only one document object.

</dd> <dt>

<span id="com.document_view_object_gloss"></span><span id="COM.DOCUMENT_VIEW_OBJECT_GLOSS"></span>**document view object**
</dt> <dd>

A COM object that implements the [**IOleDocumentView**](/windows/desktop/api/DocObj/nn-docobj-ioledocumentview) interface and corresponds to a particular document view. An object with multiple document views aggregates a separate document view object for each view.

</dd> <dt>

<span id="com.document_view_site_gloss"></span><span id="COM.DOCUMENT_VIEW_SITE_GLOSS"></span>**document view site**
</dt> <dd>

An object aggregated by a document site object for managing the display space for a particular view of a document object. Within a given document site, each document view has a corresponding document view site.

</dd> <dt>

<span id="com.document_view_site_object_gloss"></span><span id="COM.DOCUMENT_VIEW_SITE_OBJECT_GLOSS"></span>**document view site object**
</dt> <dd>

A COM object that is aggregated in a document site object and implements the [**IOleInPlaceSite**](/windows/desktop/api/OleIdl/nn-oleidl-ioleinplacesite) interface and, optionally, the [**IContinueCallback**](/windows/desktop/api/DocObj/nn-docobj-icontinuecallback) interface.

</dd> <dt>

<span id="com.drag_and_drop_gloss"></span><span id="COM.DRAG_AND_DROP_GLOSS"></span>**drag and drop**
</dt> <dd>

An operation in which the end user uses the mouse or other pointing device to move data to another location in the same window or another window.

</dd> <dt>

<span id="com.embed_gloss"></span><span id="COM.EMBED_GLOSS"></span>**embed**
</dt> <dd>

To insert an object into a compound document in such a way as to preserve the data formats native to that object, and to enable it to be edited from within its container using tools exposed by its server.

</dd> <dt>

<span id="com.embedded_object_gloss"></span><span id="COM.EMBEDDED_OBJECT_GLOSS"></span>**embedded object**
</dt> <dd>

An object whose data is stored in a compound document, but the object runs in the process space of its server. The default object handler provides a surrogate in the processing space of the container application for the real object.

</dd> <dt>

<span id="com.extended_property_gloss"></span><span id="COM.EXTENDED_PROPERTY_GLOSS"></span>**extended property**
</dt> <dd>

A run-time property, such as a control's position and size, that a user would assume to be exposed by the control but is exposed and managed by the container.

</dd> <dt>

<span id="com.file_moniker_gloss"></span><span id="COM.FILE_MONIKER_GLOSS"></span>**file moniker**
</dt> <dd>

A moniker based on a path in the file system. File monikers can be used to identify objects that are saved in their own files. A file moniker is a COM object that supports the system-provided implementation of the [**IMoniker**](/windows/desktop/api/ObjIdl/nn-objidl-imoniker) interface for the file moniker class.

</dd> <dt>

<span id="com.font_object_gloss"></span><span id="COM.FONT_OBJECT_GLOSS"></span>**font object**
</dt> <dd>

A COM object that provides access to Graphics Device Interface (GDI) fonts by implementing the [**IFont**](/windows/desktop/api/OCIdl/nn-ocidl-ifont) interface.

</dd> <dt>

<span id="com.format_identifier_gloss"></span><span id="COM.FORMAT_IDENTIFIER_GLOSS"></span>**format identifier**
</dt> <dd>

A GUID that identifies a persistent property set. Also referred to as FMTID.

</dd> <dt>

<span id="com.frame_gloss"></span><span id="COM.FRAME_GLOSS"></span>**frame**
</dt> <dd>

The part of a container application responsible for negotiating menus, accelerator keys, toolbars, and other shared user-interface elements with an embedded COM object or a document object.

</dd> <dt>

<span id="com.frame_object_gloss"></span><span id="COM.FRAME_OBJECT_GLOSS"></span>**frame object**
</dt> <dd>

A COM object that implements the [**IOleInPlaceFrame**](/windows/desktop/api/OleIdl/nn-oleidl-ioleinplaceframe) interface and, optionally, the [**IOleCommandTarget**](/windows/desktop/api/DocObj/nn-docobj-iolecommandtarget) interface.

</dd> <dt>

<span id="com.generic_composite_moniker_gloss"></span><span id="COM.GENERIC_COMPOSITE_MONIKER_GLOSS"></span>**generic composite moniker**
</dt> <dd>

A sequenced collection of monikers, starting with a file moniker to provide the document-level path and continuing with one or more item monikers that, taken as a whole, uniquely identifies an object.

</dd> <dt>

<span id="com.helper_function_gloss"></span><span id="COM.HELPER_FUNCTION_GLOSS"></span>**helper function**
</dt> <dd>

A function that encapsulates calls to other functions and interface methods publicly available in the OLE SDK. Helper functions are a convenient way to call frequently used sequences of function and method calls that accomplish common tasks.

</dd> <dt>

<span id="com.host_object_gloss"></span><span id="COM.HOST_OBJECT_GLOSS"></span>**host object**
</dt> <dd>

A COM object that forms a hierarchical relationship with one or more other COM objects, known as the dependent objects. Typically, the host object instantiates the dependent objects, and their existence only makes sense within the lifetime of the host object. However, the host object does not act as the controlling [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) for the dependent objects, nor does it directly delegate to the interface implementations of those objects.

</dd> <dt>

<span id="com.hresult_gloss"></span><span id="COM.HRESULT_GLOSS"></span>**HRESULT**
</dt> <dd>

An opaque result handle defined to be zero for a successful return from a function and nonzero if error or status information is returned.

</dd> <dt>

<span id="com.hyperlink_object_gloss"></span><span id="COM.HYPERLINK_OBJECT_GLOSS"></span>**hyperlink object**
</dt> <dd>

A COM object that implements, at a minimum, the [**IHlink**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767974(v=vs.85)) interface and acts as a link to an object at another location (the target). A hyperlink is made up of four parts: a moniker that identifies the target's location; a string for the location within the target; a friendly, or displayable, name for the target; and a string that can contain additional parameters.

</dd> <dt>

<span id="com.hyperlink_browse_context_gloss"></span><span id="COM.HYPERLINK_BROWSE_CONTEXT_GLOSS"></span>**hyperlink browse context**
</dt> <dd>

A COM object that implements the [**IHlinkBrowseContext**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767949(v=vs.85)) interface and maintains the hyperlink navigation stack. The browse context object manages the hyperlink frame window and hyperlink target object's window.

</dd> <dt>

<span id="com.hyperlink_container_gloss"></span><span id="COM.HYPERLINK_CONTAINER_GLOSS"></span>**hyperlink container**
</dt> <dd>

A container application that supports hyperlinks by implementing the [**IHlinkSite**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767933(v=vs.85)) interface and, if the container's objects can be targets of other hyperlinks, the [**IHlinkTarget**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767929(v=vs.85)) interface.

</dd> <dt>

<span id="com.hyperlink_frame_object_gloss"></span><span id="COM.HYPERLINK_FRAME_OBJECT_GLOSS"></span>**hyperlink frame object**
</dt> <dd>

A COM object that implements the [**IHlinkFrame**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767938(v=vs.85)) interface and controls the top-level navigation and display of hyperlinks for the frame's container and the hyperlink target's server.

</dd> <dt>

<span id="com.hyperlink_site_object_gloss"></span><span id="COM.HYPERLINK_SITE_OBJECT_GLOSS"></span>**hyperlink site object**
</dt> <dd>

A COM object that implements the [**IHlinkSite**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767933(v=vs.85)) interface and supplies either the moniker or interface identifier of its hyperlink container. One hyperlink site can serve multiple hyperlinks.

</dd> <dt>

<span id="com.hyperlink_target_object_gloss"></span><span id="COM.HYPERLINK_TARGET_OBJECT_GLOSS"></span>**hyperlink target object**
</dt> <dd>

A COM object that implements the [**IHlinkTarget**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767929(v=vs.85)) interface and supplies its moniker, friendly name, and other information that other hyperlink objects will use to navigate to it.

</dd> <dt>

<span id="com.in_parameter_gloss"></span><span id="COM.IN_PARAMETER_GLOSS"></span>**in parameter**
</dt> <dd>

A parameter that is allocated, set, and freed by the caller of a function or interface method. An in parameter is not modified by the called function.

</dd> <dt>

<span id="com.in_out_parameter_gloss"></span><span id="COM.IN_OUT_PARAMETER_GLOSS"></span>**in/out parameter**
</dt> <dd>

A parameter that is initially allocated by the caller of a function or interface method, and set, freed, and reallocated, if necessary, by the process that is called.

</dd> <dt>

<span id="com.in_place_activation_gloss"></span><span id="COM.IN_PLACE_ACTIVATION_GLOSS"></span>**in-place activation**
</dt> <dd>

Editing an embedded object within the window of its container, using tools provided by the server. Linked objects do not support in-place activation; they are always edited in the window of the server.

</dd> <dt>

<span id="com.in_process_server_gloss"></span><span id="COM.IN_PROCESS_SERVER_GLOSS"></span>**in-process server**
</dt> <dd>

A server implemented as a DLL that runs in the process space of the client.

</dd> <dt>

<span id="com.instance_gloss"></span><span id="COM.INSTANCE_GLOSS"></span>**instance**
</dt> <dd>

An object for which memory is allocated or which is persistent.

</dd> <dt>

<span id="com.interface_gloss"></span><span id="COM.INTERFACE_GLOSS"></span>**interface**
</dt> <dd>

A group of semantically related functions that provide access to a COM object. Each OLE interface defines a contract that allows objects to interact according to the Component Object Model (COM). While OLE provides many interface implementations, most interfaces can also be implemented by developers designing OLE applications.

</dd> <dt>

<span id="com.interface_identifier_iid_gloss"></span><span id="COM.INTERFACE_IDENTIFIER_IID_GLOSS"></span>**interface identifier (IID)**
</dt> <dd>

A globally unique identifier (GUID) associated with an interface. Some functions take IIDs as parameters to allow the caller to specify which interface pointer should be returned.

</dd> <dt>

<span id="com.item_moniker_gloss"></span><span id="COM.ITEM_MONIKER_GLOSS"></span>**item moniker**
</dt> <dd>

A moniker based on a string that identifies an object in a container. Item monikers can identify objects smaller than a file, including embedded objects in a compound document, or a pseudo-object (like a range of cells in a spreadsheet).

</dd> <dt>

<span id="com.licensing_gloss"></span><span id="COM.LICENSING_GLOSS"></span>**licensing**
</dt> <dd>

A feature of COM that provides control over object creation. Licensed objects can be created only by clients that are authorized to use them. Licensing is implemented in COM through the [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2) interface and by support for a license key that can be passed at run time.

</dd> <dt>

<span id="com.link_object_gloss"></span><span id="COM.LINK_OBJECT_GLOSS"></span>**link object**
</dt> <dd>

A COM object that is created when a linked COM object is created or loaded. The link object is provided by OLE and implements the [**IOleLink**](/windows/desktop/api/OleIdl/nn-oleidl-iolelink) interface.

</dd> <dt>

<span id="com.linked_object_gloss"></span><span id="COM.LINKED_OBJECT_GLOSS"></span>**linked object**
</dt> <dd>

A COM object whose source data physically resides where it was initially created. Only a moniker that represents the source data and the appropriate presentation data are kept with the compound document. Changes made to the link source are automatically reflected in the linked object.

</dd> <dt>

<span id="com.link_source_gloss"></span><span id="COM.LINK_SOURCE_GLOSS"></span>**link source**
</dt> <dd>

The data that is the source of a linked object. A link source may be a file or a portion of a file, such as a selected range of cells within a file (also called a pseudo object).

</dd> <dt>

<span id="com.loaded_state_gloss"></span><span id="COM.LOADED_STATE_GLOSS"></span>**loaded state**
</dt> <dd>

The state of an object after its data structures have been loaded into memory and are accessible to the client process.

</dd> <dt>

<span id="com.local_server_gloss"></span><span id="COM.LOCAL_SERVER_GLOSS"></span>**local server**
</dt> <dd>

An out-of-process server implemented as an .EXE application running on the same computer as its client application.

</dd> <dt>

<span id="com.lock_gloss"></span><span id="COM.LOCK_GLOSS"></span>**lock**
</dt> <dd>

A pointer held to-and possibly, a reference count incremented on-a running object. OLE defines two types of locks that can be held on an object: strong and weak. To implement a strong lock, a server must maintain both a pointer and a reference count, so that the object will remain "locked" in memory at least until the server calls [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release). To implement a weak lock, the server maintains only a pointer to the object, so that the object can be destroyed by another process.

</dd> <dt>

<span id="com.marshaling_gloss"></span><span id="COM.MARSHALING_GLOSS"></span>**marshaling**
</dt> <dd>

Packaging and sending interface method calls across thread or process boundaries.

</dd> <dt>

<span id="com.media_type_gloss"></span><span id="COM.MEDIA_TYPE_GLOSS"></span>**media type**
</dt> <dd>

An extension of MIME that allows data format negotiation between a client and an object.

</dd> <dt>

<span id="com.mime_content_type_gloss"></span><span id="COM.MIME_CONTENT_TYPE_GLOSS"></span>**MIME content type**
</dt> <dd>

An extension of MIME that allows data format negotiation between a client and an object.

</dd> <dt>

<span id="com.multipurpose_internet_mail_extension_gloss"></span><span id="COM.MULTIPURPOSE_INTERNET_MAIL_EXTENSION_GLOSS"></span>**Multipurpose Internet Mail Extension (MIME)**
</dt> <dd>

An Internet protocol originally developed to allow exchange of electronic mail messages with rich content across heterogeneous network, computer, and email environments. In practice, MIME has also been adopted and extended by non-mail applications.

</dd> <dt>

<span id="com.moniker_gloss"></span><span id="COM.MONIKER_GLOSS"></span>**moniker**
</dt> <dd>

An object that implements the [**IMoniker**](/windows/desktop/api/ObjIdl/nn-objidl-imoniker) interface. A moniker acts as a name that uniquely identifies a COM object. In the same way that a path identifies a file in the file system, a moniker identifies a COM object in the directory namespace.

</dd> <dt>

<span id="com.moniker_class_gloss"></span><span id="COM.MONIKER_CLASS_GLOSS"></span>**moniker class**
</dt> <dd>

An implementation of the [**IMoniker**](/windows/desktop/api/ObjIdl/nn-objidl-imoniker) interface. System-supplied moniker classes include file monikers, item monikers, generic composite monikers, anti-monikers, pointer monikers, and URL monikers.

</dd> <dt>

<span id="com.moniker_client_gloss"></span><span id="COM.MONIKER_CLIENT_GLOSS"></span>**moniker client**
</dt> <dd>

An application that uses monikers to acquire interface pointers to objects managed by another application.

</dd> <dt>

<span id="com.moniker_provider_gloss"></span><span id="COM.MONIKER_PROVIDER_GLOSS"></span>**moniker provider**
</dt> <dd>

An application that makes available monikers that identify the objects it manages, so that the objects are accessible to other applications.

</dd> <dt>

<span id="com.namespace_extension_gloss"></span><span id="COM.NAMESPACE_EXTENSION_GLOSS"></span>**namespace extension**
</dt> <dd>

An in-process COM object that implements [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder), [**IPersistFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ipersistfolder), and [**IShellView**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellview), which are sometimes referred to as the namespace extension interfaces. A namespace extension is used either to extend the shell's namespace or to create a separate namespace. Primary users are the Windows Explorer and common file dialog boxes.

</dd> <dt>

<span id="com.native_data_gloss"></span><span id="COM.NATIVE_DATA_GLOSS"></span>**native data**
</dt> <dd>

The data used by an OLE server application when editing an embedded object.

</dd> <dt>

<span id="com.object_gloss"></span><span id="COM.OBJECT_GLOSS"></span>**object**
</dt> <dd>

In OLE, a programming structure encapsulating both data and functionality that are defined and allocated as a single unit and for which the only public access is through the programming structure's interfaces. A COM object must support, at a minimum, the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface, which maintains the object's existence while it is being used and provides access to the object's other interfaces.

</dd> <dt>

<span id="com.object_state_gloss"></span><span id="COM.OBJECT_STATE_GLOSS"></span>**object state** 
</dt> <dd>

The relationship between a compound document object in its container and the application responsible for the object's creation: active, passive, loaded, or running. Passive objects are stored on disk or in a database, and the object is not selected or active. In the loaded state, the object's data structures have been loaded into memory, but they are not available for operations such as editing. Running objects are both loaded and available for all operations. Active objects are running objects that have a visible user interface.

</dd> <dt>

<span id="com.object_type_name_gloss"></span><span id="COM.OBJECT_TYPE_NAME_GLOSS"></span>**object type name**
</dt> <dd>

A unique identification string that is stored as part of the information available for an object in the registration database.

</dd> <dt>

<span id="com.ole_gloss"></span><span id="COM.OLE_GLOSS"></span>**OLE**
</dt> <dd>

Microsoft's object-based technology for sharing information and services across process and computer boundaries.

</dd> <dt>

<span id="com.out_of_process_server_gloss"></span><span id="COM.OUT_OF_PROCESS_SERVER_GLOSS"></span>**out-of-process server**
</dt> <dd>

A server, implemented as an .EXE application, which runs outside the process of its client, either on the same computer or a remote computer.

</dd> <dt>

<span id="com.out_parameter_gloss"></span><span id="COM.OUT_PARAMETER_GLOSS"></span>**out parameter**
</dt> <dd>

An out parameter is allocated by the function being called, and freed by caller.

</dd> <dt>

<span id="com.passive_state_gloss"></span><span id="COM.PASSIVE_STATE_GLOSS"></span>**passive state**
</dt> <dd>

The state of a COM object when it is stored (on disk or in a database). The object is not selected or active.

</dd> <dt>

<span id="com.persistent_property_gloss"></span><span id="COM.PERSISTENT_PROPERTY_GLOSS"></span>**persistent property**
</dt> <dd>

Information that can be stored persistently as part of a storage object such as a file or directory. Persistent properties are grouped into property sets, which can be displayed and edited.

A persistent property is different from the run-time properties of objects created with OLE Controls and Automation technologies, which can be used to affect system behavior. The [**PROPVARIANT**](/windows/win32/api/propidl/ns-propidl-propvariant) structure defines all valid types of persistent properties, whereas the **VARIANT** structure defines all valid types of run-time properties.

</dd> <dt>

<span id="com.persistent_storage_gloss"></span><span id="COM.PERSISTENT_STORAGE_GLOSS"></span>**persistent storage**
</dt> <dd>

Storage of a file or object in a medium such as a file system or database so that the object and its data persist when the file is closed and then re-opened at a later time.

</dd> <dt>

<span id="com.picture_object_gloss"></span><span id="COM.PICTURE_OBJECT_GLOSS"></span>**picture object**
</dt> <dd>

A COM object that provides access to GDI images by implementing the [**IPicture**](/windows/desktop/api/OCIdl/nn-ocidl-ipicture) interface.

</dd> <dt>

<span id="com.pointer_moniker_gloss"></span><span id="COM.POINTER_MONIKER_GLOSS"></span>**pointer moniker**
</dt> <dd>

A moniker that maps an interface pointer to an object in memory. Whereas most monikers identify objects that can be persistently stored, pointer monikers identify objects that cannot. They allow such objects to participate in a moniker binding operation.

</dd> <dt>

<span id="com.presentation_data_gloss"></span><span id="COM.PRESENTATION_DATA_GLOSS"></span>**presentation data**
</dt> <dd>

The data used by a container to display embedded or linked objects.

</dd> <dt>

<span id="com.primary_verb_gloss"></span><span id="COM.PRIMARY_VERB_GLOSS"></span>**primary verb**
</dt> <dd>

The action associated with the most common or preferred operation users perform on an object. The primary verb is always defined as verb zero in the system registration database. An object's primary verb is executed by double-clicking on the object.

</dd> <dt>

<span id="com.property_gloss"></span><span id="COM.PROPERTY_GLOSS"></span>**property**
</dt> <dd>

Information that is associated with an object. In OLE, properties fall into two categories: run-time properties and persistent properties. Run-time properties are typically associated with control objects or their containers. For example, background color is a run-time property set by a control's container. Persistent properties are associated with stored objects.

</dd> <dt>

<span id="com.property_frame_gloss"></span><span id="COM.PROPERTY_FRAME_GLOSS"></span>**property frame**
</dt> <dd>

The user interface mechanism that displays one or more property pages for a control. The OLE Controls run-time system provides a standard implementation of a property frame that can be accessed by using the [**OleCreatePropertyFrame**](/windows/desktop/api/OleCtl/nf-olectl-olecreatepropertyframe) helper function.

</dd> <dt>

<span id="com.property_identifier_gloss"></span><span id="COM.PROPERTY_IDENTIFIER_GLOSS"></span>**property identifier**
</dt> <dd>

A four-byte signed integer that identifies a persistent property within a property set.

</dd> <dt>

<span id="com.property_page_gloss"></span><span id="COM.PROPERTY_PAGE_GLOSS"></span>**property page**
</dt> <dd>

A COM object with its own CLSID that is part of a user interface, implemented by a control, and allows the control's properties to be viewed and set. Property page objects implement the [**IPropertyPage**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertypage) interface.

</dd> <dt>

<span id="com.property_page_site_gloss"></span><span id="COM.PROPERTY_PAGE_SITE_GLOSS"></span>**property page site**
</dt> <dd>

The location within a property frame where a property page is displayed. The property frame implements the [**IPropertyPageSite**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertypagesite) interface, which contains methods to manage the sites of each of the property pages supplied by a control.

</dd> <dt>

<span id="com.property_set_gloss"></span><span id="COM.PROPERTY_SET_GLOSS"></span>**property set**
</dt> <dd>

A logically related group of properties that is associated with a persistently stored object. To create, open, delete, or enumerate one or more property sets, implement the [**IPropertySetStorage**](/windows/desktop/api/propidl/nn-propidl-ipropertysetstorage) interface. If you are using compound files, you can use OLE's implementation of this interface rather than implementing your own.

</dd> <dt>

<span id="com.property_set_storage_gloss"></span><span id="COM.PROPERTY_SET_STORAGE_GLOSS"></span>**property set storage**
</dt> <dd>

A COM storage object that holds a property set. A property set storage is a dependent object associated with and managed by a storage object.

</dd> <dt>

<span id="com.property_sheet_gloss"></span><span id="COM.PROPERTY_SHEET_GLOSS"></span>**property sheet**
</dt> <dd>

A set of property pages for one or more objects.

</dd> <dt>

<span id="com.proxy_gloss"></span><span id="COM.PROXY_GLOSS"></span>**proxy**
</dt> <dd>

An interface-specific object that packages parameters for that interface in preparation for a remote method call. A proxy runs in the address space of the sender and communicates with a corresponding stub in the receiver's address space.

</dd> <dt>

<span id="com.proxy_manager_gloss"></span><span id="COM.PROXY_MANAGER_GLOSS"></span>**proxy manager**
</dt> <dd>

In standard marshaling, a proxy that manages all the interface proxies for a single object.

</dd> <dt>

<span id="com.pseudo_object_gloss"></span><span id="COM.PSEUDO_OBJECT_GLOSS"></span>**pseudo object**
</dt> <dd>

A portion of a document or embedded object, such as a range of cells in a spreadsheet, that can be the source for a COM object.

</dd> <dt>

<span id="com.reference_counting_gloss"></span><span id="COM.REFERENCE_COUNTING_GLOSS"></span>**reference counting**
</dt> <dd>

Keeping a count of each interface pointer held on an object to ensure that the object is not destroyed before all references to it are released.

</dd> <dt>

<span id="com.relative_moniker_gloss"></span><span id="COM.RELATIVE_MONIKER_GLOSS"></span>**relative moniker**
</dt> <dd>

A moniker that specifies the location of an object relative to the location of another object. A relative moniker is analogous to a relative path, such as ..\\backup\\report.old.

</dd> <dt>

<span id="com.remote_server_gloss"></span><span id="COM.REMOTE_SERVER_GLOSS"></span>**remote server**
</dt> <dd>

A server application, implemented as an EXE, running on a different computer from the client application using it.

</dd> <dt>

<span id="com.revert_gloss"></span><span id="COM.REVERT_GLOSS"></span>**revert**
</dt> <dd>

To discard any changes made to an object since the last time the changes were committed or the object's storage was opened.

</dd> <dt>

<span id="com.root_storage_object_gloss"></span><span id="COM.ROOT_STORAGE_OBJECT_GLOSS"></span>**root storage object**
</dt> <dd>

The outermost storage object in a document. A root storage object can contain other nested storage and stream objects. For example, a compound document is saved on disk as a series of storage and stream objects within a root storage object.

</dd> <dt>

<span id="com.running_state_gloss"></span><span id="COM.RUNNING_STATE_GLOSS"></span>**running state**
</dt> <dd>

The state of a COM object when its server application is running and it is possible to access its interfaces and receive notification of changes.

</dd> <dt>

<span id="com.running_object_table_gloss"></span><span id="COM.RUNNING_OBJECT_TABLE_GLOSS"></span>**running object table (ROT)**
</dt> <dd>

A globally accessible table on each computer that keeps track of all COM objects in the running state that can be identified by a moniker. Moniker providers register an object in the table, which increments the object's reference count. Before the object can be destroyed, its moniker must be released from the table.

</dd> <dt>

<span id="com.run_time_property_gloss"></span><span id="COM.RUN_TIME_PROPERTY_GLOSS"></span>**run-time property**
</dt> <dd>

Discrete state information associated with a control object or its container. There are three types of run-time properties: ambient properties, control properties, and extended properties.

</dd> <dt>

<span id="com.self_registration_gloss"></span><span id="COM.SELF_REGISTRATION_GLOSS"></span>**self-registration**
</dt> <dd>

The process by which a server can perform its own registry operations.

</dd> <dt>

<span id="com.server_application_gloss"></span><span id="COM.SERVER_APPLICATION_GLOSS"></span>**server application**
</dt> <dd>

An application that can create COM objects. Container applications can then embed or link to these objects.

</dd> <dt>

<span id="com.static_object_gloss"></span><span id="COM.STATIC_OBJECT_GLOSS"></span>**static object**
</dt> <dd>

An object that contains only a presentation, with no native data. A container can treat a static object as though it were a linked or embedded object, except that it is not possible to edit a static object.

A static object can result, for example, from the breaking of a link on a linked object-that is, the server application is unavailable, or the user doesn't want the linked object to be updated anymore.

</dd> <dt>

<span id="com.storage_object_gloss"></span><span id="COM.STORAGE_OBJECT_GLOSS"></span>**storage object**
</dt> <dd>

A COM object that implements the [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) interface. A storage object contains nested storage objects or stream objects, resulting in the equivalent of a directory/file structure within a single file.

</dd> <dt>

<span id="com.stream_object_gloss"></span><span id="COM.STREAM_OBJECT_GLOSS"></span>**stream object**
</dt> <dd>

A COM object that implements the [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface. A stream object is analogous to a file in a directory/file system.

</dd> <dt>

<span id="com.structured_storage_gloss"></span><span id="COM.STRUCTURED_STORAGE_GLOSS"></span>**Structured Storage**
</dt> <dd>

OLE's technology for storing compound files in native file systems.

</dd> <dt>

<span id="com.stub_gloss"></span><span id="COM.STUB_GLOSS"></span>**stub**
</dt> <dd>

When a function's or interface method's parameters are marshaled across a process boundary, the stub is an interface-specific object that unpackages the marshaled parameters and calls the required method. The stub runs in the receiver's address space and communicates with a corresponding proxy in the sender's address space.

</dd> <dt>

<span id="com.stub_manager_gloss"></span><span id="COM.STUB_MANAGER_GLOSS"></span>**stub manager**
</dt> <dd>

Manages all of the interface stubs for a single object.

</dd> <dt>

<span id="com.synchronous_call_gloss"></span><span id="COM.SYNCHRONOUS_CALL_GLOSS"></span>**synchronous call**
</dt> <dd>

A function call that does not allow further instructions in the calling process to be executed until the function returns.

</dd> <dt>

<span id="com.system_registry_gloss"></span><span id="COM.SYSTEM_REGISTRY_GLOSS"></span>**system registry**
</dt> <dd>

A system-wide repository of information supported by Windows, which contains information about the system and its applications, including OLE clients and servers.

</dd> <dt>

<span id="com.transacted_access_mode_gloss"></span><span id="COM.TRANSACTED_ACCESS_MODE_GLOSS"></span>**transacted access mode**
</dt> <dd>

One of two access modes in which a storage object can be opened. When opened in transacted mode, changes are stored in buffers until the root storage object commits its changes.

</dd> <dt>

<span id="com.type_information_gloss"></span><span id="COM.TYPE_INFORMATION_GLOSS"></span>**type information**
</dt> <dd>

Information about an object's class provided by a type library. To provide type information, a COM object implements the [**IProvideClassInfo**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo) interface.

</dd> <dt>

<span id="com.uniform_data_transfer_gloss"></span><span id="COM.UNIFORM_DATA_TRANSFER_GLOSS"></span>**uniform data transfer**
</dt> <dd>

A model for transferring data through the clipboard, drag and drop, or Automation. Objects conforming to this model implement the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) interface. This model replaces DDE (dynamic data exchange).

</dd> <dt>

<span id="com.unmarshaling_gloss"></span><span id="COM.UNMARSHALING_GLOSS"></span>**unmarshaling**
</dt> <dd>

Unpacking parameters that have been sent to a proxy across process boundaries.

</dd> <dt>

<span id="com.universal_resource_locator_gloss"></span><span id="COM.UNIVERSAL_RESOURCE_LOCATOR_GLOSS"></span>**universal resource locator (URL)**
</dt> <dd>

The identifier used by the World Wide Web for the names and locations of objects on the Internet. OLE provides a moniker class, URL moniker, whose implementation can be used to bind a client to objects identified by a URL.

</dd> <dt>

<span id="com.url_moniker_gloss"></span><span id="COM.URL_MONIKER_GLOSS"></span>**URL moniker**
</dt> <dd>

A moniker based on a universal resource locator (URL). A client can use URL monikers to bind to objects that reside on the Internet. The system-supplied URL moniker class supports both synchronous and asynchronous binding.

</dd> </dl>

 

 