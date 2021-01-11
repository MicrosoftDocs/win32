---
description: Classic providers should use Managed Object Format (MOF) to publish the layout of their event data. Consumers can then read the published layout from WMI at runtime and use it to read the event data.
ms.assetid: eb3d8422-2352-47cf-9825-cba9916791a9
title: Publishing Your Event Schema for a Classic Provider
ms.topic: article
ms.date: 05/31/2018
---

# Publishing Your Event Schema for a Classic Provider

[Classic](about-event-tracing.md) providers should use [Managed Object Format](../wmisdk/managed-object-format--mof-.md) (MOF) to publish the layout of their event data. Consumers can then read the published layout from WMI at runtime and use it to read the event data.

If you use MOF to publish the layout of your event data in WMI, you typically create the following three types of MOF classes in the root\\wmi namespace:

-   [A provider MOF class](#provider-mof-classes)
-   [One or more event MOF classes](#event-mof-classes)
-   [One or more event type MOF classes](#event-type-mof-classes)

## Provider MOF classes

If you publish the layout of your event data, you must create a MOF class that identifies your provider. This class must derive from the **EventTrace** MOF class and must be empty (no properties or methods). The class must also include the **Guid** qualifier which uniquely identifies the provider. This is the same GUID you use when you calling the [**RegisterTraceGuids**](/windows/win32/api/evntrace/nf-evntrace-registertraceguidsa) function to register your provider.

## Event MOF classes

An event MOF class defines a class of events that the provider provides. This class derives from the provider MOF class and must be empty (no properties or methods). The class must also include the **Guid** qualifier which uniquely identifies the class of events that its child classes define. The provider uses this same GUID when setting the **Guid** member of the [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) structure.

## Event type MOF classes

An event type MOF class defines the actual event data. This class derives from its parent event MOF class. When naming the event type MOF class, the convention is to use the event MOF class name at the beginning of the event type MOF class name. For example, if the event MOF class name is HWConfig and the event type MOF class represents CPU information, you should name the event type MOF class, HWConfig\_CPU.

Use the **EventType** qualifier on the event type MOF class to identify the event type. If multiple event types use the same event data, they can use the same MOF class. The provider uses the same event type value to identify the event when setting the **Class.Type** member of the [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) structure.

The event type MOF class contains properties. The order of these properties define the layout of the event data. The following table identifies the data types and qualifiers you can use to define the properties. For more information on the property and class qualifiers that you can use, see [Event Tracing MOF Qualifiers](event-tracing-mof-qualifiers.md).



| Data type              | Qualifiers                        | Description                                                                                                                                                                                                                                                                                                              |
|------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **sint8**, **uint8**   | **Format**                        | Declares a 1-byte decimal integer. To declare an ANSI character, use the **Format** qualifier and set its value to "c".                                                                                                                                                                                                  |
| **sint16**, **uint16** | **Format**                        | Declares a 2-byte decimal integer. To indicate the number is a hexadecimal number, use the **Format** qualifier. For example, format("x").                                                                                                                                                                               |
| **sint32**, **uint32** | **Format**                        | Declares a 4-byte decimal integer. To indicate the number is a hexadecimal number, use the **Format** qualifier and set its value to "x".                                                                                                                                                                                |
| **sint64**, **uint64** | **Format**                        | Declares a 8-byte decimal integer. To indicate the number is a hexadecimal number, use the **Format** qualifier and set its value to "x".                                                                                                                                                                                |
| **boolean**            |                                   | Declares a Boolean value. The event consumer should interpret the value as BOOL (4-byte integer).                                                                                                                                                                                                                        |
| **char16**             |                                   | Declares a wide character. The event consumer should interpret char16 arrays in kernel events as wide character strings. (Use the array size to copy the string. Some strings may contain leading NULL characters.)                                                                                                      |
| **object**             | **Extension**                     | Declares a binary blob. The **Extension** qualifier indicates the type of data in the blob.                                                                                                                                                                                                                              |
| **string**             | **Format**, **StringTermination** | Declares a string value. To indicate the string is a wide-character string use the **Format** qualifier and set its value to "w". The string is considered an ANSI string if you do not specify the **Format** qualifier. To indicate how the string is terminated, use the **StringTermination** qualifier. <br/> |



 

To specify an array, you can use square brackets, \[\]. The square brackets can include the size of the array. For example:

`[WmiDataId(1), read] uint8 MyGuid[16];`

You can also use the **Max** qualifier to specify the size of an array. For example:

`[WmiDataId(1), Max(16), read] uint8 MyGuid[];`

If you include the size of the array in the square brackets, the MOF compiler generates the Max qualifier for you.

It is important that you use the **Description** qualifier for each property. The description should contain a display name that the consumer can use when displaying the property values.

The following example shows the contents of a MOF file that describes a provider, event, and event type MOF class.

``` syntax
#pragma namespace("\\\\.\\root\\wmi")

[dynamic: ToInstance, Description("Defines my event provider"),
 Guid("{7C214FB1-9CAC-4b8d-BAED-7BF48BF63BB3}")]
class MyProvider : EventTrace
{
};

[dynamic: ToInstance, Description("Defines a category of events that my provider logs."): Amended,
 Guid("{B49D5931-AD85-4070-B1B1-3F81F1532875}")]
class MyCategory : MyProvider
{
};

[dynamic: ToInstance, Description("Defines an event within the category of events that my provider logs."): Amended,
 EventType(1)]
class MyCategory_MyEvent : MyCategory
{
    [WmiDataId(1), Description("Cost factor"): Amended, read] sint32 Cost;
    [WmiDataId(2), Description("Index values"): Amended, read] uint32 Indices[3];
    [WmiDataId(3), Description("Signature"): Amended, read, StringTermination("NullTerminated"), Format("w")] string Signature;
    [WmiDataId(4), Description("Is complete copy"): Amended, read] boolean IsComplete;
    [WmiDataId(5), Description("Class identifier"): Amended, read, Extension("Guid")] object ID;
};
```

Note that the provider, event, and event type MOF class names must be unique within the entire namespace. To avoid naming conflicts, you should use unique and descriptive name for all class names. Class properties should also be descriptive and unique within its class hierarchy—a child class that contains the same property name as a parent class overwrites the property of the parent class.

After defining your MOF classes, use the MOF compiler to generate your event schema and add it to the CIM repository. Consumers can then read the schema from the repository and programmatically read the event data. For a complete description of the MOF syntax and using the MOF compiler (Mofcomp.exe) to add your MOF classes to the CIM repository, see [Managed Object Format](../wmisdk/managed-object-format--mof-.md). For information on using Wbemtest.exe to access the CIM repository, see [Windows Management Instrumentation](../wmisdk/wmi-start-page.md) (WMI).

## Versioning MOF class

If you add or change an event type MOF class, the convention is to version both the event MOF class and its child event type MOF classes. To version the current event MOF class, append \_Vn to the class name, where n is an incremental number starting at 0. If this is the first revision to the class, append \_V0 to the class name. You must also add the **EventVersion** qualifier to the class. Use the same version number you used in the class name for the value of the **EventVersion** qualifier.

The new version of the event MOF class must use the same name and **Guid** qualifier as the original class. The new class may optionally add the **EventVersion** qualifier. The event MOF class that does not contain the **EventVersion** qualifier is considered the latest version, or if all the versions of the class contain an **EventVersion** qualifier, then the class with the highest version number is considered the latest version. The provider uses the **Class.Version** member of the [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) structure to identify the version of the event included in the trace.

The following example shows how to version an event MOF class.

``` syntax
#pragma namespace("\\\\.\\root\\wmi")
#pragma classflags("forceupdate")

[dynamic: ToInstance, Description("Defines my event provider"),
 Guid("{7C214FB1-9CAC-4b8d-BAED-7BF48BF63BB3}")]
class MyProvider : EventTrace
{
};

[dynamic: ToInstance, Description("Defines a category of events that my provider logs."),
 Guid("{B49D5931-AD85-4070-B1B1-3F81F1532875}"),
 EventVersion(1)]
class MyCategory : MyProvider
{
};

[dynamic: ToInstance, Description("Defines an event within the category of events that my provider logs."): Amended,
 EventType(1),
 EventName("MyEvent")]
class MyCategory_MyEvent : MyCategory
{
    [WmiDataId(1), Description("Cost factor"): Amended, read] sint32 Cost;
    [WmiDataId(2), Description("Index values"): Amended, read] uint32 Indices[3];
    [WmiDataId(3), Description("Signature"): Amended, read, StringTermination("NullTerminated"), Format("w")] string Signature;
    [WmiDataId(4), Description("Is complete copy"): Amended, read] boolean IsComplete;
    [WmiDataId(5), Description("Identifier"): Amended, read, Extension("Guid")] object ID;
    [WmiDataId(6), Description("Buffer Size"): Amended, read] uint32 Size;
};

[dynamic: ToInstance, Description("Defines a category of events that my provider logs."): Amended,
 Guid("{B49D5931-AD85-4070-B1B1-3F81F1532875}"),
 EventVersion(0)]
class MyCategory_V0 : MyProvider
{
};

[dynamic: ToInstance, Description("Defines an event within the category of events that my provider logs."): Amended,
 EventType(1)]
class MyCategory_V0_MyEvent : MyCategory_V0
{
    [WmiDataId(1), Description("Cost factor"): Amended, read] sint32 Cost;
    [WmiDataId(2), Description("Index values"): Amended, read] uint32 Indices[3];
    [WmiDataId(3), Description("Signature"): Amended, read, StringTermination("NullTerminated"), Format("w")] string Signature;
    [WmiDataId(4), Description("Is complete copy"): Amended, read] boolean IsComplete;
    [WmiDataId(5), Description("Identifier"): Amended, read, Extension("Guid")] object ID;
};
```

 

 
