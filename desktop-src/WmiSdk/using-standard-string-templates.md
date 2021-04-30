---
description: Several consumers, such as the Active Script Event Consumer or the Command Line Event Consumer, have string properties with the Template qualifier.
ms.assetid: d734c226-e160-4834-a5e8-62390905dfde
ms.tgt_platform: multiple
title: Using Standard String Templates
ms.topic: article
ms.date: 05/31/2018
---

# Using Standard String Templates

Several consumers, such as the Active Script Event Consumer or the Command Line Event Consumer, have string properties with the **Template** qualifier. These properties use standard string templates to construct a string that is configured in part by the consumer instance and in part by an event. The structure of a standard string template is similar to the Microsoft Windows environment variable specification.

The following list shows some examples of the template language:

-   The string "Some text here" always produces the string "Some text here".
-   "%CPUUtilization%" always produces the value of the **CPUUtilization** property of the event being delivered. If the property is not a string, it is converted to a string; for example, "90" or "TRUE".
-   "The CPU utilization of this processor is %CPUUtilization% at this time" embeds the value of the **CPUUtilization** property of the event into the string, producing something like, "The CPU utilization of this processor is 90 at this time".
-   "%TargetInstance.CPUUtilization%" retrieves the value of the **CPUUtilization** property in the embedded instance of the **TargetInstance** property.
-   "%%" produces a single % sign.
-   If the property being retrieved is an array, the entire array is produced in the following format: "(1,5,10,1024)". If there is only one element in the array, the parentheses are omitted. If there are no elements in the array, "()" is produced.
-   If a property is an embedded object, the MOF representation of the object is produced (similar to the [**IWbemClassObject::GetObjectText**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-getobjecttext) method).
-   If a property of an embedded array of objects is requested, it is treated as a property with an array value. For example: %MyEvents.TargetInstance.DriverLetter% could produce '("C:","D:")' if MyEvents is an array of embedded instance modification events.

## String Literals

Anything inside a pair of quotes is considered a string literal and will not be replaced.

The following example shows the string that the compiler sees for "CPU utilization is %CPUUtilization%".

``` syntax
CPU utilization is %CPUUtilization%
```

This string produces the following output.

``` syntax
CPU utilization is 90
```

On the other hand, the string "CPU utilization is \\"%CPUUtilization%\\"" is seen by the compiler as follows.

``` syntax
CPU utilization is "%CPUUtilization%"
```

This string produces the following output, with no variable substitution.

``` syntax
CPU utilization is "%CPUUtilization%"
```

## Related topics

<dl> <dt>

[Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md)
</dt> </dl>

 

 



