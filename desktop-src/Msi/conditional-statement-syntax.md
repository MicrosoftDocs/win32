---
description: This section describes the syntax of conditional statements used by the MsiEvaluateCondition function and the action sequence tables. For more information, see, Examples of Conditional Statement Syntax.
ms.assetid: 6f1657f9-063b-4d57-ad76-95e3dbe25786
title: Conditional Statement Syntax
ms.topic: article
ms.date: 05/31/2018
---

# Conditional Statement Syntax

This section describes the syntax of conditional statements used by the [**MsiEvaluateCondition**](/windows/desktop/api/Msiquery/nf-msiquery-msievaluateconditiona) function and the action [sequence tables](using-a-sequence-table.md). For more information, see, [Examples of Conditional Statement Syntax](examples-of-conditional-statement-syntax.md).

## Summary of Conditional Statement Syntax

This table and the following list summarize the syntax to use in conditional expressions.



| Item                | Syntax                                                                                                          |
|---------------------|-----------------------------------------------------------------------------------------------------------------|
| value               | symbol \| literal \| integer                                                                                    |
| comparison-operator | < \| > \| <= \| >= \| = \| <>                                                                 |
| term                | value \| value comparison-operator value \| ( expression )\|                                                    |
| Boolean-factor      | term \| **NOT** term                                                                                            |
| Boolean-term        | Boolean-factor \| Boolean-factor **AND** term                                                                   |
| expression          | Boolean-term \| Boolean-term **OR** expression                                                                  |
| symbol              | property \| %environment-variable \| $component-action \| ?component-state \| &feature-action \| !feature-state |



 

-   Symbol names and values are case sensitive.
-   Environment variable names are not case sensitive.
-   Literal text must be enclosed between quotation marks ("text").
    > [!Note]  
    > Literal text containing quotation marks cannot be used in conditional statements because there is no escape character for quotation marks inside literal text. To do a comparison against literal text containing quotation marks, the literal text should be put in a property. For example, to verify that the SERVERNAME property does not contain any quotation marks, define a property called QUOTES in the [Property table](property-table.md) with a value of " and change the condition to NOT SERVERNAME><QUOTES.

     

-   Nonexistent property values are treated as empty strings.
-   Floating point numeric values are not supported.
-   Operators and precedence are the same as in the BASIC and SQL languages.
-   Arithmetic operators are not supported.
-   Parentheses can be used to override operator precedence.
-   Operators are not case sensitive.
-   For string comparisons, a tilde "~" prefixed to the operator performs a comparison that is not case sensitive.
-   Comparison of an integer with a string or property value that cannot be converted to an integer is always **msiEvaluateConditionFalse**, except for the comparison operator "<>", which returns **msiEvaluateConditionTrue**.

## Access Prefixes

The following table shows the prefixes to use to access various system and installer information for use in conditional expressions.



| Symbol type          | Prefix | Value                                                     |
|----------------------|--------|-----------------------------------------------------------|
| Installer property   | (none) | Value of property ([Property](property-table.md)) table. |
| Environment variable | %      | Value of environment variable.                            |
| Component table key  | $      | Action state of the component.                            |
| Component table key  | ?      | Installed state of the component.                         |
| Feature table key    | &      | Action state of the feature.                              |
| Feature table key    | !      | Installed state of the feature.                           |



 

## Logical Operators

The following table shows the logical operators in conditional expressions, in order of high-to-low precedence.



| Operator | Meaning                                                 |
|----------|---------------------------------------------------------|
| Not      | Prefix unary operator; inverts state of following term. |
| And      | TRUE if both terms are TRUE.                            |
| Or       | TRUE if either or both terms are TRUE.                  |
| Xor      | TRUE if either but not both terms are TRUE.             |
| Eqv      | TRUE if both terms are TRUE or both terms are FALSE.    |
| Imp      | TRUE if left term is FALSE or right term is TRUE.       |



 

## Comparative Operators

The following table shows the comparison operators used in conditional expressions. These comparison operators can only occur between two values.



| Operator | Meaning                                                     |
|----------|-------------------------------------------------------------|
| =        | TRUE if left value is equal to right value.                 |
| <> | TRUE if left value is not equal to right value.             |
| >     | TRUE if left value is greater than right value.             |
| >=    | TRUE if left value is greater than or equal to right value. |
| <     | TRUE if left value is less than right value.                |
| <=    | TRUE if left value is less than or equal to right value.    |



 

## Substring Operators

The following table shows the substring operators used in conditional expressions. Substring operators can occur between two string values.



| Operator | Meaning                                           |
|----------|---------------------------------------------------|
| >< | TRUE if left string contains the right string.    |
| << | TRUE if left string starts with the right string. |
| >> | TRUE if left string ends with the right string.   |



 

## Bitwise Numeric Operators

The following table shows the bitwise numeric operators in conditional expressions. These operators can occur between two integer values.



| Operator | Meaning                                                                      |
|----------|------------------------------------------------------------------------------|
| >< | Bitwise AND, TRUE if the left and right integers have any bits in common.    |
| << | True if the high 16-bits of the left integer are equal to the right integer. |
| >> | True if the low 16-bits of the left integer are equal to the right integer.  |



 

## Feature and Component State Values

The following table shows where it is valid to use the feature and component operator symbols.



| Operator &lt;state&gt; | Where this syntax is valid                                                                                                                                         |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $component-action      | In the [Condition](condition-table.md) table, and in the [sequence](using-a-sequence-table.md) tables, after the [CostFinalize](costfinalize-action.md) action. |
| &feature-action        | In the [Condition](condition-table.md) table, and in the [sequence](using-a-sequence-table.md) tables, after the [CostFinalize](costfinalize-action.md) action. |
| !feature-state         | In the [Condition](condition-table.md) table, and in the [sequence](using-a-sequence-table.md) tables, after the [CostFinalize](costfinalize-action.md) action. |
| ?component-state       | In the [Condition](condition-table.md) table, and in the [sequence](using-a-sequence-table.md) tables, after the [CostFinalize](costfinalize-action.md) action. |



 

The following table shows the feature and component state values used in conditional expressions. These states are not set until [**MsiSetInstallLevel**](/windows/desktop/api/Msiquery/nf-msiquery-msisetinstalllevel) is called, either directly or by the [CostFinalize](costfinalize-action.md) action.



| State                    | Value | Meaning                                                         |
|--------------------------|-------|-----------------------------------------------------------------|
| INSTALLSTATE\_UNKNOWN    | -1    | No action to be taken on the feature or component.              |
| INSTALLSTATE\_ADVERTISED | 1     | Advertised feature. This state is not available for components. |
| INSTALLSTATE\_ABSENT     | 2     | Feature or component is not present.                            |
| INSTALLSTATE\_LOCAL      | 3     | Feature or component on the local computer.                     |
| INSTALLSTATE\_SOURCE     | 4     | Feature or component run from the source.                       |



 

For example, the conditional expression "&MyFeature=3" evaluates to True only if MyFeature is changing from its current state to the state of being installed on the local computer, INSTALLSTATE\_LOCAL.

Note that you should not depend upon the condition $Component1=3 to check whether Component1 is locally installed on the computer. This can fail if Component1 is installed by more than one product. After Component1 has been installed locally by Product1, the installer evaluates the condition $Component1=3 as False during the installation of Product2. This is because the installer determines the version of the component using the component's key path and marks the component for installation if its version is greater than or equal to the installed component.

Note that the installer will not do direct comparisons of the [Version](version.md) data type in conditional statements. For example, you cannot use comparative operators to compare versions such as "01.10" and "1.010" in a conditional statement. Instead use a valid method to search for a version, such as described in [Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md), and then set a property.

## Related topics

<dl> <dt>

[Using Properties in Conditional Statements](using-properties-in-conditional-statements.md)
</dt> </dl>

 

 



