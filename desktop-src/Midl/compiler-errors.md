---
title: Compiler Errors
description: List of error messages generated during MIDL compilation.
ms.assetid: 492eacdd-6bd1-49df-9112-3765f6c05f34
keywords:
- errors MIDL , compiler errors
topic_type:
- apiref
api_name:
- Compiler Errors
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Compiler Errors

The following error messages are generated during MIDL compilation:



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="MIDL2000"></span><span id="midl2000"></span><dl> <dt><strong>MIDL2000</strong></dt> </dl></td>
<td><dl> <dt><span id="must_specify__c_ext_for_abstract_declarators"></span><span id="MUST_SPECIFY__C_EXT_FOR_ABSTRACT_DECLARATORS"></span>must specify /c_ext for abstract declarators</dt> <dd> Abstract declarators represent a Microsoft extension to RPC and are not defined in DCE RPC. Therefore, if your file includes abstract declarators, you cannot compile with the <a href="-osf.md"><strong>/osf</strong></a> switch, which enforces strict DCE compatibility. MIDL versions 3.0 and later use the <a href="-c-ext.md"><strong>/c_ext</strong></a> switch as the default; the <strong>/osf</strong> switch turns off the <strong>/c_ext</strong> switch. For information on abstract declarators, see <a href="/windows/desktop/Rpc/the-acf-body">The ACF Body</a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2001"></span><span id="midl2001"></span><dl> <dt><strong>MIDL2001</strong></dt> </dl></td>
<td><dl> <dt><span id="instantiation_of_data_is_illegal__you_must_use__extern__or__static_"></span><span id="INSTANTIATION_OF_DATA_IS_ILLEGAL__YOU_MUST_USE__EXTERN__OR__STATIC_"></span>instantiation of data is illegal; you must use &quot;extern&quot; or &quot;static&quot;</dt> <dd> Declaration and initialization in the IDL file are not compatible with DCE RPC. This feature is a Microsoft extension that is not available when you compile in DCE-compatibility (<a href="-osf.md"><strong>/osf</strong></a>) mode.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2002"></span><span id="midl2002"></span><dl> <dt><strong>MIDL2002</strong></dt> </dl></td>
<td><dl> <dt><span id="compiler_stack_overflow"></span><span id="COMPILER_STACK_OVERFLOW"></span>compiler stack overflow</dt> <dd> The compiler ran out of stack space while processing the IDL file. This problem can occur when the compiler is processing a complex declaration or expression. To solve the problem, simplify the complex declaration or expression.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2003"></span><span id="midl2003"></span><dl> <dt><strong>MIDL2003</strong></dt> </dl></td>
<td><dl> <dt><span id="redefinition"></span><span id="REDEFINITION"></span>redefinition</dt> <dd> This error message can appear under the following circumstances: a type has been redefined; a procedure prototype has been redefined; a member of a structure or union of the same name already exists; a parameter of the same name already exists in the prototype.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2004"></span><span id="midl2004"></span><dl> <dt><strong>MIDL2004</strong></dt> </dl></td>
<td><dl> <dt><span id="_auto_handle__binding_will_be_used"></span><span id="_AUTO_HANDLE__BINDING_WILL_BE_USED"></span>[auto_handle] binding will be used</dt> <dd> No handle type has been defined as the default handle type. The compiler assumes that an auto handle will be used as the binding handle for the specified procedure.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2005"></span><span id="midl2005"></span><dl> <dt><strong>MIDL2005</strong></dt> </dl></td>
<td><dl> <dt><span id="out_of_memory"></span><span id="OUT_OF_MEMORY"></span>out of memory</dt> <dd> The compiler ran out of memory during compilation. Reduce the size or complexity of the IDL file or allocate more memory to the process.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2006"></span><span id="midl2006"></span><dl> <dt><strong>MIDL2006</strong></dt> </dl></td>
<td><dl> <dt><span id="recursive_definition"></span><span id="RECURSIVE_DEFINITION"></span>recursive definition</dt> <dd> A structure or union has been recursively defined. This error can occur when a pointer specification in a nested structure definition is missed.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2007"></span><span id="midl2007"></span><dl> <dt><strong>MIDL2007</strong></dt> </dl></td>
<td><dl> <dt><span id="import_ignored__file_already_imported"></span><span id="IMPORT_IGNORED__FILE_ALREADY_IMPORTED"></span>import ignored; file already imported</dt> <dd> Importing an IDL file is an idempotent operation. Including it more than once has no effect. All but the first import operation are ignored.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2008"></span><span id="midl2008"></span><dl> <dt><strong>MIDL2008</strong></dt> </dl></td>
<td><dl> <dt><span id="sparse_enums_require__c_ext_or__ms_ext"></span><span id="SPARSE_ENUMS_REQUIRE__C_EXT_OR__MS_EXT"></span>sparse enums require /c_ext or /ms_ext</dt> <dd> Assigning values to enumeration constants is not compatible with DCE RPC. If you want to use the Microsoft extensions to MIDL that permit assigning values to enumeration constants,you cannot compile with the <a href="-osf.md"><strong>/osf</strong></a> switch, which enforces strict DCE compatibility. MIDL versions 3.0 and later use the <a href="-c-ext.md"><strong>/c_ext</strong></a> and <a href="-ms-ext.md"><strong>/ms_ext</strong></a> switches as the default; the <strong>/osf</strong> switch turns off these extension switches.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2009"></span><span id="midl2009"></span><dl> <dt><strong>MIDL2009</strong></dt> </dl></td>
<td><dl> <dt><span id="undefined_symbol"></span><span id="UNDEFINED_SYMBOL"></span>undefined symbol</dt> <dd> An undefined symbol has been used in an expression. This error can occur when you use an undefined enumerated value.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2010"></span><span id="midl2010"></span><dl> <dt><strong>MIDL2010</strong></dt> </dl></td>
<td><dl> <dt><span id="type_used_in_ACF_file_not_defined_in_IDL_file"></span><span id="type_used_in_acf_file_not_defined_in_idl_file"></span><span id="TYPE_USED_IN_ACF_FILE_NOT_DEFINED_IN_IDL_FILE"></span>type used in ACF file not defined in IDL file</dt> <dd> An undefined type is being used.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2011"></span><span id="midl2011"></span><dl> <dt><strong>MIDL2011</strong></dt> </dl></td>
<td><dl> <dt><span id="unresolved_type_declaration"></span><span id="UNRESOLVED_TYPE_DECLARATION"></span>unresolved type declaration</dt> <dd> The type reported in the additional error-information field has not been defined elsewhere in the IDL file.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2012"></span><span id="midl2012"></span><dl> <dt><strong>MIDL2012</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_wide-character_constants_requires__ms_ext_or__c_ext"></span><span id="USE_OF_WIDE-CHARACTER_CONSTANTS_REQUIRES__MS_EXT_OR__C_EXT"></span>use of wide-character constants requires /ms_ext or /c_ext</dt> <dd> Wide-character constants are a Microsoft extension to DCE IDL. To use the data type <a href="wchar-t.md"><strong>wchar_t</strong></a>, you cannot compile with the <a href="-osf.md"><strong>/osf</strong></a> switch, which overrides the MIDL compiler default switches <a href="-ms-ext.md"><strong>/ms_ext</strong></a> and <a href="-c-ext.md"><strong>/c_ext</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2013"></span><span id="midl2013"></span><dl> <dt><strong>MIDL2013</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_wide_character_strings_requires__ms_ext_or__c_ext"></span><span id="USE_OF_WIDE_CHARACTER_STRINGS_REQUIRES__MS_EXT_OR__C_EXT"></span>use of wide character strings requires /ms_ext or /c_ext</dt> <dd> Wide-character string constants are a Microsoft extension to DCE IDL. To use the data type <a href="wchar-t.md"><strong>wchar_t</strong></a>, you cannot compile with the <a href="-osf.md"><strong>/osf</strong></a> switch, which overrides the MIDL compiler default switches <a href="-ms-ext.md"><strong>/ms_ext</strong></a> and <a href="-c-ext.md"><strong>/c_ext</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2014"></span><span id="midl2014"></span><dl> <dt><strong>MIDL2014</strong></dt> </dl></td>
<td><dl> <dt><span id="inconsistent_redefinition_of_type_wchar_t"></span><span id="INCONSISTENT_REDEFINITION_OF_TYPE_WCHAR_T"></span>inconsistent redefinition of type wchar_t</dt> <dd> The type <a href="wchar-t.md"><strong>wchar_t</strong></a> has been redefined as a type that is not equivalent to unsigned short DOS *.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2015"></span><span id="midl2015"></span><dl> <dt><strong>MIDL2015</strong></dt> </dl></td>
<td><dl> <dt><span id="importlib_not_found"></span><span id="IMPORTLIB_NOT_FOUND"></span>importlib not found</dt> <dd> The compiler could not find the type library specified by the [ <a href="importlib.md"><strong>importlib</strong></a>] directive. Check to make sure the path and name of the library are correct.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2016"></span><span id="midl2016"></span><dl> <dt><strong>MIDL2016</strong></dt> </dl></td>
<td><dl> <dt><span id="two_library_blocks"></span><span id="TWO_LIBRARY_BLOCKS"></span>two library blocks</dt> <dd> Two library blocks (even with different names) in the same source file are illegal. Combine all the elements into a single library block.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2017"></span><span id="midl2017"></span><dl> <dt><strong>MIDL2017</strong></dt> </dl></td>
<td><dl> <dt><span id="the_dispinterface_statement_requires_a_definition_for_IDispatch"></span><span id="the_dispinterface_statement_requires_a_definition_for_idispatch"></span><span id="THE_DISPINTERFACE_STATEMENT_REQUIRES_A_DEFINITION_FOR_IDISPATCH"></span>the dispinterface statement requires a definition for IDispatch</dt> <dd> This error generally occurs when the files Stdole2.tlb or Oaidl.idl are not imported.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2018"></span><span id="midl2018"></span><dl> <dt><strong>MIDL2018</strong></dt> </dl></td>
<td><dl> <dt><span id="error_accessing_type_library"></span><span id="ERROR_ACCESSING_TYPE_LIBRARY"></span>error accessing type library</dt> <dd> The compiler could not find the specified type library. Check to make sure that you have specified the path correctly.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2019"></span><span id="midl2019"></span><dl> <dt><strong>MIDL2019</strong></dt> </dl></td>
<td><dl> <dt><span id="error_accessing_type_info"></span><span id="ERROR_ACCESSING_TYPE_INFO"></span>error accessing type info</dt> <dd> The imported type library is corrupt, invalid, or only partially constructed.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2020"></span><span id="midl2020"></span><dl> <dt><strong>MIDL2020</strong></dt> </dl></td>
<td><dl> <dt><span id="error_generating_type_library"></span><span id="ERROR_GENERATING_TYPE_LIBRARY"></span>error generating type library</dt> <dd> The type library could not be generated. One possible cause of this error is specifying a path to the IDL file that is longer than 126 characters. Oleaut32.dll does not support path names longer than 126 characters.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2021"></span><span id="midl2021"></span><dl> <dt><strong>MIDL2021</strong></dt> </dl></td>
<td><dl> <dt><span id="duplicate_id"></span><span id="DUPLICATE_ID"></span>duplicate id</dt> <dd> Applications use the <a href="id.md"><strong>id</strong></a> statement in IDL files to specify a DISPID for member functions. The member functions can be either properties or methods of interfaces or dispinterfaces. This error indicates the IDL file specifies the same identifier number for two methods or properties.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2022"></span><span id="midl2022"></span><dl> <dt><strong>MIDL2022</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_or_missing_value_for_entry_attribute"></span><span id="ILLEGAL_OR_MISSING_VALUE_FOR_ENTRY_ATTRIBUTE"></span>illegal or missing value for entry attribute</dt> <dd> The argument for the entry attribute may be either a string that specifies a named entry point, or an ordinal number that defines the entry point. This argument is either missing or it contains an invalid value.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2023"></span><span id="midl2023"></span><dl> <dt><strong>MIDL2023</strong></dt> </dl></td>
<td><dl> <dt><span id="error_recovery_assumes"></span><span id="ERROR_RECOVERY_ASSUMES"></span>error recovery assumes</dt> <dd> The MIDL compiler found illegal characters in the IDL file.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2024"></span><span id="midl2024"></span><dl> <dt><strong>MIDL2024</strong></dt> </dl></td>
<td><dl> <dt><span id="error_recovery_discards"></span><span id="ERROR_RECOVERY_DISCARDS"></span>error recovery discards</dt> <dd> The MIDL compiler found illegal characters in the IDL file. It will ignore the illegal characters.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2025"></span><span id="midl2025"></span><dl> <dt><strong>MIDL2025</strong></dt> </dl></td>
<td><dl> <dt><span id="syntax_error"></span><span id="SYNTAX_ERROR"></span>syntax error</dt> <dd> The compiler detected a syntax error at the specified line.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2026"></span><span id="midl2026"></span><dl> <dt><strong>MIDL2026</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_recover_from_earlier_syntax_errors__aborting_compilation"></span><span id="CANNOT_RECOVER_FROM_EARLIER_SYNTAX_ERRORS__ABORTING_COMPILATION"></span>cannot recover from earlier syntax errors; aborting compilation</dt> <dd> The MIDL compiler automatically tries to recover from syntax errors by adding or removing syntactic elements. This message indicates that despite these attempts to recover, the compiler detected too many errors. Correct the specified error(s) and recompile.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2027"></span><span id="midl2027"></span><dl> <dt><strong>MIDL2027</strong></dt> </dl></td>
<td><dl> <dt><span id="unknown_pragma_option"></span><span id="UNKNOWN_PRAGMA_OPTION"></span>unknown pragma option</dt> <dd> The specified C pragma is not supported in MIDL. Remove the pragma from the IDL file.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2028"></span><span id="midl2028"></span><dl> <dt><strong>MIDL2028</strong></dt> </dl></td>
<td><dl> <dt><span id="feature_not_implemented"></span><span id="FEATURE_NOT_IMPLEMENTED"></span>feature not implemented</dt> <dd> The MIDL feature, although part of the language definition, is not implemented in Microsoft RPC and is not supported by the MIDL compiler. For example, the following language features are not implemented: bitset, pipe, and the international character type. The unimplemented language feature appears in the additional error-information field of the error message.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2029"></span><span id="midl2029"></span><dl> <dt><strong>MIDL2029</strong></dt> </dl></td>
<td><dl> <dt><span id="type_not_implemented"></span><span id="TYPE_NOT_IMPLEMENTED"></span>type not implemented</dt> <dd> The specified data type, although a legal MIDL keyword, is not implemented in Microsoft RPC.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2030"></span><span id="midl2030"></span><dl> <dt><strong>MIDL2030</strong></dt> </dl></td>
<td><dl> <dt><span id="non-pointer_used_in_a_dereference_operation"></span><span id="NON-POINTER_USED_IN_A_DEREFERENCE_OPERATION"></span>non-pointer used in a dereference operation</dt> <dd> A data type that is not a pointer has been associated with pointer operations. You cannot access the object through the specified non-pointer.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2031"></span><span id="midl2031"></span><dl> <dt><strong>MIDL2031</strong></dt> </dl></td>
<td><dl> <dt><span id="expression_has_a_divide_by_zero"></span><span id="EXPRESSION_HAS_A_DIVIDE_BY_ZERO"></span>expression has a divide by zero</dt> <dd> The constant expression contains division by zero.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2032"></span><span id="midl2032"></span><dl> <dt><strong>MIDL2032</strong></dt> </dl></td>
<td><dl> <dt><span id="expression_uses_incompatible_types"></span><span id="EXPRESSION_USES_INCOMPATIBLE_TYPES"></span>expression uses incompatible types</dt> <dd> The left and right sides of the operator in an expression are of incompatible types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2033"></span><span id="midl2033"></span><dl> <dt><strong>MIDL2033</strong></dt> </dl></td>
<td><dl> <dt><span id="nonarray_expression_uses_index_operator"></span><span id="NONARRAY_EXPRESSION_USES_INDEX_OPERATOR"></span>nonarray expression uses index operator</dt> <dd> The expression uses the array-indexing operation on a data item that is not of the array type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2034"></span><span id="midl2034"></span><dl> <dt><strong>MIDL2034</strong></dt> </dl></td>
<td><dl> <dt><span id="left-hand_side_of_expression_does_not_evaluate_to_struct_union_enum"></span><span id="LEFT-HAND_SIDE_OF_EXPRESSION_DOES_NOT_EVALUATE_TO_STRUCT_UNION_ENUM"></span>left-hand side of expression does not evaluate to struct/union/enum</dt> <dd> The direct or indirect reference operator &quot;.&quot; or &quot;->&quot; has been applied to a data object that is not a structure, union, or an enumeration. You cannot obtain a direct or indirect reference using the specified object.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2035"></span><span id="midl2035"></span><dl> <dt><strong>MIDL2035</strong></dt> </dl></td>
<td><dl> <dt><span id="constant_expression_expected"></span><span id="CONSTANT_EXPRESSION_EXPECTED"></span>constant expression expected</dt> <dd> A constant expression was expected in the syntax. For example, array bounds require a constant expression. The compiler issues this error message when the array bound is defined with a variable or undefined symbol.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2036"></span><span id="midl2036"></span><dl> <dt><strong>MIDL2036</strong></dt> </dl></td>
<td><dl> <dt><span id="expression_cannot_be_evaluated_at_compile_time"></span><span id="EXPRESSION_CANNOT_BE_EVALUATED_AT_COMPILE_TIME"></span>expression cannot be evaluated at compile time</dt> <dd> The compiler cannot evaluate an expression at compile time.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2037"></span><span id="midl2037"></span><dl> <dt><strong>MIDL2037</strong></dt> </dl></td>
<td><dl> <dt><span id="expression_not_implemented"></span><span id="EXPRESSION_NOT_IMPLEMENTED"></span>expression not implemented</dt> <dd> A feature that was supported in previous releases of the MIDL compiler is not supported in the version of the compiler supplied with Microsoft RPC. Remove the specified expression.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2038"></span><span id="midl2038"></span><dl> <dt><strong>MIDL2038</strong></dt> </dl></td>
<td><dl> <dt><span id="no__pointer_default__attribute_specified__assuming__unique__for_all_unattributed_pointers"></span><span id="NO__POINTER_DEFAULT__ATTRIBUTE_SPECIFIED__ASSUMING__UNIQUE__FOR_ALL_UNATTRIBUTED_POINTERS"></span>no [pointer_default] attribute specified, assuming [unique] for all unattributed pointers</dt> <dd> The MIDL compiler offers three different default cases for pointers that do not have pointer attributes. Function parameters that are top-level pointers default to [<a href="ref.md"><strong>ref</strong></a>] pointers. Pointers embedded in structures and pointers to other pointers (not top-level pointers) default to the type specified by the [<a href="pointer-default.md"><strong>pointer_default</strong></a>] attribute. When no [<strong>pointer_default</strong>] attribute is supplied, these nontop-level pointers default to unique pointers. This error message indicates the last case: no [<strong>pointer_default</strong>] attribute is supplied, and there is at least one non-top-level pointer that will be treated as a unique pointer. For more information, see <a href="/windows/desktop/Rpc/default-pointer-types">Default Pointer Types</a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2039"></span><span id="midl2039"></span><dl> <dt><strong>MIDL2039</strong></dt> </dl></td>
<td><dl> <dt><span id="interface_is_not_automation_marshaling_conformant"></span><span id="INTERFACE_IS_NOT_AUTOMATION_MARSHALING_CONFORMANT"></span>interface is not automation marshaling conformant</dt> <dd> The interface does not meet the requirements for an OLE Automation interface. Check to make sure the interface is derived from <strong>IUnknown</strong> or <strong>IDispatch</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2040"></span><span id="midl2040"></span><dl> <dt><strong>MIDL2040</strong></dt> </dl></td>
<td><dl> <dt><span id="_out__only_parameter_cannot_be_a_pointer_to_an_open_structure"></span><span id="_OUT__ONLY_PARAMETER_CANNOT_BE_A_POINTER_TO_AN_OPEN_STRUCTURE"></span>[out] only parameter cannot be a pointer to an open structure</dt> <dd> An [<a href="out-idl.md"><strong>out</strong></a>]-only parameter has been used as a pointer to a structure, known as an open structure, whose transmitted range and size are determined at run time. The server stub does not know how much space to allocate for an open structure. Use a pointer to a pointer to the open structure and ensure that the server application allocates sufficient space for it.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2041"></span><span id="midl2041"></span><dl> <dt><strong>MIDL2041</strong></dt> </dl></td>
<td><dl> <dt><span id="_out__only_parameter_cannot_be_an_unsized_string"></span><span id="_OUT__ONLY_PARAMETER_CANNOT_BE_AN_UNSIZED_STRING"></span>[out] only parameter cannot be an unsized string</dt> <dd> An array with the string attribute has been declared as an [<a href="out-idl.md"><strong>out</strong></a>]-only parameter without any size specification. The server stub needs size information to allocate memory for the string. You can remove the string attribute and add the [<a href="size-is.md"><strong>size_is</strong></a>] attribute, or you can change the parameter to an [<strong>in, out</strong>] parameter.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2042"></span><span id="midl2042"></span><dl> <dt><strong>MIDL2042</strong></dt> </dl></td>
<td><dl> <dt><span id="_out__parameter_is_not_a_pointer"></span><span id="_OUT__PARAMETER_IS_NOT_A_POINTER"></span>[out] parameter is not a pointer</dt> <dd> All [<a href="out-idl.md"><strong>out</strong></a>] parameters must be pointers, in keeping with the call-by-value convention of the C programming language. The [<strong>out</strong>] directional parameter indicates that the server transmits a value to the client. With the call-by-value convention, the server can transmit data to the client only if the function argument is a pointer.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2043"></span><span id="midl2043"></span><dl> <dt><strong>MIDL2043</strong></dt> </dl></td>
<td><dl> <dt><span id="open_structure_cannot_be_a_parameter"></span><span id="OPEN_STRUCTURE_CANNOT_BE_A_PARAMETER"></span>open structure cannot be a parameter</dt> <dd> An open structure contains a conformant array as the last element. A structure or union is truncated when the last element of that structure or union is a conformant array.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2044"></span><span id="midl2044"></span><dl> <dt><strong>MIDL2044</strong></dt> </dl></td>
<td><dl> <dt><span id="_out__context_handle_generic_handle_must_be_specified_as_a_pointer_to_that_handle_type"></span><span id="_OUT__CONTEXT_HANDLE_GENERIC_HANDLE_MUST_BE_SPECIFIED_AS_A_POINTER_TO_THAT_HANDLE_TYPE"></span>[out] context handle/generic handle must be specified as a pointer to that handle type</dt> <dd> A context-handle or user-defined handle parameter with the [<a href="out-idl.md"><strong>out</strong></a>] directional attribute must be a pointer to a pointer.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2045"></span><span id="midl2045"></span><dl> <dt><strong>MIDL2045</strong></dt> </dl></td>
<td><dl> <dt><span id="context_handle_must_not_derive_from_a_type_that_has_the__transmit_as__attribute"></span><span id="CONTEXT_HANDLE_MUST_NOT_DERIVE_FROM_A_TYPE_THAT_HAS_THE__TRANSMIT_AS__ATTRIBUTE"></span>context handle must not derive from a type that has the [transmit_as] attribute</dt> <dd> Context handles must be transmitted as context-handle types. They cannot be transmitted as other types and cannot derive from [transmit_is], [<strong>represent_as</strong>], [<strong>wire_marshal</strong>], or [<strong>user_marshal</strong>].<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2046"></span><span id="midl2046"></span><dl> <dt><strong>MIDL2046</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_specify_a_variable_number_of_arguments_to_a_remote_procedure"></span><span id="CANNOT_SPECIFY_A_VARIABLE_NUMBER_OF_ARGUMENTS_TO_A_REMOTE_PROCEDURE"></span>cannot specify a variable number of arguments to a remote procedure</dt> <dd> Remote procedure calls that specify a variable number of arguments at compile time are not compatible with the DCE RPC definition. You cannot use a variable number of arguments in Microsoft RPC.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2047"></span><span id="midl2047"></span><dl> <dt><strong>MIDL2047</strong></dt> </dl></td>
<td><dl> <dt><span id="named_parameter_cannot_be__void_"></span><span id="NAMED_PARAMETER_CANNOT_BE__VOID_"></span>named parameter cannot be &quot;void&quot;</dt> <dd> A parameter with the base type <a href="void.md"><strong>void</strong></a> is specified with a name.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2048"></span><span id="midl2048"></span><dl> <dt><strong>MIDL2048</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_derives_from__coclass__or__module_"></span><span id="PARAMETER_DERIVES_FROM__COCLASS__OR__MODULE_"></span>parameter derives from &quot;coclass&quot; or &quot;module&quot;</dt> <dd> The <a href="coclass.md"><strong>coclass</strong></a> specifies a top-level object that contains interfaces and dispinterfaces. It cannot be passed as a parameter.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2049"></span><span id="midl2049"></span><dl> <dt><strong>MIDL2049</strong></dt> </dl></td>
<td><dl> <dt><span id="only_the_first_parameter_can_be_a_binding_handle__you_must_specify_the__ms_ext_switch"></span><span id="ONLY_THE_FIRST_PARAMETER_CAN_BE_A_BINDING_HANDLE__YOU_MUST_SPECIFY_THE__MS_EXT_SWITCH"></span>only the first parameter can be a binding handle; you must specify the /ms_ext switch</dt> <dd> DCE RPC allows only the first parameter to be a binding handle. Compiling with the <a href="-osf.md"><strong>/osf</strong></a> switch turns off the default <a href="-ms-ext.md"><strong>/ms_ext</strong></a> switch that supports multiple handle parameters and handle parameters in other than the left-most position.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2050"></span><span id="midl2050"></span><dl> <dt><strong>MIDL2050</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_use__comm_status__on_both_a_parameter_and_a_return_type"></span><span id="CANNOT_USE__COMM_STATUS__ON_BOTH_A_PARAMETER_AND_A_RETURN_TYPE"></span>cannot use [comm_status] on both a parameter and a return type</dt> <dd> Both the procedure and one of its parameters have the [<a href="comm-status.md"><strong>comm_status</strong></a>] attribute. The [<strong>comm_status</strong>] attribute specifies that only one data object at a time can be of type <a href="error-status-t.md"><strong>error_status_t</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2051"></span><span id="midl2051"></span><dl> <dt><strong>MIDL2051</strong></dt> </dl></td>
<td><dl> <dt><span id="__local__attribute_on_a_procedure_requires__ms_ext"></span><span id="__LOCAL__ATTRIBUTE_ON_A_PROCEDURE_REQUIRES__MS_EXT"></span> [local] attribute on a procedure requires /ms_ext</dt> <dd> The [<a href="local.md"><strong>local</strong></a>] attribute is a Microsoft extension to DCE IDL. To use this attribute on a function, you cannot compile with the <a href="-osf.md"><strong>/osf</strong></a> switch. The <strong>/osf</strong> switch overrides the MIDL compiler default switches <a href="-ms-ext.md"><strong>/ms_ext</strong></a> and <a href="-c-ext.md"><strong>/c_ext</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2052"></span><span id="midl2052"></span><dl> <dt><strong>MIDL2052</strong></dt> </dl></td>
<td><dl> <dt><span id="property_attributes_may_only_be_used_with_procedures"></span><span id="PROPERTY_ATTRIBUTES_MAY_ONLY_BE_USED_WITH_PROCEDURES"></span>property attributes may only be used with procedures</dt> <dd> Improper usage of a [<a href="propget.md"><strong>propget</strong></a>], [<a href="propput.md"><strong>propput</strong></a>], or [<a href="propputref.md"><strong>propputref</strong></a>] attribute. Check to be sure that you have spelled the property's function name correctly and that the property and function have the same name.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2053"></span><span id="midl2053"></span><dl> <dt><strong>MIDL2053</strong></dt> </dl></td>
<td><dl> <dt><span id="a_procedure_may_not_have_more_than_one_property_attribute"></span><span id="A_PROCEDURE_MAY_NOT_HAVE_MORE_THAN_ONE_PROPERTY_ATTRIBUTE"></span>a procedure may not have more than one property attribute</dt> <dd> At most, only one of the [<a href="propget.md"><strong>propget</strong></a>], [<a href="propput.md"><strong>propput</strong></a>], or [<a href="propputref.md"><strong>propputref</strong></a>] attributes can be specified for a function.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2054"></span><span id="midl2054"></span><dl> <dt><strong>MIDL2054</strong></dt> </dl></td>
<td><dl> <dt><span id="the_procedure_has_an_illegal_combination_of_operation_attributes"></span><span id="THE_PROCEDURE_HAS_AN_ILLEGAL_COMBINATION_OF_OPERATION_ATTRIBUTES"></span>the procedure has an illegal combination of operation attributes</dt> <dd> Certain attributes cannot be used in connection with other attributes. Check the MIDL Language Reference for the exact requirements and syntax of the attributes used in this procedure.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2055"></span><span id="midl2055"></span><dl> <dt><strong>MIDL2055</strong></dt> </dl></td>
<td><dl> <dt><span id="field_deriving_from_a_conformant_array_must_be_the_last_member_of_the_structure"></span><span id="FIELD_DERIVING_FROM_A_CONFORMANT_ARRAY_MUST_BE_THE_LAST_MEMBER_OF_THE_STRUCTURE"></span>field deriving from a conformant array must be the last member of the structure</dt> <dd> The structure contains a conformant array that is not the last element in the structure. The conformant array must appear as the last structure element.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2056"></span><span id="midl2056"></span><dl> <dt><strong>MIDL2056</strong></dt> </dl></td>
<td><dl> <dt><span id="duplicate__case__label"></span><span id="DUPLICATE__CASE__LABEL"></span>duplicate [case] label</dt> <dd> A duplicate case label has been specified. The duplicate label is displayed.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2057"></span><span id="midl2057"></span><dl> <dt><strong>MIDL2057</strong></dt> </dl></td>
<td><dl> <dt><span id="no__default__case_specified_for_discriminated_union"></span><span id="NO__DEFAULT__CASE_SPECIFIED_FOR_DISCRIMINATED_UNION"></span>no [default] case specified for discriminated union</dt> <dd> A discriminated union has been specified without a default case.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2058"></span><span id="midl2058"></span><dl> <dt><strong>MIDL2058</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_expression_cannot_be_resolved"></span><span id="ATTRIBUTE_EXPRESSION_CANNOT_BE_RESOLVED"></span>attribute expression cannot be resolved</dt> <dd> The expression associated with the attribute cannot be resolved. This error usually occurs when a variable that appears in the expression is not defined. For example, the error can occur when the variable <em>s</em> is not defined and is used by the attribute [<a href="size-is.md"><strong>size_is</strong></a>].<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2059"></span><span id="midl2059"></span><dl> <dt><strong>MIDL2059</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_expression_must_be_of_integral_type__no_support_for_64-bit_expressions"></span><span id="ATTRIBUTE_EXPRESSION_MUST_BE_OF_INTEGRAL_TYPE__NO_SUPPORT_FOR_64-BIT_EXPRESSIONS"></span>attribute expression must be of integral type, no support for 64-bit expressions</dt> <dd> The specified attribute variable or expression must be an integral type. This error occurs when the attribute-expression type does not resolve to an integer.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2060"></span><span id="midl2060"></span><dl> <dt><strong>MIDL2060</strong></dt> </dl></td>
<td><dl> <dt><span id="_byte_count__requires__ms_ext"></span><span id="_BYTE_COUNT__REQUIRES__MS_EXT"></span>[byte_count] requires /ms_ext</dt> <dd> The [<a href="byte-count.md"><strong>byte_count</strong></a>] attribute is a Microsoft extension to DCE IDL. To use this attribute you cannot compile with the <a href="-osf.md"><strong>/osf</strong></a> switch, which overrides the MIDL compiler default switches <a href="-ms-ext.md"><strong>/ms_ext</strong></a> and <a href="-c-ext.md"><strong>/c_ext</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2061"></span><span id="midl2061"></span><dl> <dt><strong>MIDL2061</strong></dt> </dl></td>
<td><dl> <dt><span id="_byte_count__can_be_applied_only_to_out_parameters_of_pointer_type"></span><span id="_BYTE_COUNT__CAN_BE_APPLIED_ONLY_TO_OUT_PARAMETERS_OF_POINTER_TYPE"></span>[byte_count] can be applied only to out parameters of pointer type</dt> <dd> The [<a href="byte-count.md"><strong>byte_count</strong></a>] attribute can only be applied to [<a href="out-idl.md"><strong>out</strong></a>] parameters, and all [<strong>out</strong>] parameters must be pointer types.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2062"></span><span id="midl2062"></span><dl> <dt><strong>MIDL2062</strong></dt> </dl></td>
<td><dl> <dt><span id="_byte_count__cannot_be_specified_on_a_pointer_to_a_conformant_array_or_structure"></span><span id="_BYTE_COUNT__CANNOT_BE_SPECIFIED_ON_A_POINTER_TO_A_CONFORMANT_ARRAY_OR_STRUCTURE"></span>[byte_count] cannot be specified on a pointer to a conformant array or structure</dt> <dd> The [<a href="byte-count.md"><strong>byte_count</strong></a>] attribute cannot be applied to a conformant array or structure.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2063"></span><span id="midl2063"></span><dl> <dt><strong>MIDL2063</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_specifying_the_byte_count_is_not__in__only_or_byte_count_parameter_is_not__out__only"></span><span id="PARAMETER_SPECIFYING_THE_BYTE_COUNT_IS_NOT__IN__ONLY_OR_BYTE_COUNT_PARAMETER_IS_NOT__OUT__ONLY"></span>parameter specifying the byte count is not [in] only or byte count parameter is not [out] only</dt> <dd> The value associated with the [<a href="byte-count.md"><strong>byte_count</strong></a>] must be transmitted from the client to the server; it must be an [<a href="in.md"><strong>in</strong></a>] parameter. The [<strong>byte_count</strong>] parameter does not need to be an [<strong>in, out</strong>] parameter.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2064"></span><span id="midl2064"></span><dl> <dt><strong>MIDL2064</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_specifying_the_byte_count_is_not_an_integral_type"></span><span id="PARAMETER_SPECIFYING_THE_BYTE_COUNT_IS_NOT_AN_INTEGRAL_TYPE"></span>parameter specifying the byte count is not an integral type</dt> <dd> The value associated with the byte count must be the integer type <a href="int.md"><strong>int</strong></a>, <a href="small.md"><strong>small</strong></a>, <a href="short.md"><strong>short</strong></a>, or <a href="long.md"><strong>long</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2065"></span><span id="midl2065"></span><dl> <dt><strong>MIDL2065</strong></dt> </dl></td>
<td><dl> <dt><span id="_byte_count__cannot_be_specified_on_a_parameter_with_size_attributes"></span><span id="_BYTE_COUNT__CANNOT_BE_SPECIFIED_ON_A_PARAMETER_WITH_SIZE_ATTRIBUTES"></span>[byte_count] cannot be specified on a parameter with size attributes</dt> <dd> The [<a href="byte-count.md"><strong>byte_count</strong></a>] attribute cannot be used with other size attributes such as [<a href="size-is.md"><strong>size_is</strong></a>] or [<a href="length-is.md"><strong>length_is</strong></a>].<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2066"></span><span id="midl2066"></span><dl> <dt><strong>MIDL2066</strong></dt> </dl></td>
<td><dl> <dt><span id="_case__expression_is_not_constant"></span><span id="_CASE__EXPRESSION_IS_NOT_CONSTANT"></span>[case] expression is not constant</dt> <dd> The expression specified for the case label is not a constant.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2067"></span><span id="midl2067"></span><dl> <dt><strong>MIDL2067</strong></dt> </dl></td>
<td><dl> <dt><span id="_case__expression_is_not_of_integral_type"></span><span id="_CASE__EXPRESSION_IS_NOT_OF_INTEGRAL_TYPE"></span>[case] expression is not of integral type</dt> <dd> The expression specified for the case label is not an integer type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2068"></span><span id="midl2068"></span><dl> <dt><strong>MIDL2068</strong></dt> </dl></td>
<td><dl> <dt><span id="specifying__context_handle__on_a_type_other_than_void___requires__ms_ext"></span><span id="SPECIFYING__CONTEXT_HANDLE__ON_A_TYPE_OTHER_THAN_VOID___REQUIRES__MS_EXT"></span>specifying [context_handle] on a type other than void * requires /ms_ext</dt> <dd> For DCE-RPC compatibility, the context handle must be a pointer of type <strong>void *</strong>. If you want the context handles to be associated with types other than <strong>void *</strong>, do not use the MIDL compiler switch <a href="-osf.md"><strong>/osf</strong></a>, which overrides the MIDL compiler default switch <a href="-ms-ext.md"><strong>/ms_ext</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2069"></span><span id="midl2069"></span><dl> <dt><strong>MIDL2069</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_specify_more_than_one_parameter_with_each_of_comm_status_fault_status"></span><span id="CANNOT_SPECIFY_MORE_THAN_ONE_PARAMETER_WITH_EACH_OF_COMM_STATUS_FAULT_STATUS"></span>cannot specify more than one parameter with each of comm_status/fault_status</dt> <dd> A procedure can have only one parameter with the [<a href="comm-status.md"><strong>comm_status</strong></a>] attribute. It can have at most one parameter with the [<a href="fault-status.md"><strong>fault_status</strong></a>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2070"></span><span id="midl2070"></span><dl> <dt><strong>MIDL2070</strong></dt> </dl></td>
<td><dl> <dt><span id="comm_status_fault_status_parameter_must_be_an__out__only_pointer_parameter"></span><span id="COMM_STATUS_FAULT_STATUS_PARAMETER_MUST_BE_AN__OUT__ONLY_POINTER_PARAMETER"></span>comm_status/fault_status parameter must be an [out] only pointer parameter</dt> <dd> The error-code types [<a href="comm-status.md"><strong>comm_status</strong></a>] and [<a href="fault-status.md"><strong>fault_status</strong></a>] are transmitted from server to client and therefore must be specified as an [<a href="out-idl.md"><strong>out</strong></a>] parameter. Due to the constraints in the C-programming language, all [<strong>out</strong>] parameters must be pointers.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2071"></span><span id="midl2071"></span><dl> <dt><strong>MIDL2071</strong></dt> </dl></td>
<td><dl> <dt><span id="endpoint_syntax_error"></span><span id="ENDPOINT_SYNTAX_ERROR"></span>endpoint syntax error</dt> <dd> The endpoint syntax is incorrect.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2072"></span><span id="midl2072"></span><dl> <dt><strong>MIDL2072</strong></dt> </dl></td>
<td><dl> <dt><span id="inapplicable_attribute"></span><span id="INAPPLICABLE_ATTRIBUTE"></span>inapplicable attribute</dt> <dd> The specified attribute cannot be applied in this construct. For example, the string attribute applies to <a href="char-idl.md"><strong>char</strong></a> arrays or <strong>char</strong> pointers and cannot be applied to a structure that consists of two <a href="short.md"><strong>short</strong></a> integers: <br/>
<pre class="syntax" data-space="preserve"><code>typedef [string] struct moo 
{
    short x;
    short y;
};</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2073"></span><span id="midl2073"></span><dl> <dt><strong>MIDL2073</strong></dt> </dl></td>
<td><dl> <dt><span id="_allocate__requires__ms_ext"></span><span id="_ALLOCATE__REQUIRES__MS_EXT"></span>[allocate] requires /ms_ext</dt> <dd> The <a href="allocate.md"><strong>allocate</strong></a> attribute represents a Microsoft extension that is not defined as part of DCE RPC. To use this attribute, you cannot compile with the <a href="-osf.md"><strong>/osf</strong></a> switch, which overrides the MIDL compiler default switch <a href="-ms-ext.md"><strong>/ms_ext</strong></a><br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2074"></span><span id="midl2074"></span><dl> <dt><strong>MIDL2074</strong></dt> </dl></td>
<td><dl> <dt><span id="invalid__allocate__mode"></span><span id="INVALID__ALLOCATE__MODE"></span>invalid [allocate] mode</dt> <dd> An invalid mode for the [<a href="allocate.md"><strong>allocate</strong></a>] attribute construct has been specified. The four valid modes are single_node, all_nodes, on_null, and always.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2075"></span><span id="midl2075"></span><dl> <dt><strong>MIDL2075</strong></dt> </dl></td>
<td><dl> <dt><span id="length_attributes_cannot_be_applied_with_string_attribute"></span><span id="LENGTH_ATTRIBUTES_CANNOT_BE_APPLIED_WITH_STRING_ATTRIBUTE"></span>length attributes cannot be applied with string attribute</dt> <dd> When the string attribute is used, the generated stub files call the <strong>strlen</strong> function to determine the string length. Don't use the length attribute and the string attribute for the same variable.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2076"></span><span id="midl2076"></span><dl> <dt><strong>MIDL2076</strong></dt> </dl></td>
<td><dl> <dt><span id="_last_is__and__length_is__cannot_be_specified_at_the_same_time"></span><span id="_LAST_IS__AND__LENGTH_IS__CANNOT_BE_SPECIFIED_AT_THE_SAME_TIME"></span>[last_is] and [length_is] cannot be specified at the same time</dt> <dd> Both [<a href="last-is.md"><strong>last_is</strong></a>] and [<a href="length-is.md"><strong>length_is</strong></a>] have been specified for the same array. These attributes are related as follows: length = last   first + 1. Because each value can be derived from the other, don't specify both.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2077"></span><span id="midl2077"></span><dl> <dt><strong>MIDL2077</strong></dt> </dl></td>
<td><dl> <dt><span id="_max_is__and__size_is__cannot_be_specified_at_the_same_time"></span><span id="_MAX_IS__AND__SIZE_IS__CANNOT_BE_SPECIFIED_AT_THE_SAME_TIME"></span>[max_is] and [size_is] cannot be specified at the same time</dt> <dd> Both [ <a href="max-is.md"><strong>max_is</strong></a>] and [ <a href="size-is.md"><strong>size_is</strong></a>] have been specified for the same array. These attributes are related as follows: max = size + 1. Because each value can be derived from the other, don't specify both.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2078"></span><span id="midl2078"></span><dl> <dt><strong>MIDL2078</strong></dt> </dl></td>
<td><dl> <dt><span id="no__switch_is__attribute_specified_at_use_of_union"></span><span id="NO__SWITCH_IS__ATTRIBUTE_SPECIFIED_AT_USE_OF_UNION"></span>no [switch_is] attribute specified at use of union</dt> <dd> No discriminant has been specified for the union. The [<a href="switch-is.md"><strong>switch_is</strong></a>] attribute indicates the discriminant used to select among the union fields.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2079"></span><span id="midl2079"></span><dl> <dt><strong>MIDL2079</strong></dt> </dl></td>
<td><dl> <dt><span id="no__uuid__specified"></span><span id="NO__UUID__SPECIFIED"></span>no [uuid] specified</dt> <dd> No UUID has been specified for the interface.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2080"></span><span id="midl2080"></span><dl> <dt><strong>MIDL2080</strong></dt> </dl></td>
<td><dl> <dt><span id="_uuid__ignored_on__local__interface"></span><span id="_UUID__IGNORED_ON__LOCAL__INTERFACE"></span>[uuid] ignored on [local] interface</dt> <dd> Using the [<a href="local.md"><strong>local</strong></a>] attribute on an object interface causes the MIDL compiler to ignore the [<a href="uuid.md"><strong>uuid</strong></a>] attribute. You cannot use both attributes on an RPC interface.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2081"></span><span id="midl2081"></span><dl> <dt><strong>MIDL2081</strong></dt> </dl></td>
<td><dl> <dt><span id="type_mismatch_between_length_and_size_attribute_expressions"></span><span id="TYPE_MISMATCH_BETWEEN_LENGTH_AND_SIZE_ATTRIBUTE_EXPRESSIONS"></span>type mismatch between length and size attribute expressions</dt> <dd> The length and size attribute expressions must be of the same types. For example, this warning is issued when the attribute variable for the [<a href="size-is.md"><strong>size_is</strong></a>] expression is of type <strong>unsigned long</strong> and the attribute variable for the [<a href="length-is.md"><strong>length_is</strong></a>] expression is of type <a href="long.md"><strong>long</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2082"></span><span id="midl2082"></span><dl> <dt><strong>MIDL2082</strong></dt> </dl></td>
<td><dl> <dt><span id="_string__attribute_must_be_specified__byte____char___or__wchar_t__array_or_pointer"></span><span id="_STRING__ATTRIBUTE_MUST_BE_SPECIFIED__BYTE____CHAR___OR__WCHAR_T__ARRAY_OR_POINTER"></span>[string] attribute must be specified &quot;byte,&quot; &quot;char,&quot; or &quot;wchar_t&quot; array or pointer</dt> <dd> A string attribute cannot be applied to a pointer or array whose base type is not a <a href="byte.md"><strong>byte</strong></a>, <a href="char-idl.md"><strong>char</strong></a>, or <a href="struct.md"><strong>struct</strong></a> in which the members are all of the <strong>byte</strong> or <strong>char</strong> type.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2083"></span><span id="midl2083"></span><dl> <dt><strong>MIDL2083</strong></dt> </dl></td>
<td><dl> <dt><span id="mismatch_between_the_type_of_the__switch_is__expression_and_the_switch_type_of_the_union"></span><span id="MISMATCH_BETWEEN_THE_TYPE_OF_THE__SWITCH_IS__EXPRESSION_AND_THE_SWITCH_TYPE_OF_THE_UNION"></span>mismatch between the type of the [switch_is] expression and the switch type of the union</dt> <dd> If the union [<a href="switch-type.md"><strong>switch_type</strong></a>] is not specified, the switch type is the same type as the [<a href="switch-is.md"><strong>switch_is</strong></a>] field.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2084"></span><span id="midl2084"></span><dl> <dt><strong>MIDL2084</strong></dt> </dl></td>
<td><dl> <dt><span id="_transmit_as__must_not_be_applied_to_a_type_that_derives_from_a_context_handle"></span><span id="_TRANSMIT_AS__MUST_NOT_BE_APPLIED_TO_A_TYPE_THAT_DERIVES_FROM_A_CONTEXT_HANDLE"></span>[transmit_as] must not be applied to a type that derives from a context handle</dt> <dd> Context handles cannot be transmitted as other types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2085"></span><span id="midl2085"></span><dl> <dt><strong>MIDL2085</strong></dt> </dl></td>
<td><dl> <dt><span id="_transmit_as__must_specify_a_transmissible_type"></span><span id="_TRANSMIT_AS__MUST_SPECIFY_A_TRANSMISSIBLE_TYPE"></span>[transmit_as] must specify a transmissible type</dt> <dd> The specified [<a href="transmit-as.md"><strong>transmit_as</strong></a>] type derives from a type that cannot be transmitted by Microsoft RPC, such as <a href="void.md"><strong>void</strong></a>, <strong>void *</strong>, or <a href="int.md"><strong>int</strong></a>. Use a defined RPC base type; in the case of <strong>int</strong>, add size specifiers like <a href="small.md"><strong>small</strong></a>, <a href="short.md"><strong>short</strong></a>, or <a href="long.md"><strong>long</strong></a> to qualify the <strong>int</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2086"></span><span id="midl2086"></span><dl> <dt><strong>MIDL2086</strong></dt> </dl></td>
<td><dl> <dt><span id="transmitted_type_for__transmit_as__and__represent_as__must_not_be_a_pointer_or_derive_from_a_pointer"></span><span id="TRANSMITTED_TYPE_FOR__TRANSMIT_AS__AND__REPRESENT_AS__MUST_NOT_BE_A_POINTER_OR_DERIVE_FROM_A_POINTER"></span>transmitted type for [transmit_as] and [represent_as] must not be a pointer or derive from a pointer</dt> <dd> The transmitted type cannot be a pointer or derive from a pointer.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2087"></span><span id="midl2087"></span><dl> <dt><strong>MIDL2087</strong></dt> </dl></td>
<td><dl> <dt><span id="presented_type_for__transmit_as__and__represent_as__must_not_derive_from_a_conformant_varying_array__its_pointer_equivalent__or_a_conformant_varying_structure"></span><span id="PRESENTED_TYPE_FOR__TRANSMIT_AS__AND__REPRESENT_AS__MUST_NOT_DERIVE_FROM_A_CONFORMANT_VARYING_ARRAY__ITS_POINTER_EQUIVALENT__OR_A_CONFORMANT_VARYING_STRUCTURE"></span>presented type for [transmit_as] and [represent_as] must not derive from a conformant/varying array, its pointer equivalent, or a conformant/varying structure</dt> <dd> The type to which [<a href="transmit-as.md"><strong>transmit_as</strong></a>] has been applied cannot derive from a conformant array or structure (an array or structure whose size is determined at run time).<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2088"></span><span id="midl2088"></span><dl> <dt><strong>MIDL2088</strong></dt> </dl></td>
<td><dl> <dt><span id="_uuid__format_is_incorrect"></span><span id="_UUID__FORMAT_IS_INCORRECT"></span>[uuid] format is incorrect</dt> <dd> The UUID format does not conform to specification. The UUID must be a string that consists of five sequences of hexadecimal digits of length 8, 4, 4, 4, and 12 digits. &quot;12345678-1234-ABCD-EF01-28A49C28F17D&quot; is a valid UUID. Use the function <a href="/windows/desktop/api/rpcdce/nf-rpcdce-uuidcreate"><strong>UuidCreate</strong></a> or a utility to generate a valid UUID.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2089"></span><span id="midl2089"></span><dl> <dt><strong>MIDL2089</strong></dt> </dl></td>
<td><dl> <dt><span id="uuid_is_not_a_hexadecimal_number"></span><span id="UUID_IS_NOT_A_HEXADECIMAL_NUMBER"></span>uuid is not a hexadecimal number</dt> <dd> The UUID specified for the interface contains characters that are invalid in a hexadecimal number representation. The characters 0 through 9 and A through F are valid in a hexadecimal representation.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2090"></span><span id="midl2090"></span><dl> <dt><strong>MIDL2090</strong></dt> </dl></td>
<td><dl> <dt><span id="optional_parameters_must_come_after_required_parameters"></span><span id="OPTIONAL_PARAMETERS_MUST_COME_AFTER_REQUIRED_PARAMETERS"></span>optional parameters must come after required parameters</dt> <dd> For a description of the ordering of parameter lists, see [<a href="optional.md"><strong>optional</strong></a>] in the MIDL Language Reference.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2091"></span><span id="midl2091"></span><dl> <dt><strong>MIDL2091</strong></dt> </dl></td>
<td><dl> <dt><span id="_dllname__required_when__entry__is_used"></span><span id="_DLLNAME__REQUIRED_WHEN__ENTRY__IS_USED"></span>[dllname] required when [entry] is used</dt> <dd> If you are specifying an entry point into a DLL you must also specify the name of that DLL by using the [<a href="dllname-str-.md"><strong>dllname</strong></a>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2092"></span><span id="midl2092"></span><dl> <dt><strong>MIDL2092</strong></dt> </dl></td>
<td><dl> <dt><span id="_bindable__is_invalid_without__propget____propput___or__propputref_"></span><span id="_BINDABLE__IS_INVALID_WITHOUT__PROPGET____PROPPUT___OR__PROPPUTREF_"></span>[bindable] is invalid without [propget], [propput], or [propputref]</dt> <dd> The [<a href="bindable.md"><strong>bindable</strong></a>] attribute is valid only on a property, therefore you must also specify one of the property-accessing or property-setting functions.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2093"></span><span id="midl2093"></span><dl> <dt><strong>MIDL2093</strong></dt> </dl></td>
<td><dl> <dt><span id="procedures_with__propput__or__propputref__must_have_at_least_one_parameter"></span><span id="PROCEDURES_WITH__PROPPUT__OR__PROPPUTREF__MUST_HAVE_AT_LEAST_ONE_PARAMETER"></span>procedures with [propput] or [propputref] must have at least one parameter</dt> <dd> A [<a href="propput.md"><strong>propput</strong></a>] or [ <a href="propputref.md"><strong>propputref</strong></a>] procedure must have at least an [<a href="in.md"><strong>in</strong></a>] parameter with the property to set; a [<a href="propget.md"><strong>propget</strong></a>] procedure must have at least an [<a href="out-idl.md"><strong>out</strong></a>, <a href="retval.md"><strong>retval</strong></a>] parameter to receive the property or reference.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2094"></span><span id="midl2094"></span><dl> <dt><strong>MIDL2094</strong></dt> </dl></td>
<td><dl> <dt><span id="_id__attribute_is_required"></span><span id="_ID__ATTRIBUTE_IS_REQUIRED"></span>[id] attribute is required</dt> <dd> This member function, because of the <a href="dispinterface.md"><strong>dispinterface</strong></a> syntax used, requires a DISPID, which you specify by using the [ <a href="id.md"><strong>id</strong></a>] attribute. When you specify a <strong>dispinterface</strong> by using properties and methods you must specify a DISPID for every property and method.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2095"></span><span id="midl2095"></span><dl> <dt><strong>MIDL2095</strong></dt> </dl></td>
<td><dl> <dt><span id="interface_name_specified_in_the_ACF_does_not_match_that_specified_in_the_IDL_file"></span><span id="interface_name_specified_in_the_acf_does_not_match_that_specified_in_the_idl_file"></span><span id="INTERFACE_NAME_SPECIFIED_IN_THE_ACF_DOES_NOT_MATCH_THAT_SPECIFIED_IN_THE_IDL_FILE"></span>interface name specified in the ACF does not match that specified in the IDL file</dt> <dd> In the current compiler mode, the name that follows the interface keyword in the ACF must be the same as the name that follows the interface keyword in the IDL file. The interface names in the IDL and ACF files can be different when you compile with the MIDL compiler switch <a href="-acf.md"><strong>/acf</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2096"></span><span id="midl2096"></span><dl> <dt><strong>MIDL2096</strong></dt> </dl></td>
<td><dl> <dt><span id="duplicated_attribute"></span><span id="DUPLICATED_ATTRIBUTE"></span>duplicated attribute</dt> <dd> Duplicate or conflicting attributes have been specified. This error often occurs when two attributes are mutually exclusive. For example, the attributes [<a href="code.md"><strong>code</strong></a>] and [<a href="nocode.md"><strong>nocode</strong></a>] cannot be used at the same time.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2097"></span><span id="midl2097"></span><dl> <dt><strong>MIDL2097</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_with__comm_status__or__fault_status__attribute_must_be_a_pointer_to_type_error_status_t"></span><span id="PARAMETER_WITH__COMM_STATUS__OR__FAULT_STATUS__ATTRIBUTE_MUST_BE_A_POINTER_TO_TYPE_ERROR_STATUS_T"></span>parameter with [comm_status] or [fault_status] attribute must be a pointer to type error_status_t</dt> <dd> When [<a href="fault-status.md"><strong>fault_status</strong></a>] or [<a href="comm-status.md"><strong>comm_status</strong></a>] is used as a parameter attribute, the parameter must be an [<a href="out-idl.md"><strong>out</strong></a>] parameter of type <a href="error-status-t.md"><strong>error_status_t</strong></a>. If a server error occurs, the parameter is set to the error code. When the remote call is successfully completed, the procedure sets the value.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2098"></span><span id="midl2098"></span><dl> <dt><strong>MIDL2098</strong></dt> </dl></td>
<td><dl> <dt><span id="a__local__procedure_cannot_be_specified_in_ACF_file"></span><span id="a__local__procedure_cannot_be_specified_in_acf_file"></span><span id="A__LOCAL__PROCEDURE_CANNOT_BE_SPECIFIED_IN_ACF_FILE"></span>a [local] procedure cannot be specified in ACF file</dt> <dd> A local procedure has been specified in the ACF. The local procedure can only be specified in the IDL file.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2099"></span><span id="midl2099"></span><dl> <dt><strong>MIDL2099</strong></dt> </dl></td>
<td><dl> <dt><span id="specified_type_is_not_defined_as_a_handle"></span><span id="SPECIFIED_TYPE_IS_NOT_DEFINED_AS_A_HANDLE"></span>specified type is not defined as a handle</dt> <dd> The type specified in the [<a href="implicit-handle.md"><strong>implicit_handle</strong></a>] attribute is not defined as a handle type. Change the type definition or the type name specified by the attribute.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2100"></span><span id="midl2100"></span><dl> <dt><strong>MIDL2100</strong></dt> </dl></td>
<td><dl> <dt><span id="procedure_undefined"></span><span id="PROCEDURE_UNDEFINED"></span>procedure undefined</dt> <dd> An attribute has been applied to a procedure in the ACF, and that procedure is not defined in the IDL file.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2101"></span><span id="midl2101"></span><dl> <dt><strong>MIDL2101</strong></dt> </dl></td>
<td><dl> <dt><span id="this_parameter_does_not_exist_in_the_IDL_file"></span><span id="this_parameter_does_not_exist_in_the_idl_file"></span><span id="THIS_PARAMETER_DOES_NOT_EXIST_IN_THE_IDL_FILE"></span>this parameter does not exist in the IDL file</dt> <dd> A parameter specified in the ACF does not exist in the definition in the IDL file. All parameters, functions, and type definitions that appear in the ACF must correspond to parameters, functions, and types previously defined in the IDL file.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2102"></span><span id="midl2102"></span><dl> <dt><strong>MIDL2102</strong></dt> </dl></td>
<td><dl> <dt><span id="this_array-bounds_construct_is_not_supported"></span><span id="THIS_ARRAY-BOUNDS_CONSTRUCT_IS_NOT_SUPPORTED"></span>this array-bounds construct is not supported</dt> <dd> MIDL currently supports expressing the upper and lower bounds of an array in the form Array[Lower .. Upper] only when the constant that specifies the lower bound of the array resolves to the value zero.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2103"></span><span id="midl2103"></span><dl> <dt><strong>MIDL2103</strong></dt> </dl></td>
<td><dl> <dt><span id="array_bound_specification_is_illegal"></span><span id="ARRAY_BOUND_SPECIFICATION_IS_ILLEGAL"></span>array bound specification is illegal</dt> <dd> The user specification of array bounds for the fixed-size array is illegal. For example: <br/>
<pre class="syntax" data-space="preserve"><code>typedef short Array[-1]</code></pre>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2104"></span><span id="midl2104"></span><dl> <dt><strong>MIDL2104</strong></dt> </dl></td>
<td><dl> <dt><span id="pointer_to_a_conformant_array_or_an_array_that_contains_a_conformant_array_is_not_supported"></span><span id="POINTER_TO_A_CONFORMANT_ARRAY_OR_AN_ARRAY_THAT_CONTAINS_A_CONFORMANT_ARRAY_IS_NOT_SUPPORTED"></span>pointer to a conformant array or an array that contains a conformant array is not supported</dt> <dd> Illegal conformant array usage. For rules governing conformant arrays, see <a href="/windows/desktop/Rpc/arrays-and-rpc">Arrays and RPC</a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2105"></span><span id="midl2105"></span><dl> <dt><strong>MIDL2105</strong></dt> </dl></td>
<td><dl> <dt><span id="pointee_array_does_not_derive_any_size"></span><span id="POINTEE_ARRAY_DOES_NOT_DERIVE_ANY_SIZE"></span>pointee/array does not derive any size</dt> <dd> A conformant array has been specified without any size specification. You can specify the size with the [<a href="max-is.md"><strong>max_is</strong></a>] or [<a href="size-is.md"><strong>size_is</strong></a>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2106"></span><span id="midl2106"></span><dl> <dt><strong>MIDL2106</strong></dt> </dl></td>
<td><dl> <dt><span id="only_fixed_arrays_and_SAFEARRAYs_are_legal_in_a_type_library"></span><span id="only_fixed_arrays_and_safearrays_are_legal_in_a_type_library"></span><span id="ONLY_FIXED_ARRAYS_AND_SAFEARRAYS_ARE_LEGAL_IN_A_TYPE_LIBRARY"></span>only fixed arrays and SAFEARRAYs are legal in a type library</dt> <dd> You have used an array type inside a library statement that cannot be used in a type library.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2107"></span><span id="midl2107"></span><dl> <dt><strong>MIDL2107</strong></dt> </dl></td>
<td><dl> <dt><span id="SAFEARRAYs_are_only_legal_inside_a_library_block"></span><span id="safearrays_are_only_legal_inside_a_library_block"></span><span id="SAFEARRAYS_ARE_ONLY_LEGAL_INSIDE_A_LIBRARY_BLOCK"></span>SAFEARRAYs are only legal inside a library block</dt> <dd> The MIDL compiler does not recognize a SAFEARRAY as a valid data type except when generating a type library.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2108"></span><span id="midl2108"></span><dl> <dt><strong>MIDL2108</strong></dt> </dl></td>
<td><dl> <dt><span id="badly_formed_character_constant"></span><span id="BADLY_FORMED_CHARACTER_CONSTANT"></span>badly formed character constant</dt> <dd> The end-of-line character is not allowed in character constants.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2109"></span><span id="midl2109"></span><dl> <dt><strong>MIDL2109</strong></dt> </dl></td>
<td><dl> <dt><span id="end_of_file_found_in_comment"></span><span id="END_OF_FILE_FOUND_IN_COMMENT"></span>end of file found in comment</dt> <dd> The end-of-file character has been encountered in a comment.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2110"></span><span id="midl2110"></span><dl> <dt><strong>MIDL2110</strong></dt> </dl></td>
<td><dl> <dt><span id="end_of_file_found_in_string"></span><span id="END_OF_FILE_FOUND_IN_STRING"></span>end of file found in string</dt> <dd> The end-of-file character has been encountered in a string.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2111"></span><span id="midl2111"></span><dl> <dt><strong>MIDL2111</strong></dt> </dl></td>
<td><dl> <dt><span id="identifier_length_exceeds_31_characters"></span><span id="IDENTIFIER_LENGTH_EXCEEDS_31_CHARACTERS"></span>identifier length exceeds 31 characters</dt> <dd> Identifiers are limited to 31 alphanumeric characters. Identifier names longer than 31 characters are truncated.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2112"></span><span id="midl2112"></span><dl> <dt><strong>MIDL2112</strong></dt> </dl></td>
<td><dl> <dt><span id="end_of_line_found_in_string"></span><span id="END_OF_LINE_FOUND_IN_STRING"></span>end of line found in string</dt> <dd> The end-of-line character has been encountered in the string. Verify that you have included the double-quote character that terminates the string.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2113"></span><span id="midl2113"></span><dl> <dt><strong>MIDL2113</strong></dt> </dl></td>
<td><dl> <dt><span id="string_constant_exceeds_limit_of_255_characters"></span><span id="STRING_CONSTANT_EXCEEDS_LIMIT_OF_255_CHARACTERS"></span>string constant exceeds limit of 255 characters</dt> <dd> The string exceeded the maximum allowable length of 255 characters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2114"></span><span id="midl2114"></span><dl> <dt><strong>MIDL2114</strong></dt> </dl></td>
<td><dl> <dt><span id="identifier_exceeds_limit_of_255_characters_and_has_been_truncated"></span><span id="IDENTIFIER_EXCEEDS_LIMIT_OF_255_CHARACTERS_AND_HAS_BEEN_TRUNCATED"></span>identifier exceeds limit of 255 characters and has been truncated</dt> <dd> The identifier exceeded the maximum allowable length of 255 characters. Excess characters in the identifier are truncated.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2115"></span><span id="midl2115"></span><dl> <dt><strong>MIDL2115</strong></dt> </dl></td>
<td><dl> <dt><span id="constant_too_big"></span><span id="CONSTANT_TOO_BIG"></span>constant too big</dt> <dd> The constant is too large to be represented internally.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2116"></span><span id="midl2116"></span><dl> <dt><strong>MIDL2116</strong></dt> </dl></td>
<td><dl> <dt><span id="numerical_parsing_error"></span><span id="NUMERICAL_PARSING_ERROR"></span>numerical parsing error</dt> <dd> The compiler could not parse the numerical identifier.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2117"></span><span id="midl2117"></span><dl> <dt><strong>MIDL2117</strong></dt> </dl></td>
<td><dl> <dt><span id="error_in_opening_file"></span><span id="ERROR_IN_OPENING_FILE"></span>error in opening file</dt> <dd> The operating system reported an error while trying to open an output file. This error can be caused by a name that is too long for the file system or by a duplicate filename.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2118"></span><span id="midl2118"></span><dl> <dt><strong>MIDL2118</strong></dt> </dl></td>
<td>error binding to function<br/></td>
</tr>
<tr class="even">
<td><span id="MIDL2119"></span><span id="midl2119"></span><dl> <dt><strong>MIDL2119</strong></dt> </dl></td>
<td>error initializing OLE<br/></td>
</tr>
<tr class="odd">
<td><span id="MIDL2120"></span><span id="midl2120"></span><dl> <dt><strong>MIDL2120</strong></dt> </dl></td>
<td>error loading library<br/></td>
</tr>
<tr class="even">
<td><span id="MIDL2121"></span><span id="midl2121"></span><dl> <dt><strong>MIDL2121</strong></dt> </dl></td>
<td><dl> <dt><span id="_out__only_parameter_must_not_derive_from_a_top-level__unique__or__ptr__pointer_array"></span><span id="_OUT__ONLY_PARAMETER_MUST_NOT_DERIVE_FROM_A_TOP-LEVEL__UNIQUE__OR__PTR__POINTER_ARRAY"></span>[out] only parameter must not derive from a top-level [unique] or [ptr] pointer/array</dt> <dd> A unique pointer cannot be an [<a href="out-idl.md"><strong>out</strong></a>]-only parameter. By definition, a unique pointer can change from <strong>NULL</strong> to non-<strong>NULL</strong>. No information about the [<strong>out</strong>]-only parameter is passed from client to server.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2122"></span><span id="midl2122"></span><dl> <dt><strong>MIDL2122</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_is_not_applicable_to_this_non-rpcable_union"></span><span id="ATTRIBUTE_IS_NOT_APPLICABLE_TO_THIS_NON-RPCABLE_UNION"></span>attribute is not applicable to this non-rpcable union</dt> <dd> Only the [<a href="switch-is.md"><strong>switch_is</strong></a>] and [<a href="switch-type.md"><strong>switch_type</strong></a>] attributes apply to a union that is transmitted as part of a remote procedure call.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2123"></span><span id="midl2123"></span><dl> <dt><strong>MIDL2123</strong></dt> </dl></td>
<td><dl> <dt><span id="expression_used_for_a_size_attribute_must_not_derive_from_an__out_-only_parameter"></span><span id="EXPRESSION_USED_FOR_A_SIZE_ATTRIBUTE_MUST_NOT_DERIVE_FROM_AN__OUT_-ONLY_PARAMETER"></span>expression used for a size attribute must not derive from an [out]-only parameter</dt> <dd> The value of an [<a href="out-idl.md"><strong>out</strong></a>]-only parameter is not transmitted to the server and cannot be used to determine the length or size of the [<a href="in.md"><strong>in</strong></a>] parameter.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2124"></span><span id="midl2124"></span><dl> <dt><strong>MIDL2124</strong></dt> </dl></td>
<td><dl> <dt><span id="expression_used_for_a_length_attribute_for_an__in__parameter_cannot_derive_from_an__out_-only_parameter"></span><span id="EXPRESSION_USED_FOR_A_LENGTH_ATTRIBUTE_FOR_AN__IN__PARAMETER_CANNOT_DERIVE_FROM_AN__OUT_-ONLY_PARAMETER"></span>expression used for a length attribute for an [in] parameter cannot derive from an [out]-only parameter</dt> <dd> The value of an [<a href="out-idl.md"><strong>out</strong></a>]-only parameter is not transmitted to the server and cannot be used to determine the length or size of the [<a href="in.md"><strong>in</strong></a>] parameter.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2125"></span><span id="midl2125"></span><dl> <dt><strong>MIDL2125</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of__int__needs__c_ext"></span><span id="USE_OF__INT__NEEDS__C_EXT"></span>use of &quot;int&quot; needs /c_ext</dt> <dd> MIDL is a strongly typed language. All parameters transmitted over the network must be derived from one of the MIDL base types. The type <a href="int.md"><strong>int</strong></a> is not defined as part of MIDL. Transmitted data must include a size specifier: <a href="small.md"><strong>small</strong></a>, <strong>short</strong>, or <strong>long</strong>. Data that is not transmitted over the network can be included in an interface; use the <a href="-c-ext.md"><strong>/c_ext</strong></a> switch.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2126"></span><span id="midl2126"></span><dl> <dt><strong>MIDL2126</strong></dt> </dl></td>
<td><dl> <dt><span id="struct_union_field_must_not_be__void_"></span><span id="STRUCT_UNION_FIELD_MUST_NOT_BE__VOID_"></span>struct/union field must not be &quot;void&quot;</dt> <dd> Fields in a structure or union must be declared to be of a specific base type supported by MIDL or a type that is derived from the base types. Void types are not allowed in remote operations.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2127"></span><span id="midl2127"></span><dl> <dt><strong>MIDL2127</strong></dt> </dl></td>
<td><dl> <dt><span id="array_element_must_not_be_void"></span><span id="ARRAY_ELEMENT_MUST_NOT_BE_VOID"></span>array element must not be void</dt> <dd> An array element cannot be void.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2128"></span><span id="midl2128"></span><dl> <dt><strong>MIDL2128</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_type_qualifiers_and_or_modifiers_needs__c_ext"></span><span id="USE_OF_TYPE_QUALIFIERS_AND_OR_MODIFIERS_NEEDS__C_EXT"></span>use of type qualifiers and/or modifiers needs /c_ext</dt> <dd> Type modifiers such as <strong>_cdecl</strong> and <strong>_far</strong> can be compiled only if you specify the <a href="-c-ext.md"><strong>/c_ext</strong></a> switch.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2129"></span><span id="midl2129"></span><dl> <dt><strong>MIDL2129</strong></dt> </dl></td>
<td><dl> <dt><span id="struct_union_field_must_not_derive_from_a_function"></span><span id="STRUCT_UNION_FIELD_MUST_NOT_DERIVE_FROM_A_FUNCTION"></span>struct/union field must not derive from a function</dt> <dd> The fields of a structure or union must be MIDL base types or types that are derived from these base types. Functions are not legal in structure or union fields.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2130"></span><span id="midl2130"></span><dl> <dt><strong>MIDL2130</strong></dt> </dl></td>
<td><dl> <dt><span id="array_element_must_not_be_a_function"></span><span id="ARRAY_ELEMENT_MUST_NOT_BE_A_FUNCTION"></span>array element must not be a function</dt> <dd> An array element cannot be a function.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2131"></span><span id="midl2131"></span><dl> <dt><strong>MIDL2131</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_must_not_be_a_function"></span><span id="PARAMETER_MUST_NOT_BE_A_FUNCTION"></span>parameter must not be a function</dt> <dd> The parameter to a remote procedure must be a variable of a specified type. A function cannot be a parameter to the remote procedure.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2132"></span><span id="midl2132"></span><dl> <dt><strong>MIDL2132</strong></dt> </dl></td>
<td><dl> <dt><span id="struct_union_with_bit_fields_needs__c_ext"></span><span id="STRUCT_UNION_WITH_BIT_FIELDS_NEEDS__C_EXT"></span>struct/union with bit fields needs /c_ext</dt> <dd> You must specify the MIDL compiler switch <a href="-c-ext.md"><strong>/c_ext</strong></a> to allow bit fields in structures that are not transmitted in a remote procedure call.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2133"></span><span id="midl2133"></span><dl> <dt><strong>MIDL2133</strong></dt> </dl></td>
<td><dl> <dt><span id="bit_field_specification_on_a_type_other_that__int__is_a_non-ANSI-compatible_extension"></span><span id="bit_field_specification_on_a_type_other_that__int__is_a_non-ansi-compatible_extension"></span><span id="BIT_FIELD_SPECIFICATION_ON_A_TYPE_OTHER_THAT__INT__IS_A_NON-ANSI-COMPATIBLE_EXTENSION"></span>bit field specification on a type other that &quot;int&quot; is a non-ANSI-compatible extension</dt> <dd> The ANSI C programming language specification does not allow bit fields to be applied to noninteger types.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2134"></span><span id="midl2134"></span><dl> <dt><strong>MIDL2134</strong></dt> </dl></td>
<td><dl> <dt><span id="bit_field_specification_can_be_applied_only_to_simple__integral_types"></span><span id="BIT_FIELD_SPECIFICATION_CAN_BE_APPLIED_ONLY_TO_SIMPLE__INTEGRAL_TYPES"></span>bit field specification can be applied only to simple, integral types</dt> <dd> The ANSI C programming language specification does not allow bit fields to be applied to noninteger types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2135"></span><span id="midl2135"></span><dl> <dt><strong>MIDL2135</strong></dt> </dl></td>
<td><dl> <dt><span id="struct_union_field_must_not_derive_from_handle_t_or_a_context-handle"></span><span id="STRUCT_UNION_FIELD_MUST_NOT_DERIVE_FROM_HANDLE_T_OR_A_CONTEXT-HANDLE"></span>struct/union field must not derive from handle_t or a context-handle</dt> <dd> Context handles cannot be transmitted as part of another structure. They must be transmitted as context handles.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2136"></span><span id="midl2136"></span><dl> <dt><strong>MIDL2136</strong></dt> </dl></td>
<td><dl> <dt><span id="array_element_must_not_derive_from_handle_t_or_a_context_handle"></span><span id="ARRAY_ELEMENT_MUST_NOT_DERIVE_FROM_HANDLE_T_OR_A_CONTEXT_HANDLE"></span>array element must not derive from handle_t or a context handle</dt> <dd> Context handles cannot be transmitted as part of an array.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2137"></span><span id="midl2137"></span><dl> <dt><strong>MIDL2137</strong></dt> </dl></td>
<td><dl> <dt><span id="this_specification_of_union_needs__c_ext"></span><span id="THIS_SPECIFICATION_OF_UNION_NEEDS__C_EXT"></span>this specification of union needs /c_ext</dt> <dd> A union that appears in the interface definition must be associated with the discriminant or declared as local. Data that is not transmitted over the network can be implicitly declared as local when you use the <a href="-c-ext.md"><strong>/c_ext</strong></a> switch, which is the MIDL default. You cannot compile this IDL with the <a href="-osf.md"><strong>/osf</strong></a> switch.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2138"></span><span id="midl2138"></span><dl> <dt><strong>MIDL2138</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_deriving_from_an__int__must_have_size_specifier__small____short___or__long__with_the__int_"></span><span id="PARAMETER_DERIVING_FROM_AN__INT__MUST_HAVE_SIZE_SPECIFIER__SMALL____SHORT___OR__LONG__WITH_THE__INT_"></span>parameter deriving from an &quot;int&quot; must have size specifier &quot;small,&quot; &quot;short,&quot; or &quot;long&quot; with the &quot;int&quot;</dt> <dd> The type <a href="int.md"><strong>int</strong></a> is only a valid MIDL type on 32-bit platforms, on 16-bit systems <strong>int</strong> must be accompanied by a size specification. Use one of the size specifiers <a href="small.md"><strong>small</strong></a>, <a href="short.md"><strong>short</strong></a>, or <a href="long.md"><strong>long</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2139"></span><span id="midl2139"></span><dl> <dt><strong>MIDL2139</strong></dt> </dl></td>
<td><dl> <dt><span id="type_of_the_parameter_cannot_derive_from_void_or_void_"></span><span id="TYPE_OF_THE_PARAMETER_CANNOT_DERIVE_FROM_VOID_OR_VOID_"></span>type of the parameter cannot derive from void or void*</dt> <dd> MIDL is a strongly typed language. All parameters transmitted over the network must be derived from one of the MIDL base types. MIDL does not support <a href="void.md"><strong>void</strong></a> as a base type. You must change the declaration to a valid MIDL type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2140"></span><span id="midl2140"></span><dl> <dt><strong>MIDL2140</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_deriving_from_a_struct_union_containing_bit_fields_is_not_supported"></span><span id="PARAMETER_DERIVING_FROM_A_STRUCT_UNION_CONTAINING_BIT_FIELDS_IS_NOT_SUPPORTED"></span>parameter deriving from a struct/union containing bit fields is not supported</dt> <dd> Bit fields are not defined as a valid data type by DCE RPC.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2141"></span><span id="midl2141"></span><dl> <dt><strong>MIDL2141</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_a_parameter_deriving_from_a_type_containing_type-modifiers_type-qualifiers_needs__c_ext"></span><span id="USE_OF_A_PARAMETER_DERIVING_FROM_A_TYPE_CONTAINING_TYPE-MODIFIERS_TYPE-QUALIFIERS_NEEDS__C_EXT"></span>use of a parameter deriving from a type containing type-modifiers/type-qualifiers needs /c_ext</dt> <dd> The use of keywords such as <strong>far</strong>, <strong>near</strong>, <a href="const.md"><strong>const</strong></a>, and <strong>volatile</strong> in the IDL file is a Microsoft extension to DCE RPC. These keywords are not available when you compile with the <a href="-osf.md"><strong>/osf</strong></a> switch, which turns off the default <a href="-c-ext.md"><strong>/c_ext</strong></a> extension switch.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2142"></span><span id="midl2142"></span><dl> <dt><strong>MIDL2142</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_must_not_derive_from_a_pointer_to_a_function"></span><span id="PARAMETER_MUST_NOT_DERIVE_FROM_A_POINTER_TO_A_FUNCTION"></span>parameter must not derive from a pointer to a function</dt> <dd> The RPC run-time libraries transmit a pointer and its associated data between client and server. Pointers to functions cannot be transmitted as parameters because the function cannot be transmitted over the network.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2143"></span><span id="midl2143"></span><dl> <dt><strong>MIDL2143</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_must_not_derive_from_a_nonrpccapable_union"></span><span id="PARAMETER_MUST_NOT_DERIVE_FROM_A_NONRPCCAPABLE_UNION"></span>parameter must not derive from a nonrpc capable union</dt> <dd> The union must be associated with a discriminant. Use the [<a href="switch-is.md"><strong>switch_is</strong></a>] and [<a href="switch-type.md"><strong>switch_type</strong></a>] attributes.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2144"></span><span id="midl2144"></span><dl> <dt><strong>MIDL2144</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_derives_from_an__int.__You_must_use_size_specifiers_with_the__int_"></span><span id="return_type_derives_from_an__int.__you_must_use_size_specifiers_with_the__int_"></span><span id="RETURN_TYPE_DERIVES_FROM_AN__INT.__YOU_MUST_USE_SIZE_SPECIFIERS_WITH_THE__INT_"></span>return type derives from an &quot;int.&quot; You must use size specifiers with the &quot;int&quot;</dt> <dd> On 16-bit systems, the type <a href="int.md"><strong>int</strong></a> is not a valid MIDL type unless it is accompanied by a size specification. Use one of the size specifiers <a href="small.md"><strong>small</strong></a>, <a href="short.md"><strong>short</strong></a>, or <a href="long.md"><strong>long</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2145"></span><span id="midl2145"></span><dl> <dt><strong>MIDL2145</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_must_not_derive_from_a_void_pointer"></span><span id="RETURN_TYPE_MUST_NOT_DERIVE_FROM_A_VOID_POINTER"></span>return type must not derive from a void pointer</dt> <dd> MIDL is a strongly typed language. All parameters transmitted over the network must be derived from one of the MIDL base types. Void types are not defined as part of MIDL. You must change the declaration to a valid MIDL type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2146"></span><span id="midl2146"></span><dl> <dt><strong>MIDL2146</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_must_not_derive_from_a_structure_union_containing_bit-fields"></span><span id="RETURN_TYPE_MUST_NOT_DERIVE_FROM_A_STRUCTURE_UNION_CONTAINING_BIT-FIELDS"></span>return type must not derive from a structure/union containing bit-fields</dt> <dd> Bit fields are not defined as a valid data type by DCE RPC.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2147"></span><span id="midl2147"></span><dl> <dt><strong>MIDL2147</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_must_not_derive_from_a_nonrpccapable_union"></span><span id="RETURN_TYPE_MUST_NOT_DERIVE_FROM_A_NONRPCCAPABLE_UNION"></span>return type must not derive from a nonrpc capable union</dt> <dd> The union must be associated with a discriminant. Use the [<a href="switch-is.md"><strong>switch_is</strong></a>] and [<a href="switch-type.md"><strong>switch_type</strong></a>] attributes.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2148"></span><span id="midl2148"></span><dl> <dt><strong>MIDL2148</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_must_not_derive_from_a_pointer_to_a_function"></span><span id="RETURN_TYPE_MUST_NOT_DERIVE_FROM_A_POINTER_TO_A_FUNCTION"></span>return type must not derive from a pointer to a function</dt> <dd> The RPC run-time libraries transmit a pointer and its associated data between client and server. Pointers to functions cannot be transmitted as parameters because RPC does not define a method to transmit the associated function over the network.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2149"></span><span id="midl2149"></span><dl> <dt><strong>MIDL2149</strong></dt> </dl></td>
<td><dl> <dt><span id="compound_initializers_are_not_supported"></span><span id="COMPOUND_INITIALIZERS_ARE_NOT_SUPPORTED"></span>compound initializers are not supported</dt> <dd> DCE RPC supports simple initialization only. The structure or array cannot be initialized in the IDL file.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2150"></span><span id="midl2150"></span><dl> <dt><strong>MIDL2150</strong></dt> </dl></td>
<td><dl> <dt><span id="ACF_attributes_in_the_IDL_file_need_the__app_config_switch"></span><span id="acf_attributes_in_the_idl_file_need_the__app_config_switch"></span><span id="ACF_ATTRIBUTES_IN_THE_IDL_FILE_NEED_THE__APP_CONFIG_SWITCH"></span>ACF attributes in the IDL file need the /app_config switch</dt> <dd> A Microsoft extension allows you to specify ACF attributes in the IDL file. Use the <a href="-app-config.md"><strong>/app_config</strong></a> switch to activate this extension.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2151"></span><span id="midl2151"></span><dl> <dt><strong>MIDL2151</strong></dt> </dl></td>
<td><dl> <dt><span id="single-line_comment_needs__ms_ext_or__c_ext"></span><span id="SINGLE-LINE_COMMENT_NEEDS__MS_EXT_OR__C_EXT"></span>single-line comment needs /ms_ext or /c_ext</dt> <dd> Single-line comments that use two slash characters (//) represent a Microsoft extension to DCE RPC. You cannot use single-line comments if you are compiling with the <a href="-osf.md"><strong>/osf</strong></a> switch.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2152"></span><span id="midl2152"></span><dl> <dt><strong>MIDL2152</strong></dt> </dl></td>
<td><dl> <dt><span id="_version__format_is_incorrect"></span><span id="_VERSION__FORMAT_IS_INCORRECT"></span>[version] format is incorrect</dt> <dd> The interface version number in the interface header must be specified in the format <em>major</em>.<em>minor</em>, where each number can range from 0 to 65535.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2153"></span><span id="midl2153"></span><dl> <dt><strong>MIDL2153</strong></dt> </dl></td>
<td><dl> <dt><span id="_signed__needs__ms_ext_or__c_ext"></span><span id="_SIGNED__NEEDS__MS_EXT_OR__C_EXT"></span>&quot;signed&quot; needs /ms_ext or /c_ext</dt> <dd> The use of the <a href="signed.md"><strong>signed</strong></a> keyword is a Microsoft extension to DCE RPC. You cannot use the <a href="-osf.md"><strong>/osf</strong></a> switch if you want to use this feature.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2154"></span><span id="midl2154"></span><dl> <dt><strong>MIDL2154</strong></dt> </dl></td>
<td><dl> <dt><span id="mismatch_in_assignment_type"></span><span id="MISMATCH_IN_ASSIGNMENT_TYPE"></span>mismatch in assignment type</dt> <dd> The type of the variable does not match the type of the value that is assigned to the variable.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2155"></span><span id="midl2155"></span><dl> <dt><strong>MIDL2155</strong></dt> </dl></td>
<td><dl> <dt><span id="declaration_must_be_of_the_form__const__type__declarator_____initializing_expression_"></span><span id="DECLARATION_MUST_BE_OF_THE_FORM__CONST__TYPE__DECLARATOR_____INITIALIZING_EXPRESSION_"></span>declaration must be of the form: const &lt;type&gt;<declarator> = <initializing expression></dt> <dd> The declaration is not compatible with DCE RPC syntax. Use the <a href="-ms-ext.md"><strong>/ms_ext</strong></a> or <a href="-c-ext.md"><strong>/c_ext</strong></a> MIDL compiler mode switch.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2156"></span><span id="midl2156"></span><dl> <dt><strong>MIDL2156</strong></dt> </dl></td>
<td><dl> <dt><span id="declaration_must_have__const_"></span><span id="DECLARATION_MUST_HAVE__CONST_"></span>declaration must have &quot;const&quot;</dt> <dd> Declarations in the IDL file must be constant expressions that use the keyword <a href="const.md"><strong>const</strong></a>, for example:<br/>
<pre class="syntax" data-space="preserve"><code>const short x = 2;</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2157"></span><span id="midl2157"></span><dl> <dt><strong>MIDL2157</strong></dt> </dl></td>
<td><dl> <dt><span id="struct_union_enum_must_not_be_defined_in_a_parameter-type_specification"></span><span id="STRUCT_UNION_ENUM_MUST_NOT_BE_DEFINED_IN_A_PARAMETER-TYPE_SPECIFICATION"></span>struct/union/enum must not be defined in a parameter-type specification</dt> <dd> The structure, union, or enumerated type must be explicitly stated outside of the function prototype.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2158"></span><span id="midl2158"></span><dl> <dt><strong>MIDL2158</strong></dt> </dl></td>
<td><dl> <dt><span id="_allocate__attribute_must_be_applied_only_on_non-void_pointer_types"></span><span id="_ALLOCATE__ATTRIBUTE_MUST_BE_APPLIED_ONLY_ON_NON-VOID_POINTER_TYPES"></span>[allocate] attribute must be applied only on non-void pointer types</dt> <dd> The [<a href="allocate.md"><strong>allocate</strong></a>] attribute is designed for complex pointer-based data structures. When the [allocate] attribute is specified, the stub file traverses the data structure to compute the total size of all objects accessible from the pointer and all other pointers in the data structure. Change the type to a nonvoid pointer type or remove the [<strong>allocate</strong>] attribute and use another method to determine its allocation size, such as the <strong>sizeof</strong> operator.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2159"></span><span id="midl2159"></span><dl> <dt><strong>MIDL2159</strong></dt> </dl></td>
<td><dl> <dt><span id="array_or_equivalent_pointer_construct_cannot_derive_from_a_nonencapsulated_union"></span><span id="ARRAY_OR_EQUIVALENT_POINTER_CONSTRUCT_CANNOT_DERIVE_FROM_A_NONENCAPSULATED_UNION"></span>array or equivalent pointer construct cannot derive from a nonencapsulated union</dt> <dd> Each union must be associated with a discriminant. Arrays of unions are not permitted because they do not provide the associated discriminant. Arrays of structures in which the structure packages the union and its discriminant are permitted because the stubs can use the discriminant to determine the size of each union.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2160"></span><span id="midl2160"></span><dl> <dt><strong>MIDL2160</strong></dt> </dl></td>
<td><dl> <dt><span id="field_must_not_derive_from_an_error_status_t_type"></span><span id="FIELD_MUST_NOT_DERIVE_FROM_AN_ERROR_STATUS_T_TYPE"></span>field must not derive from an error_status_t type</dt> <dd> The <a href="error-status-t.md"><strong>error_status_t</strong></a> type can only be used as a parameter or a return type. It cannot be embedded in the field of a structure or union.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2161"></span><span id="midl2161"></span><dl> <dt><strong>MIDL2161</strong></dt> </dl></td>
<td><dl> <dt><span id="union_has_at_least_one_arm_without_a_case_label"></span><span id="UNION_HAS_AT_LEAST_ONE_ARM_WITHOUT_A_CASE_LABEL"></span>union has at least one arm without a case label</dt> <dd> The union declaration does not match the required MIDL syntax for the union. Each union arm requires a case label or default label that selects that union arm.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2162"></span><span id="midl2162"></span><dl> <dt><strong>MIDL2162</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_or_return_value_must_not_derive_from_a_type_that_has__ignore__applied_to_it"></span><span id="PARAMETER_OR_RETURN_VALUE_MUST_NOT_DERIVE_FROM_A_TYPE_THAT_HAS__IGNORE__APPLIED_TO_IT"></span>parameter or return value must not derive from a type that has [ignore] applied to it</dt> <dd> The [<a href="ignore.md"><strong>ignore</strong></a>] attribute is a field attribute that can be applied only to fields, such as fields of structures and arrays. The [<strong>ignore</strong>] attribute indicates that the stub should not dereference the pointer during transmission and is not allowed when it conflicts with other attributes that must be dereferenced, such as [<a href="out-idl.md"><strong>out</strong></a>] parameters and function return values.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2163"></span><span id="midl2163"></span><dl> <dt><strong>MIDL2163</strong></dt> </dl></td>
<td><dl> <dt><span id="pointer_already_has_a_pointer_attribute_applied_to_it"></span><span id="POINTER_ALREADY_HAS_A_POINTER_ATTRIBUTE_APPLIED_TO_IT"></span>pointer already has a pointer attribute applied to it</dt> <dd> Only one of the pointer attributes, [<a href="ref.md"><strong>ref</strong></a>], [<a href="unique.md"><strong>unique</strong></a>], or [<a href="ptr.md"><strong>ptr</strong></a>], can be applied to a single pointer.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2164"></span><span id="midl2164"></span><dl> <dt><strong>MIDL2164</strong></dt> </dl></td>
<td><dl> <dt><span id="field_parameter_must_not_derive_from_a_structure_that_is_recursive_through_a_ref_pointer"></span><span id="FIELD_PARAMETER_MUST_NOT_DERIVE_FROM_A_STRUCTURE_THAT_IS_RECURSIVE_THROUGH_A_REF_POINTER"></span>field/parameter must not derive from a structure that is recursive through a ref pointer</dt> <dd> By definition, a reference pointer cannot be set to <strong>NULL</strong>. A recursive data structure defined with a reference pointer has no <strong>NULL</strong> elements and by convention is nonterminating. Use a [<a href="unique.md"><strong>unique</strong></a>] pointer attribute to allow the data structure to specify a <strong>NULL</strong> element, or redefine the data structure as a nonrecursive data structure.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2165"></span><span id="midl2165"></span><dl> <dt><strong>MIDL2165</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_field_deriving_from_a_void_pointer_needs__c_ext"></span><span id="USE_OF_FIELD_DERIVING_FROM_A_VOID_POINTER_NEEDS__C_EXT"></span>use of field deriving from a void pointer needs /c_ext</dt> <dd> The type <strong>void *</strong> and other types and type qualifiers that are not supported by DCE IDL are allowed in the IDL file only when you use the MIDL default compiler settings. Using the <a href="-osf.md"><strong>/osf</strong></a> switch overrides this default. If you must compile in osf-compatibility mode, you will need to redefine the pointer type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2166"></span><span id="midl2166"></span><dl> <dt><strong>MIDL2166</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_this_attribute_needs__ms_ext"></span><span id="USE_OF_THIS_ATTRIBUTE_NEEDS__MS_EXT"></span>use of this attribute needs /ms_ext</dt> <dd> This language feature is a Microsoft extension to DCE IDL. You cannot use this feature if you are compiling in osf-compatibility mode ( <a href="-osf.md"><strong>/osf</strong></a> ).<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2167"></span><span id="midl2167"></span><dl> <dt><strong>MIDL2167</strong></dt> </dl></td>
<td><dl> <dt><span id="this_attribute_only_allowed_with_new_format_type_libraries"></span><span id="THIS_ATTRIBUTE_ONLY_ALLOWED_WITH_NEW_FORMAT_TYPE_LIBRARIES"></span>this attribute only allowed with new format type libraries</dt> <dd> To use this attribute, you need the version of Oleaut32.dll provided with Windows 2000 or later.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2168"></span><span id="midl2168"></span><dl> <dt><strong>MIDL2168</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_wchar_t_needs__ms_ext_or__c_ext"></span><span id="USE_OF_WCHAR_T_NEEDS__MS_EXT_OR__C_EXT"></span>use of wchar_t needs /ms_ext or /c_ext</dt> <dd> The wide-character type represents an extension to DCE IDL. The MIDL compiler does not accept the wide-character type when you specify the <a href="-osf.md"><strong>/osf</strong></a> switch.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2169"></span><span id="midl2169"></span><dl> <dt><strong>MIDL2169</strong></dt> </dl></td>
<td><dl> <dt><span id="unnamed_fields_need__ms_ext_or__c_ext"></span><span id="UNNAMED_FIELDS_NEED__MS_EXT_OR__C_EXT"></span>unnamed fields need /ms_ext or /c_ext</dt> <dd> DCE IDL does not support the use of unnamed structures or unions embedded in other structures or unions. In DCE IDL, all such embedded fields must be named. The MIDL compiler does not allow their use when you specify the <a href="-osf.md"><strong>/osf</strong></a> switch.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2170"></span><span id="midl2170"></span><dl> <dt><strong>MIDL2170</strong></dt> </dl></td>
<td><dl> <dt><span id="unnamed_fields_can_derive_only_from_struct_union_types"></span><span id="UNNAMED_FIELDS_CAN_DERIVE_ONLY_FROM_STRUCT_UNION_TYPES"></span>unnamed fields can derive only from struct/union types</dt> <dd> The Microsoft extension to the DCE IDL that supports unnamed fields applies only to structures and unions. You must assign a name to the field or redefine the field to comply with this restriction.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2171"></span><span id="midl2171"></span><dl> <dt><strong>MIDL2171</strong></dt> </dl></td>
<td><dl> <dt><span id="field_of_a_union_cannot_derive_from_a_conformant_varying_array_or_its_pointer_equivalent"></span><span id="FIELD_OF_A_UNION_CANNOT_DERIVE_FROM_A_CONFORMANT_VARYING_ARRAY_OR_ITS_POINTER_EQUIVALENT"></span>field of a union cannot derive from a conformant/varying array or its pointer equivalent</dt> <dd> The conformant array cannot appear alone in the union but must be accompanied by the value that specifies the size of the array. Instead of using the array as the union arm, use a structure that consists of the conformant array and the identifier that specifies its size.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2172"></span><span id="midl2172"></span><dl> <dt><strong>MIDL2172</strong></dt> </dl></td>
<td><dl> <dt><span id="no__pointer_default__attribute_specified__assuming__ptr__for_all_unattributed_pointers_in_interface"></span><span id="NO__POINTER_DEFAULT__ATTRIBUTE_SPECIFIED__ASSUMING__PTR__FOR_ALL_UNATTRIBUTED_POINTERS_IN_INTERFACE"></span>no [pointer_default] attribute specified, assuming [ptr] for all unattributed pointers in interface</dt> <dd> The DCE IDL implementation specifies that all pointers in each IDL file must be associated with pointer attributes. When an explicit pointer attribute is not assigned to the parameter or pointer type and no [<a href="pointer-default.md"><strong>pointer_default</strong></a>] attribute is specified in the IDL file, the full pointer attribute <a href="ptr.md"><strong>ptr</strong></a> is associated with the pointer. You can change the pointer attributes by using explicit pointer attributes, by specifying a [<strong>pointer_default</strong>] attribute, or by specifying the <a href="-ms-ext.md"><strong>/ms_ext</strong></a> switch to change the default for unattributed pointers to [<a href="unique.md"><strong>unique</strong></a>].<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2173"></span><span id="midl2173"></span><dl> <dt><strong>MIDL2173</strong></dt> </dl></td>
<td><dl> <dt><span id="initializing_expression_must_resolve_to_a_constant_expression"></span><span id="INITIALIZING_EXPRESSION_MUST_RESOLVE_TO_A_CONSTANT_EXPRESSION"></span>initializing expression must resolve to a constant expression</dt> <dd> If an expression is used as an initializer, the expression must be a constant expression. This is true in all MIDL compiler modes. The expression must be resolvable at compile time. Specify a literal constant or an expression that resolves to a constant, rather than a variable.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2174"></span><span id="midl2174"></span><dl> <dt><strong>MIDL2174</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_expression_must_be_of_type_integer__char__Boolean_or_enum"></span><span id="attribute_expression_must_be_of_type_integer__char__boolean_or_enum"></span><span id="ATTRIBUTE_EXPRESSION_MUST_BE_OF_TYPE_INTEGER__CHAR__BOOLEAN_OR_ENUM"></span>attribute expression must be of type integer, char, Boolean or enum</dt> <dd> The specified type does not resolve to a valid switch type. Use an integer, character, <a href="byte.md"><strong>byte</strong></a>, <a href="boolean.md"><strong>Boolean</strong></a>, or <a href="enum.md"><strong>enum</strong></a> type, or a type that is derived from one of these types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2175"></span><span id="midl2175"></span><dl> <dt><strong>MIDL2175</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_constant"></span><span id="ILLEGAL_CONSTANT"></span>illegal constant</dt> <dd> The specified constant is out of the valid range for the specified type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2176"></span><span id="midl2176"></span><dl> <dt><strong>MIDL2176</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_not_implemented__ignored"></span><span id="ATTRIBUTE_NOT_IMPLEMENTED__IGNORED"></span>attribute not implemented; ignored</dt> <dd> The attribute specified is not implemented in this release of Microsoft RPC. The MIDL compiler continues processing the IDL file as if the attribute were not present.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2177"></span><span id="midl2177"></span><dl> <dt><strong>MIDL2177</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_must_not_derive_from_a__ref__pointer"></span><span id="RETURN_TYPE_MUST_NOT_DERIVE_FROM_A__REF__POINTER"></span>return type must not derive from a [ref] pointer</dt> <dd> Function return values that are defined to be pointer types must be specified as [<a href="unique.md"><strong>unique</strong></a>] or <a href="ptr.md"><strong>full</strong></a> pointers. You cannot use reference pointers.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2178"></span><span id="midl2178"></span><dl> <dt><strong>MIDL2178</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_expression_must_be_a_variable_name_or_a_pointer_dereference_expression_in_this_mode._You_must_specify_the__ms_ext_switch"></span><span id="attribute_expression_must_be_a_variable_name_or_a_pointer_dereference_expression_in_this_mode._you_must_specify_the__ms_ext_switch"></span><span id="ATTRIBUTE_EXPRESSION_MUST_BE_A_VARIABLE_NAME_OR_A_POINTER_DEREFERENCE_EXPRESSION_IN_THIS_MODE._YOU_MUST_SPECIFY_THE__MS_EXT_SWITCH"></span>attribute expression must be a variable name or a pointer dereference expression in this mode. You must specify the /ms_ext switch</dt> <dd> The DCE IDL compiler requires the size associated with the [<a href="size-is.md"><strong>size_is</strong></a>] attribute to be specified by a variable or pointer variable. If you want to take advantage of the Microsoft extension that allows the [<strong>size_is</strong>] attribute to be defined by a constant expression, you cannot use the <a href="-osf.md"><strong>/osf</strong></a> compiler switch.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2179"></span><span id="midl2179"></span><dl> <dt><strong>MIDL2179</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_must_not_derive_from_a_recursive_nonencapsulated_union"></span><span id="PARAMETER_MUST_NOT_DERIVE_FROM_A_RECURSIVE_NONENCAPSULATED_UNION"></span>parameter must not derive from a recursive nonencapsulated union</dt> <dd> A union must include a discriminant, so a union cannot have another union as an element. A union can be embedded in another union only when it is part of a structure that includes the discriminant.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2180"></span><span id="midl2180"></span><dl> <dt><strong>MIDL2180</strong></dt> </dl></td>
<td><dl> <dt><span id="binding-handle_parameter_cannot_be__out__only"></span><span id="BINDING-HANDLE_PARAMETER_CANNOT_BE__OUT__ONLY"></span>binding-handle parameter cannot be [out] only</dt> <dd> The handle parameter identified by the MIDL compiler as the binding handle for this operation must be an [<a href="in.md"><strong>in</strong></a>] parameter. [<a href="out-idl.md"><strong>out</strong></a>]-only parameters are undefined on the client stub, and the binding handle must be defined on the client.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2181"></span><span id="midl2181"></span><dl> <dt><strong>MIDL2181</strong></dt> </dl></td>
<td><dl> <dt><span id="pointer_to_a_handle_cannot_be__unique__or__ptr_"></span><span id="POINTER_TO_A_HANDLE_CANNOT_BE__UNIQUE__OR__PTR_"></span>pointer to a handle cannot be [unique] or [ptr]</dt> <dd> You cannot use the unique and full pointer attributes for a pointer to a handle. These attributes allow the value <strong>NULL</strong>, and the binding handle cannot be <strong>NULL</strong>. Use the [<a href="ref.md"><strong>ref</strong></a>] attribute to derive the binding-handle parameter from reference pointers.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2182"></span><span id="midl2182"></span><dl> <dt><strong>MIDL2182</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_that_is_not_a_binding_handle_must_not_derive_from_handle_t"></span><span id="PARAMETER_THAT_IS_NOT_A_BINDING_HANDLE_MUST_NOT_DERIVE_FROM_HANDLE_T"></span>parameter that is not a binding handle must not derive from handle_t</dt> <dd> The primitive handle type <a href="handle-t.md"><strong>handle_t</strong></a> is not a valid data type that is transmitted over the network. Change the parameter type to a type other than <strong>handle_t</strong>, or remove the parameter.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2183"></span><span id="midl2183"></span><dl> <dt><strong>MIDL2183</strong></dt> </dl></td>
<td><dl> <dt><span id="unexpected_end_of_file_found"></span><span id="UNEXPECTED_END_OF_FILE_FOUND"></span>unexpected end of file found</dt> <dd> The MIDL compiler found the end of the file before it was able to successfully resolve all syntactical elements of the file. Verify that the terminating right-brace character (}) is present at the end of the file, or check the syntax.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2184"></span><span id="midl2184"></span><dl> <dt><strong>MIDL2184</strong></dt> </dl></td>
<td><dl> <dt><span id="type_deriving_from_handle_t_must_not_have__transmit_as__applied_to_it"></span><span id="TYPE_DERIVING_FROM_HANDLE_T_MUST_NOT_HAVE__TRANSMIT_AS__APPLIED_TO_IT"></span>type deriving from handle_t must not have [transmit_as] applied to it</dt> <dd> The primitive handle type <a href="handle-t.md"><strong>handle_t</strong></a> is not transmitted over the network.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2185"></span><span id="midl2185"></span><dl> <dt><strong>MIDL2185</strong></dt> </dl></td>
<td><dl> <dt><span id="_context_handle__must_not_be_applied_to_a_type_that_has__handle__applied_to_it"></span><span id="_CONTEXT_HANDLE__MUST_NOT_BE_APPLIED_TO_A_TYPE_THAT_HAS__HANDLE__APPLIED_TO_IT"></span>[context_handle] must not be applied to a type that has [handle] applied to it</dt> <dd> The [<a href="context-handle.md"><strong>context_handle</strong></a>] and [<a href="handle.md"><strong>handle</strong></a>] attributes cannot be applied to the same type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2186"></span><span id="midl2186"></span><dl> <dt><strong>MIDL2186</strong></dt> </dl></td>
<td><dl> <dt><span id="_handle__must_not_be_specified_on_a_type_deriving_from_void_or_void__"></span><span id="_HANDLE__MUST_NOT_BE_SPECIFIED_ON_A_TYPE_DERIVING_FROM_VOID_OR_VOID__"></span>[handle] must not be specified on a type deriving from void or void *</dt> <dd> A type specified with the [<a href="handle.md"><strong>handle</strong></a>] attribute can be transmitted over the network, but the type <strong>void*</strong> is not a transmissible type. The handle type must resolve to a type that derives from the transmissible base types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2187"></span><span id="midl2187"></span><dl> <dt><strong>MIDL2187</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_must_have_either__in____out__or__in_out__in_this_mode._You_must_specify__ms_ext_or__c_ext"></span><span id="parameter_must_have_either__in____out__or__in_out__in_this_mode._you_must_specify__ms_ext_or__c_ext"></span><span id="PARAMETER_MUST_HAVE_EITHER__IN____OUT__OR__IN_OUT__IN_THIS_MODE._YOU_MUST_SPECIFY__MS_EXT_OR__C_EXT"></span>parameter must have either [in], [out] or [in,out] in this mode. You must specify /ms_ext or /c_ext</dt> <dd> The DCE IDL compiler requires all parameters to have explicit directional parameters. To use the Microsoft extensions to DCE IDL, you cannot use the <a href="-osf.md"><strong>/osf</strong></a> switch, which overrides <a href="-ms-ext.md"><strong>/ms_ext</strong></a> and <a href="-c-ext.md"><strong>/c_ext</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2188"></span><span id="midl2188"></span><dl> <dt><strong>MIDL2188</strong></dt> </dl></td>
<td><dl> <dt><span id="transmitted_type_may_not_derive_from__void__for__transmit_as____represent_as____wire_marshal____user_marshal_"></span><span id="TRANSMITTED_TYPE_MAY_NOT_DERIVE_FROM__VOID__FOR__TRANSMIT_AS____REPRESENT_AS____WIRE_MARSHAL____USER_MARSHAL_"></span>transmitted type may not derive from &quot;void&quot; for [transmit_as], [represent_as], [wire_marshal], [user_marshal]</dt> <dd> The [<a href="transmit-as.md"><strong>transmit_as</strong></a>] attribute applies only to pointer types. Use the type <strong>void*</strong> in place of <a href="void.md"><strong>void</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2189"></span><span id="midl2189"></span><dl> <dt><strong>MIDL2189</strong></dt> </dl></td>
<td><dl> <dt><span id="_void__must_be_specified_on_the_first_and_only_parameter_specification"></span><span id="_VOID__MUST_BE_SPECIFIED_ON_THE_FIRST_AND_ONLY_PARAMETER_SPECIFICATION"></span>&quot;void&quot; must be specified on the first and only parameter specification</dt> <dd> The keyword <a href="void.md"><strong>void</strong></a> incorrectly appears with other function parameters. To specify a function without parameters, the keyword <strong>void</strong> must be the only element of the parameter list, as in the following example:<br/>
<pre class="syntax" data-space="preserve"><code>void Moo(void)</code></pre>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2190"></span><span id="midl2190"></span><dl> <dt><strong>MIDL2190</strong></dt> </dl></td>
<td><dl> <dt><span id="_switch_is__must_be_specified_only_on_a_type_deriving_from_a_nonencapsulated_union"></span><span id="_SWITCH_IS__MUST_BE_SPECIFIED_ONLY_ON_A_TYPE_DERIVING_FROM_A_NONENCAPSULATED_UNION"></span>[switch_is] must be specified only on a type deriving from a nonencapsulated union</dt> <dd> The [<a href="switch-is.md"><strong>switch_is</strong></a>] keyword is incorrectly applied. It can only be used with <a href="nonencapsulated-unions.md">nonencapsulated union types</a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2191"></span><span id="midl2191"></span><dl> <dt><strong>MIDL2191</strong></dt> </dl></td>
<td><dl> <dt><span id="stringable_structures_are_not_implemented_in_this_version"></span><span id="STRINGABLE_STRUCTURES_ARE_NOT_IMPLEMENTED_IN_THIS_VERSION"></span>stringable structures are not implemented in this version</dt> <dd> DCE IDL allows the attribute [<a href="string.md"><strong>string</strong></a>] to apply to a structure whose elements consist only of characters, bytes, or types that resolve to characters or bytes. This functionality is not supported in Microsoft RPC. The [<strong>string</strong>] attribute cannot be applied to the structure as a whole. However, it can be applied to each individual array.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2192"></span><span id="midl2192"></span><dl> <dt><strong>MIDL2192</strong></dt> </dl></td>
<td><dl> <dt><span id="switch_type_can_only_be_integral__char__Boolean_or_enum"></span><span id="switch_type_can_only_be_integral__char__boolean_or_enum"></span><span id="SWITCH_TYPE_CAN_ONLY_BE_INTEGRAL__CHAR__BOOLEAN_OR_ENUM"></span>switch type can only be integral, char, Boolean or enum</dt> <dd> The specified type does not resolve to a valid switch type. Use an integer, character, <a href="byte.md"><strong>byte</strong></a>, <a href="boolean.md"><strong>Boolean</strong></a>, <a href="enum.md"><strong>enum</strong></a> type, or a type that is derived from one of these types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2193"></span><span id="midl2193"></span><dl> <dt><strong>MIDL2193</strong></dt> </dl></td>
<td><dl> <dt><span id="_handle__must_not_be_specified_on_a_type_deriving_from_handle_t"></span><span id="_HANDLE__MUST_NOT_BE_SPECIFIED_ON_A_TYPE_DERIVING_FROM_HANDLE_T"></span>[handle] must not be specified on a type deriving from handle_t</dt> <dd> A handle type must be defined using one and only one of the handle types or attributes. Use the primitive type <a href="handle-t.md"><strong>handle_t</strong></a> or the attribute [<a href="handle.md"><strong>handle</strong></a>], but not both. The user-defined handle type must be transmissible, but the <strong>handle_t</strong> type is not transmitted on the network.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2194"></span><span id="midl2194"></span><dl> <dt><strong>MIDL2194</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_deriving_from_handle_t_must_not_be_an__out__parameter"></span><span id="PARAMETER_DERIVING_FROM_HANDLE_T_MUST_NOT_BE_AN__OUT__PARAMETER"></span>parameter deriving from handle_t must not be an [out] parameter</dt> <dd> A handle of the primitive type <a href="handle-t.md"><strong>handle_t</strong></a> is meaningful only to the side of the application in which it is defined. The type <strong>handle_t</strong> is not transmitted on the network.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2195"></span><span id="midl2195"></span><dl> <dt><strong>MIDL2195</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_expression_derives_from__unique__or__ptr__pointer_dereference"></span><span id="ATTRIBUTE_EXPRESSION_DERIVES_FROM__UNIQUE__OR__PTR__POINTER_DEREFERENCE"></span>attribute expression derives from [unique] or [ptr] pointer dereference</dt> <dd> Although the [<a href="unique.md"><strong>unique</strong></a>] and <a href="ptr.md"><strong>full</strong></a> pointer attributes allow pointers to have <strong>NULL</strong> values, the expression that defines the size or length attribute must never have a <strong>NULL</strong> value. When pointers are used, MIDL constrains expressions to [<a href="ref.md"><strong>ref</strong></a>] pointers.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2196"></span><span id="midl2196"></span><dl> <dt><strong>MIDL2196</strong></dt> </dl></td>
<td><dl> <dt><span id="_cpp_quote__requires__ms_ext"></span><span id="_CPP_QUOTE__REQUIRES__MS_EXT"></span>&quot;cpp_quote&quot; requires /ms_ext</dt> <dd> The <a href="cpp-quote.md"><strong>cpp_quote</strong></a> attribute is a Microsoft extension to DCE IDL. Do not use the MIDL compiler switch <a href="-osf.md"><strong>/osf</strong></a>, which overrides <a href="-ms-ext.md"><strong>/ms_ext</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2197"></span><span id="midl2197"></span><dl> <dt><strong>MIDL2197</strong></dt> </dl></td>
<td><dl> <dt><span id="quoted_uuid_requires__ms_ext"></span><span id="QUOTED_UUID_REQUIRES__MS_EXT"></span>quoted uuid requires /ms_ext</dt> <dd> The ability to specify a UUID value within quotation marks is a Microsoft extension to DCE IDL. Do not use the MIDL compiler switch <a href="-osf.md"><strong>/osf</strong></a>, which overrides <a href="-ms-ext.md"><strong>/ms_ext</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2198"></span><span id="midl2198"></span><dl> <dt><strong>MIDL2198</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_cannot_derive_from_a_nonencapsulated_union"></span><span id="RETURN_TYPE_CANNOT_DERIVE_FROM_A_NONENCAPSULATED_UNION"></span>return type cannot derive from a nonencapsulated union</dt> <dd> The nonencapsulated union cannot be used as a function return type. To return the union type, specify the union type as an [<a href="out-idl.md"><strong>out</strong></a>] or [<strong>in, out</strong>] parameter.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2199"></span><span id="midl2199"></span><dl> <dt><strong>MIDL2199</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_cannot_derive_from_a_conformant_structure"></span><span id="RETURN_TYPE_CANNOT_DERIVE_FROM_A_CONFORMANT_STRUCTURE"></span>return type cannot derive from a conformant structure</dt> <dd> The size of the return type must be a constant. You cannot specify as a return type a structure that contains a conformant array even when the structure also includes its size specifier. To return the conformant structure, specify the structure as an [<a href="out-idl.md"><strong>out</strong></a>] or [<strong>in, out</strong>] parameter.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2200"></span><span id="midl2200"></span><dl> <dt><strong>MIDL2200</strong></dt> </dl></td>
<td><dl> <dt><span id="_transmit_as__must_not_be_applied_to_a_type_deriving_from_a_generic_handle"></span><span id="_TRANSMIT_AS__MUST_NOT_BE_APPLIED_TO_A_TYPE_DERIVING_FROM_A_GENERIC_HANDLE"></span>[transmit_as] must not be applied to a type deriving from a generic handle</dt> <dd> In this release, the [<a href="handle.md"><strong>handle</strong></a>] and [<a href="transmit-as.md"><strong>transmit_as</strong></a>] attributes cannot be combined on the same type.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2201"></span><span id="midl2201"></span><dl> <dt><strong>MIDL2201</strong></dt> </dl></td>
<td><dl> <dt><span id="_handle__must_not_be_applied_to_a_type_that_has__transmit_as__applied_to_it"></span><span id="_HANDLE__MUST_NOT_BE_APPLIED_TO_A_TYPE_THAT_HAS__TRANSMIT_AS__APPLIED_TO_IT"></span>[handle] must not be applied to a type that has [transmit_as] applied to it</dt> <dd> In this release, the [<a href="handle.md"><strong>handle</strong></a>] and [<a href="transmit-as.md"><strong>transmit_as</strong></a>] attributes cannot be combined on the same type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2202"></span><span id="midl2202"></span><dl> <dt><strong>MIDL2202</strong></dt> </dl></td>
<td><dl> <dt><span id="type_specified_for_the_const_declaration_is_invalid"></span><span id="TYPE_SPECIFIED_FOR_THE_CONST_DECLARATION_IS_INVALID"></span>type specified for the const declaration is invalid</dt> <dd> Constant declarations are limited to integer, character, wide-character, string, and Boolean types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2203"></span><span id="midl2203"></span><dl> <dt><strong>MIDL2203</strong></dt> </dl></td>
<td><dl> <dt><span id="operand_to_the_sizeof_operator_is_not_supported"></span><span id="OPERAND_TO_THE_SIZEOF_OPERATOR_IS_NOT_SUPPORTED"></span>operand to the sizeof operator is not supported</dt> <dd> The MIDL compiler supports the <strong>sizeof</strong> operation for simple types only. The specified operand does not evaluate to an integer type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2204"></span><span id="midl2204"></span><dl> <dt><strong>MIDL2204</strong></dt> </dl></td>
<td><dl> <dt><span id="this_name_already_used_as_a_const_identifier_name"></span><span id="THIS_NAME_ALREADY_USED_AS_A_CONST_IDENTIFIER_NAME"></span>this name already used as a const identifier name</dt> <dd> The identifier has previously been used to identify a constant in a <a href="const.md"><strong>const</strong></a> declaration. Change the name of one of the identifiers so that the identifiers are unique.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2205"></span><span id="midl2205"></span><dl> <dt><strong>MIDL2205</strong></dt> </dl></td>
<td><dl> <dt><span id="inconsistent_redefinition_of_type_error_status_t"></span><span id="INCONSISTENT_REDEFINITION_OF_TYPE_ERROR_STATUS_T"></span>inconsistent redefinition of type error_status_t</dt> <dd> The type <a href="error-status-t.md"><strong>error_status_t</strong></a> must resolve to the type <strong>unsigned long</strong>. Other type definitions cannot be used.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2206"></span><span id="midl2206"></span><dl> <dt><strong>MIDL2206</strong></dt> </dl></td>
<td><dl> <dt><span id="_case__value_out_of_range_of_switch_type"></span><span id="_CASE__VALUE_OUT_OF_RANGE_OF_SWITCH_TYPE"></span>[case] value out of range of switch type</dt> <dd> The value associated with the switch statement case is out of range for the specified switch type. For example, this error occurs when a long integer value is used in the case statement for a short integer type.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2207"></span><span id="midl2207"></span><dl> <dt><strong>MIDL2207</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_deriving_from_wchar_t_needs__ms_ext"></span><span id="PARAMETER_DERIVING_FROM_WCHAR_T_NEEDS__MS_EXT"></span>parameter deriving from wchar_t needs /ms_ext</dt> <dd> The wide-character type <a href="wchar-t.md"><strong>wchar_t</strong></a> is a Microsoft extension to DCE IDL. Do not use the MIDL compiler switch <a href="-osf.md"><strong>/osf</strong></a>, which overrides <a href="-ms-ext.md"><strong>/ms_ext</strong></a><br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2208"></span><span id="midl2208"></span><dl> <dt><strong>MIDL2208</strong></dt> </dl></td>
<td><dl> <dt><span id="this_interface_has_only_callbacks"></span><span id="THIS_INTERFACE_HAS_ONLY_CALLBACKS"></span>this interface has only callbacks</dt> <dd> Callbacks are valid only in the context of a remote procedure call. The interface must include at least one function prototype for a remote procedure call that does not include the [<a href="callback.md"><strong>callback</strong></a>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2209"></span><span id="midl2209"></span><dl> <dt><strong>MIDL2209</strong></dt> </dl></td>
<td><dl> <dt><span id="redundantly_specified_attribute__ignored"></span><span id="REDUNDANTLY_SPECIFIED_ATTRIBUTE__IGNORED"></span>redundantly specified attribute; ignored</dt> <dd> The specified attribute has been applied more than once. Multiple instances of the same attribute are ignored.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2210"></span><span id="midl2210"></span><dl> <dt><strong>MIDL2210</strong></dt> </dl></td>
<td><dl> <dt><span id="context_handle_type_used_for_an_implicit_handle"></span><span id="CONTEXT_HANDLE_TYPE_USED_FOR_AN_IMPLICIT_HANDLE"></span>context handle type used for an implicit handle</dt> <dd> A type that was defined using the [<a href="context-handle.md"><strong>context_handle</strong></a>] attribute has been specified as the handle type in an [ <a href="implicit-handle.md"><strong>implicit_handle</strong></a>] attribute. The attributes cannot be combined in this way.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2211"></span><span id="midl2211"></span><dl> <dt><strong>MIDL2211</strong></dt> </dl></td>
<td><dl> <dt><span id="conflicting_options_specified_for__allocate_"></span><span id="CONFLICTING_OPTIONS_SPECIFIED_FOR__ALLOCATE_"></span>conflicting options specified for [allocate]</dt> <dd> The options specified for the ACF attribute [<a href="allocate.md"><strong>allocate</strong></a>] represent conflicting directives. For example, specify either the option all_nodes or the option single_node, but not both.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2212"></span><span id="midl2212"></span><dl> <dt><strong>MIDL2212</strong></dt> </dl></td>
<td><dl> <dt><span id="error_while_writing_to_file"></span><span id="ERROR_WHILE_WRITING_TO_FILE"></span>error while writing to file</dt> <dd> An error occurred while writing to the file. This condition can be caused by errors relating to disk space, file handles, file-access restrictions, and hardware failures.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2213"></span><span id="midl2213"></span><dl> <dt><strong>MIDL2213</strong></dt> </dl></td>
<td><dl> <dt><span id="no_switch_type_found_at_definition_of_union__using_the__switch_is__type"></span><span id="NO_SWITCH_TYPE_FOUND_AT_DEFINITION_OF_UNION__USING_THE__SWITCH_IS__TYPE"></span>no switch type found at definition of union, using the [switch_is] type</dt> <dd> The union definition does not include an explicit [<a href="switch-type.md"><strong>switch_type</strong></a>] attribute. The type of the variable specified by the [<a href="switch-is.md"><strong>switch_is</strong></a>] attribute is used as the switch type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2214"></span><span id="midl2214"></span><dl> <dt><strong>MIDL2214</strong></dt> </dl></td>
<td><dl> <dt><span id="semantic_check_incomplete_due_to_previous_errors"></span><span id="SEMANTIC_CHECK_INCOMPLETE_DUE_TO_PREVIOUS_ERRORS"></span>semantic check incomplete due to previous errors</dt> <dd> The MIDL compiler makes two passes over the input file(s) to resolve any forward declarations. Due to errors encountered during the first pass, checking for the second pass has not been performed. Unreported errors relating to forward declarations may still be present in the file.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2215"></span><span id="midl2215"></span><dl> <dt><strong>MIDL2215</strong></dt> </dl></td>
<td><dl> <dt><span id="handle_parameter_or_return_type_is_not_supported_on_a__callback__procedure"></span><span id="HANDLE_PARAMETER_OR_RETURN_TYPE_IS_NOT_SUPPORTED_ON_A__CALLBACK__PROCEDURE"></span>handle parameter or return type is not supported on a [callback] procedure</dt> <dd> A [<a href="callback.md"><strong>callback</strong></a>] procedure occurs in the context of a call from a client to the server and uses the same binding handle as the original call. Explicit binding-handle parameters or return types are not permitted in callback functions.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2216"></span><span id="midl2216"></span><dl> <dt><strong>MIDL2216</strong></dt> </dl></td>
<td><dl> <dt><span id="_ptr__does_not_support_aliasing_in_this_version"></span><span id="_PTR__DOES_NOT_SUPPORT_ALIASING_IN_THIS_VERSION"></span>[ptr] does not support aliasing in this version</dt> <dd> An alias occurs when data is accessible through more than one pointer or variable name. Remove the alias. For more information, see <a href="/windows/desktop/Rpc/unique-pointers">Unique Pointers</a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2217"></span><span id="midl2217"></span><dl> <dt><strong>MIDL2217</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_already_defined_as_a_context_handle"></span><span id="PARAMETER_ALREADY_DEFINED_AS_A_CONTEXT_HANDLE"></span>parameter already defined as a context handle</dt> <dd> The parameter was previously defined as a context handle.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2218"></span><span id="midl2218"></span><dl> <dt><strong>MIDL2218</strong></dt> </dl></td>
<td><dl> <dt><span id="_context_handle__must_not_derive_from_handle_t"></span><span id="_CONTEXT_HANDLE__MUST_NOT_DERIVE_FROM_HANDLE_T"></span>[context_handle] must not derive from handle_t</dt> <dd> The three handle characteristics: the type <a href="handle-t.md"><strong>handle_t</strong></a>, the attribute [<a href="handle.md"><strong>handle</strong></a>], and the attribute [<a href="context-handle.md"><strong>context_handle</strong></a>], are mutually exclusive. Only one characteristic can be applied to a type or parameter at a time.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2219"></span><span id="midl2219"></span><dl> <dt><strong>MIDL2219</strong></dt> </dl></td>
<td><dl> <dt><span id="array_size_exceeds_65536_bytes"></span><span id="ARRAY_SIZE_EXCEEDS_65536_BYTES"></span>array size exceeds 65536 bytes</dt> <dd> On some Microsoft platforms, the maximum transmissible data size is 64K. Redesign your application so that all transmitted data fits within the maximum transmissible size.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2220"></span><span id="midl2220"></span><dl> <dt><strong>MIDL2220</strong></dt> </dl></td>
<td><dl> <dt><span id="structure_size_exceeds_65536_bytes"></span><span id="STRUCTURE_SIZE_EXCEEDS_65536_BYTES"></span>structure size exceeds 65536 bytes</dt> <dd> On some Microsoft platforms, the maximum transmissible data size is 64K. Redesign your application so that all transmitted data fits within the maximum transmissible size.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2221"></span><span id="midl2221"></span><dl> <dt><strong>MIDL2221</strong></dt> </dl></td>
<td><dl> <dt><span id="field_of_a_nonencapsulated_union_cannot_be_another_nonencapsulated_union"></span><span id="FIELD_OF_A_NONENCAPSULATED_UNION_CANNOT_BE_ANOTHER_NONENCAPSULATED_UNION"></span>field of a nonencapsulated union cannot be another nonencapsulated union</dt> <dd> Unions that are transmitted as part of a remote procedure call require an associated data item, the discriminant, that selects the union arm. Unions nested in other unions do not offer a discriminant; as a result, they cannot be transmitted in this form. Create a structure that consists of the union and its discriminant.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2222"></span><span id="midl2222"></span><dl> <dt><strong>MIDL2222</strong></dt> </dl></td>
<td><dl> <dt><span id="pointer_attribute_s__applied_on_an_embedded_array__ignored"></span><span id="POINTER_ATTRIBUTE_S__APPLIED_ON_AN_EMBEDDED_ARRAY__IGNORED"></span>pointer attribute(s) applied on an embedded array; ignored</dt> <dd> A pointer attribute can be applied to an array only when the array is a top-level parameter. Other pointer attributes applied to arrays embedded in other data structures are ignored.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2223"></span><span id="midl2223"></span><dl> <dt><strong>MIDL2223</strong></dt> </dl></td>
<td><dl> <dt><span id="_allocate__is_illegal_on_either_the_transmitted_or_presented_type_for__transmit_as____represent_as____wire_marshal___or__user_marshal_"></span><span id="_ALLOCATE__IS_ILLEGAL_ON_EITHER_THE_TRANSMITTED_OR_PRESENTED_TYPE_FOR__TRANSMIT_AS____REPRESENT_AS____WIRE_MARSHAL___OR__USER_MARSHAL_"></span>[allocate] is illegal on either the transmitted or presented type for [transmit_as], [represent_as], [wire_marshal], or [user_marshal]</dt> <dd> The [<a href="transmit-as.md"><strong>transmit_as</strong></a>] and [<a href="allocate.md"><strong>allocate</strong></a>] attributes cannot both be applied to the same type. The [<strong>transmit_as</strong>] attribute distinguishes between presented and transmitted types, while the [<strong>allocate</strong>] attribute assumes that the presented type is the same as the transmitted type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2224"></span><span id="midl2224"></span><dl> <dt><strong>MIDL2224</strong></dt> </dl></td>
<td>[switch_type] must be specified in this import mode<br/></td>
</tr>
<tr class="even">
<td><span id="MIDL2225"></span><span id="midl2225"></span><dl> <dt><strong>MIDL2225</strong></dt> </dl></td>
<td><dl> <dt><span id="_implicit_handle__type_undefined__assuming_generic_handle"></span><span id="_IMPLICIT_HANDLE__TYPE_UNDEFINED__ASSUMING_GENERIC_HANDLE"></span>[implicit_handle] type undefined; assuming generic handle</dt> <dd> The handle type specified in the ACF is not defined in the IDL file. The MIDL compiler assumes that the handle type resolves to the primitive handle type <a href="handle-t.md"><strong>handle_t</strong></a>. Add the [<a href="handle.md"><strong>handle</strong></a>] attribute to the type definition if you want the handle to behave like a user-defined or generic handle.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2226"></span><span id="midl2226"></span><dl> <dt><strong>MIDL2226</strong></dt> </dl></td>
<td><dl> <dt><span id="array_element_must_not_derive_from_error_status_t"></span><span id="ARRAY_ELEMENT_MUST_NOT_DERIVE_FROM_ERROR_STATUS_T"></span>array element must not derive from error_status_t</dt> <dd> In this release of Microsoft RPC, the type <a href="error-status-t.md"><strong>error_status_t</strong></a> can appear only as a parameter or return type. It cannot appear in arrays.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2227"></span><span id="midl2227"></span><dl> <dt><strong>MIDL2227</strong></dt> </dl></td>
<td><dl> <dt><span id="_allocate__illegal_on_a_type_deriving_from_a_primitive_generic_context_handle"></span><span id="_ALLOCATE__ILLEGAL_ON_A_TYPE_DERIVING_FROM_A_PRIMITIVE_GENERIC_CONTEXT_HANDLE"></span>[allocate] illegal on a type deriving from a primitive/generic/context handle</dt> <dd> By design, the ACF attribute [<a href="allocate.md"><strong>allocate</strong></a>] cannot be applied to handle types.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2228"></span><span id="midl2228"></span><dl> <dt><strong>MIDL2228</strong></dt> </dl></td>
<td><dl> <dt><span id="transmitted_or_presented_type_must_not_derive_from_error_status_t"></span><span id="TRANSMITTED_OR_PRESENTED_TYPE_MUST_NOT_DERIVE_FROM_ERROR_STATUS_T"></span>transmitted or presented type must not derive from error_status_t</dt> <dd> In this release of Microsoft RPC, the type <a href="error-status-t.md"><strong>error_status_t</strong></a> cannot be used with the [<a href="transmit-as.md"><strong>transmit_as</strong></a>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2229"></span><span id="midl2229"></span><dl> <dt><strong>MIDL2229</strong></dt> </dl></td>
<td><dl> <dt><span id="discriminant_of_a_union_must_not_derive_from_a_field_with__ignore__applied_to_it"></span><span id="DISCRIMINANT_OF_A_UNION_MUST_NOT_DERIVE_FROM_A_FIELD_WITH__IGNORE__APPLIED_TO_IT"></span>discriminant of a union must not derive from a field with [ignore] applied to it</dt> <dd> A union used in a remote procedure call must be associated with another data item, called the discriminant, that selects the union arm. The discriminant must be transmitted. The [<a href="ignore.md"><strong>ignore</strong></a>] attribute cannot be applied to the union discriminant.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2230"></span><span id="midl2230"></span><dl> <dt><strong>MIDL2230</strong></dt> </dl></td>
<td><dl> <dt><span id="_nocode__ignored_for_server_side_since___server_none__not_specified"></span><span id="_NOCODE__IGNORED_FOR_SERVER_SIDE_SINCE___SERVER_NONE__NOT_SPECIFIED"></span>[nocode] ignored for server side since &quot;/server none&quot; not specified</dt> <dd> Some DCE IDL compilers generate an error when the [<a href="nocode.md"><strong>nocode</strong></a>] attribute is applied to a procedure in an interface for which server stub files are being generated. Because the server must support all operations, [<strong>nocode</strong>] must not be applied to a procedure in this mode, or you must use the MIDL compiler switch <a href="-server.md"><strong>/server</strong></a> none to explicitly specify that no server routines are to be generated.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2231"></span><span id="midl2231"></span><dl> <dt><strong>MIDL2231</strong></dt> </dl></td>
<td><dl> <dt><span id="no_remote_procedures_specified_in_non-_local__interface__no_client_server_stubs_will_be_generated"></span><span id="NO_REMOTE_PROCEDURES_SPECIFIED_IN_NON-_LOCAL__INTERFACE__NO_CLIENT_SERVER_STUBS_WILL_BE_GENERATED"></span>no remote procedures specified in non-[local] interface; no client/server stubs will be generated</dt> <dd> The provided interface does not have any remote procedures, so only header files will be generated.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2232"></span><span id="midl2232"></span><dl> <dt><strong>MIDL2232</strong></dt> </dl></td>
<td><dl> <dt><span id="too_many_default_cases_specified_for_encapsulated_union"></span><span id="TOO_MANY_DEFAULT_CASES_SPECIFIED_FOR_ENCAPSULATED_UNION"></span>too many default cases specified for encapsulated union</dt> <dd> An encapsulated union can have only one default: arm.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2233"></span><span id="midl2233"></span><dl> <dt><strong>MIDL2233</strong></dt> </dl></td>
<td><dl> <dt><span id="too_many_default_interfaces_specified_for_coclass"></span><span id="TOO_MANY_DEFAULT_INTERFACES_SPECIFIED_FOR_COCLASS"></span>too many default interfaces specified for coclass</dt> <dd> A <a href="coclass.md"><strong>coclass</strong></a> can have at most two [<a href="default.md"><strong>default</strong></a>] members, one to represent the outgoing (source) interface or dispinterface, and one to represent the incoming (sink) interface or dispinterface.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2234"></span><span id="midl2234"></span><dl> <dt><strong>MIDL2234</strong></dt> </dl></td>
<td><dl> <dt><span id="items_with__defaultvtable__must_also_have__source_"></span><span id="ITEMS_WITH__DEFAULTVTABLE__MUST_ALSO_HAVE__SOURCE_"></span>items with [defaultvtable] must also have [source]</dt> <dd> The <a href="defaultvtable.md"><strong>defaultvtable</strong></a> interface creates a second source interface for an object, one that lets sinks receive events through the V-table.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2235"></span><span id="midl2235"></span><dl> <dt><strong>MIDL2235</strong></dt> </dl></td>
<td><dl> <dt><span id="union_specification_with_no_fields_is_illegal"></span><span id="UNION_SPECIFICATION_WITH_NO_FIELDS_IS_ILLEGAL"></span>union specification with no fields is illegal</dt> <dd> Unions must have at least one field.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2236"></span><span id="midl2236"></span><dl> <dt><strong>MIDL2236</strong></dt> </dl></td>
<td><dl> <dt><span id="value_out_of_range"></span><span id="VALUE_OUT_OF_RANGE"></span>value out of range</dt> <dd> The provided case value is out of the range of the switch type.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2237"></span><span id="midl2237"></span><dl> <dt><strong>MIDL2237</strong></dt> </dl></td>
<td><dl> <dt><span id="_context_handle__must_be_applied_on_a_pointer_type"></span><span id="_CONTEXT_HANDLE__MUST_BE_APPLIED_ON_A_POINTER_TYPE"></span>[context_handle] must be applied on a pointer type</dt> <dd> Context handles must always be pointer types. DCE specifies that all context handles must be typed as <strong>void *</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2238"></span><span id="midl2238"></span><dl> <dt><strong>MIDL2238</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_must_not_derive_from_handle_t"></span><span id="RETURN_TYPE_MUST_NOT_DERIVE_FROM_HANDLE_T"></span>return type must not derive from handle_t</dt> <dd><a href="handle-t.md"><strong>handle_t</strong></a> cannot be returned.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2239"></span><span id="midl2239"></span><dl> <dt><strong>MIDL2239</strong></dt> </dl></td>
<td><dl> <dt><span id="_handle__must_not_be_applied_to_a_type_deriving_from_a_context_handle"></span><span id="_HANDLE__MUST_NOT_BE_APPLIED_TO_A_TYPE_DERIVING_FROM_A_CONTEXT_HANDLE"></span>[handle] must not be applied to a type deriving from a context handle</dt> <dd> A type cannot be both a context handle and a generic handle.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2240"></span><span id="midl2240"></span><dl> <dt><strong>MIDL2240</strong></dt> </dl></td>
<td><dl> <dt><span id="field_deriving_from_an__int__must_have_size_specifier__small____short___or__long__with_the__int_"></span><span id="FIELD_DERIVING_FROM_AN__INT__MUST_HAVE_SIZE_SPECIFIER__SMALL____SHORT___OR__LONG__WITH_THE__INT_"></span>field deriving from an &quot;int&quot; must have size specifier &quot;small&quot;, &quot;short&quot;, or &quot;long&quot; with the &quot;int&quot;</dt> <dd> The type <a href="int.md"><strong>int</strong></a> is not transmissible on 16-bit systems, since the size of <strong>int</strong> may be different across machines.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2241"></span><span id="midl2241"></span><dl> <dt><strong>MIDL2241</strong></dt> </dl></td>
<td><dl> <dt><span id="field_must_not_derive_from_a_void_or_void__"></span><span id="FIELD_MUST_NOT_DERIVE_FROM_A_VOID_OR_VOID__"></span>field must not derive from a void or void *</dt> <dd> <strong>void</strong> and <strong>void *</strong> cannot be used as parameter types for remote procedures.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2242"></span><span id="midl2242"></span><dl> <dt><strong>MIDL2242</strong></dt> </dl></td>
<td><dl> <dt><span id="field_must_not_derive_from_a_structure_containing_bit-fields"></span><span id="FIELD_MUST_NOT_DERIVE_FROM_A_STRUCTURE_CONTAINING_BIT-FIELDS"></span>field must not derive from a structure containing bit-fields</dt> <dd> Structures containing bit fields cannot be used as parameters or return types for remote procedures.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2243"></span><span id="midl2243"></span><dl> <dt><strong>MIDL2243</strong></dt> </dl></td>
<td><dl> <dt><span id="field_must_not_derive_from_a_non-rpcable_union"></span><span id="FIELD_MUST_NOT_DERIVE_FROM_A_NON-RPCABLE_UNION"></span>field must not derive from a non-rpcable union</dt> <dd> A union must be specified as a nonencapsulated union or encapsulated union in order to be transmitted. Ordinary C unions lack the discriminant needed to transmit the union across the network.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2244"></span><span id="midl2244"></span><dl> <dt><strong>MIDL2244</strong></dt> </dl></td>
<td><dl> <dt><span id="field_must_not_derive_from_a_pointer_to_a_function"></span><span id="FIELD_MUST_NOT_DERIVE_FROM_A_POINTER_TO_A_FUNCTION"></span>field must not derive from a pointer to a function</dt> <dd> Pointers to functions cannot be transmitted to remote procedures. Pointers to functions point to function code, and no function code can be transmitted across the network using RPC.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2245"></span><span id="midl2245"></span><dl> <dt><strong>MIDL2245</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_use__fault_status__on_both_a_parameter_and_a_return_type"></span><span id="CANNOT_USE__FAULT_STATUS__ON_BOTH_A_PARAMETER_AND_A_RETURN_TYPE"></span>cannot use [fault_status] on both a parameter and a return type</dt> <dd> The attribute [<a href="fault-status.md"><strong>fault_status</strong></a>] can be used only once per procedure. The [<a href="comm-status.md"><strong>comm_status</strong></a>] attribute can be used independently.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2246"></span><span id="midl2246"></span><dl> <dt><strong>MIDL2246</strong></dt> </dl></td>
<td><dl> <dt><span id="return_type_too_complicated_for__Oi_modes__using__Os"></span><span id="return_type_too_complicated_for__oi_modes__using__os"></span><span id="RETURN_TYPE_TOO_COMPLICATED_FOR__OI_MODES__USING__OS"></span>return type too complicated for /Oi modes, using /Os</dt> <dd> Large return types that are passed by value can be handled only by <a href="-os.md"><strong>/Os</strong></a> optimization stubs. The stubs for this routine will be generated using <strong>/Os</strong> optimization.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2247"></span><span id="midl2247"></span><dl> <dt><strong>MIDL2247</strong></dt> </dl></td>
<td><dl> <dt><span id="generic_handle_type_too_large_for__Oi_modes__using__Os"></span><span id="generic_handle_type_too_large_for__oi_modes__using__os"></span><span id="GENERIC_HANDLE_TYPE_TOO_LARGE_FOR__OI_MODES__USING__OS"></span>generic handle type too large for /Oi modes, using /Os</dt> <dd> Large generic handle types that are passed by value can be handled only by <a href="-os.md"><strong>/Os</strong></a> optimization stubs. The stubs for this routine will be generated using <strong>/Os</strong> optimization.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2248"></span><span id="midl2248"></span><dl> <dt><strong>MIDL2248</strong></dt> </dl></td>
<td><dl> <dt><span id="_allocate_all_nodes___on_an__in_out__parameter_may_orphan_the_original_memory"></span><span id="_ALLOCATE_ALL_NODES___ON_AN__IN_OUT__PARAMETER_MAY_ORPHAN_THE_ORIGINAL_MEMORY"></span>[allocate(all_nodes)] on an [in,out] parameter may orphan the original memory</dt> <dd> Use of [<a href="allocate.md"><strong>allocate</strong></a>(all_nodes)] on an [<a href="in.md"><strong>in</strong></a>, <a href="out-idl.md"><strong>out</strong></a>] parameter must reallocate contiguous memory for the [<strong>out</strong>] direction, thus orphaning the [<strong>in</strong>] parameter. This usage is not recommended.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2249"></span><span id="midl2249"></span><dl> <dt><strong>MIDL2249</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_have_a__ref__pointer_as_a_union_arm"></span><span id="CANNOT_HAVE_A__REF__POINTER_AS_A_UNION_ARM"></span>cannot have a [ref] pointer as a union arm</dt> <dd> Reference pointers must always point to valid memory, but an [<a href="in.md"><strong>in</strong></a>, <a href="out-idl.md"><strong>out</strong></a>] union with a reference pointer may return a reference pointer when the [<strong>in</strong>] direction used another type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2250"></span><span id="midl2250"></span><dl> <dt><strong>MIDL2250</strong></dt> </dl></td>
<td><dl> <dt><span id="return_of_context_handles_not_supported_for__Oi_modes__using__Os"></span><span id="return_of_context_handles_not_supported_for__oi_modes__using__os"></span><span id="RETURN_OF_CONTEXT_HANDLES_NOT_SUPPORTED_FOR__OI_MODES__USING__OS"></span>return of context handles not supported for /Oi modes, using /Os</dt> <dd> MIDL does not support context handles in the fully interpreted optimization modes. Switching to mixed-mode optimization.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2251"></span><span id="midl2251"></span><dl> <dt><strong>MIDL2251</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_the_extra__comm_status__or__fault_status__parameter_not_supported_for__Oi_modes__using__Os"></span><span id="use_of_the_extra__comm_status__or__fault_status__parameter_not_supported_for__oi_modes__using__os"></span><span id="USE_OF_THE_EXTRA__COMM_STATUS__OR__FAULT_STATUS__PARAMETER_NOT_SUPPORTED_FOR__OI_MODES__USING__OS"></span>use of the extra [comm_status] or [fault_status] parameter not supported for /Oi modes, using /Os</dt> <dd> The [<a href="comm-status.md"><strong>comm_status</strong></a>] and [<a href="fault-status.md"><strong>fault_status</strong></a>] attributes can be handled only by <a href="-os.md"><strong>/Os</strong></a> optimization stubs. The stubs for this routine will be generated using <strong>/Os</strong> optimization.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2252"></span><span id="midl2252"></span><dl> <dt><strong>MIDL2252</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of_an_unknown_type_for__represent_as__or__user_marshal__not_supported_for__Oi_modes__using__Os"></span><span id="use_of_an_unknown_type_for__represent_as__or__user_marshal__not_supported_for__oi_modes__using__os"></span><span id="USE_OF_AN_UNKNOWN_TYPE_FOR__REPRESENT_AS__OR__USER_MARSHAL__NOT_SUPPORTED_FOR__OI_MODES__USING__OS"></span>use of an unknown type for [represent_as] or [user_marshal] not supported for /Oi modes, using /Os</dt> <dd> Use of the [<a href="represent-as.md"><strong>represent_as</strong></a>] attribute with a local type that is not defined in the IDL file or an imported IDL file can be handled only by <a href="-os.md"><strong>/Os</strong></a> optimization stubs. The stubs for this routine will be generated using <strong>/Os</strong> optimization.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2253"></span><span id="midl2253"></span><dl> <dt><strong>MIDL2253</strong></dt> </dl></td>
<td><dl> <dt><span id="array_types_with__transmit_as__or__represent_as__not_supported_on_return_type_for__Oi_modes___using__Os"></span><span id="array_types_with__transmit_as__or__represent_as__not_supported_on_return_type_for__oi_modes___using__os"></span><span id="ARRAY_TYPES_WITH__TRANSMIT_AS__OR__REPRESENT_AS__NOT_SUPPORTED_ON_RETURN_TYPE_FOR__OI_MODES___USING__OS"></span>array types with [transmit_as] or [represent_as] not supported on return type for /Oi modes , using /Os</dt> <dd> Returning an array with [<a href="transmit-as.md"><strong>transmit_as</strong></a>] or [<a href="represent-as.md"><strong>represent_as</strong></a>] applied can only be handled by <a href="-os.md"><strong>/Os</strong></a> optimization stubs. The stubs for this routine will be generated using <strong>/Os</strong> optimization.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2254"></span><span id="midl2254"></span><dl> <dt><strong>MIDL2254</strong></dt> </dl></td>
<td><dl> <dt><span id="array_types_with__transmit_as__or__represent_as__not_supported_pass-by-value_for__Oi_modes__using__Os"></span><span id="array_types_with__transmit_as__or__represent_as__not_supported_pass-by-value_for__oi_modes__using__os"></span><span id="ARRAY_TYPES_WITH__TRANSMIT_AS__OR__REPRESENT_AS__NOT_SUPPORTED_PASS-BY-VALUE_FOR__OI_MODES__USING__OS"></span>array types with [transmit_as] or [represent_as] not supported pass-by-value for /Oi modes, using /Os</dt> <dd> This action is not supported for fully-interpreted optimization. Switching to mixed-mode optimization.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2255"></span><span id="midl2255"></span><dl> <dt><strong>MIDL2255</strong></dt> </dl></td>
<td><dl> <dt><span id="_callback__requires__ms_ext"></span><span id="_CALLBACK__REQUIRES__MS_EXT"></span>[callback] requires /ms_ext</dt> <dd> The [<a href="callback.md"><strong>callback</strong></a>] attribute is a Microsoft extension and requires that the <a href="-ms-ext.md"><strong>/ms_ext</strong></a> switch be enabled. Do not compile with <a href="-osf.md"><strong>/osf</strong></a>, which overrides <strong>/ms_ext</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2256"></span><span id="midl2256"></span><dl> <dt><strong>MIDL2256</strong></dt> </dl></td>
<td><dl> <dt><span id="circular_interface_dependency"></span><span id="CIRCULAR_INTERFACE_DEPENDENCY"></span>circular interface dependency</dt> <dd> This interface uses itself (directly or indirectly) as a base interface.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2257"></span><span id="midl2257"></span><dl> <dt><strong>MIDL2257</strong></dt> </dl></td>
<td><dl> <dt><span id="only_IUnknown_may_be_used_as_the_root_interface"></span><span id="only_iunknown_may_be_used_as_the_root_interface"></span><span id="ONLY_IUNKNOWN_MAY_BE_USED_AS_THE_ROOT_INTERFACE"></span>only IUnknown may be used as the root interface</dt> <dd> Currently, all interfaces must have <a href="/windows/desktop/api/unknwn/nn-unknwn-iunknown"><strong>IUnknown</strong></a> as the root interface.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2258"></span><span id="midl2258"></span><dl> <dt><strong>MIDL2258</strong></dt> </dl></td>
<td><dl> <dt><span id="_IID_IS__may_only_be_applied_to_pointers_to_interfaces"></span><span id="_iid_is__may_only_be_applied_to_pointers_to_interfaces"></span><span id="_IID_IS__MAY_ONLY_BE_APPLIED_TO_POINTERS_TO_INTERFACES"></span>[IID_IS] may only be applied to pointers to interfaces</dt> <dd> The [<a href="iid-is.md"><strong>iid_is</strong></a>] attribute can only be applied to interface pointers, although they can be specified as pointers to <a href="/windows/desktop/api/unknwn/nn-unknwn-iunknown"><strong>IUnknown</strong></a> *.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2259"></span><span id="midl2259"></span><dl> <dt><strong>MIDL2259</strong></dt> </dl></td>
<td><dl> <dt><span id="interfaces_may_only_be_used_in_pointer-to-interface_constructs"></span><span id="INTERFACES_MAY_ONLY_BE_USED_IN_POINTER-TO-INTERFACE_CONSTRUCTS"></span>interfaces may only be used in pointer-to-interface constructs</dt> <dd> Interface names cannot be used except as base interfaces or interface pointers.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2260"></span><span id="midl2260"></span><dl> <dt><strong>MIDL2260</strong></dt> </dl></td>
<td><dl> <dt><span id="interface_pointers_must_have_a_UUID_IID"></span><span id="interface_pointers_must_have_a_uuid_iid"></span><span id="INTERFACE_POINTERS_MUST_HAVE_A_UUID_IID"></span>interface pointers must have a UUID/IID</dt> <dd> The base type of the [<a href="iid-is.md"><strong>iid_is</strong></a>] expression must be a UUID/GUID/IID type.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2261"></span><span id="midl2261"></span><dl> <dt><strong>MIDL2261</strong></dt> </dl></td>
<td><dl> <dt><span id="definitions_and_declarations_outside_of_interface_body_requires__ms_ext"></span><span id="DEFINITIONS_AND_DECLARATIONS_OUTSIDE_OF_INTERFACE_BODY_REQUIRES__MS_EXT"></span>definitions and declarations outside of interface body requires /ms_ext</dt> <dd> Putting declarations and definitions outside of any interface body is a Microsoft extension and requires the use of the <a href="-ms-ext.md"><strong>/ms_ext</strong></a> switch.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2262"></span><span id="midl2262"></span><dl> <dt><strong>MIDL2262</strong></dt> </dl></td>
<td><dl> <dt><span id="multiple_interfaces_in_one_file_requires__ms_ext"></span><span id="MULTIPLE_INTERFACES_IN_ONE_FILE_REQUIRES__MS_EXT"></span>multiple interfaces in one file requires /ms_ext</dt> <dd> Using multiple interfaces in a single idl file is a Microsoft extension and is not available when you compile in <a href="-osf.md"><strong>/osf</strong></a> mode.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2263"></span><span id="midl2263"></span><dl> <dt><strong>MIDL2263</strong></dt> </dl></td>
<td><dl> <dt><span id="only_one_of__implicit_handle____auto_handle___or__explicit_handle__allowed"></span><span id="ONLY_ONE_OF__IMPLICIT_HANDLE____AUTO_HANDLE___OR__EXPLICIT_HANDLE__ALLOWED"></span>only one of [implicit_handle], [auto_handle], or [explicit_handle] allowed</dt> <dd> Each interface can have only one of these three attributes.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2264"></span><span id="midl2264"></span><dl> <dt><strong>MIDL2264</strong></dt> </dl></td>
<td><dl> <dt><span id="_implicit_handle__references_a_type_which_is_not_a_handle"></span><span id="_IMPLICIT_HANDLE__REFERENCES_A_TYPE_WHICH_IS_NOT_A_HANDLE"></span>[implicit_handle] references a type which is not a handle</dt> <dd> Implicit handles must be of one of the handle types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2265"></span><span id="midl2265"></span><dl> <dt><strong>MIDL2265</strong></dt> </dl></td>
<td><dl> <dt><span id="_object__procs_may_only_be_used_with___env_win32_"></span><span id="_OBJECT__PROCS_MAY_ONLY_BE_USED_WITH___ENV_WIN32_"></span>[object] procs may only be used with &quot;/env win32&quot;</dt> <dd> Interfaces with the [<a href="object.md"><strong>object</strong></a>] attribute cannot be used with 16-bit environments.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2266"></span><span id="midl2266"></span><dl> <dt><strong>MIDL2266</strong></dt> </dl></td>
<td><dl> <dt><span id="_callback__with_-env_dos_win16_not_supported_for__Oi__using__Os"></span><span id="_callback__with_-env_dos_win16_not_supported_for__oi__using__os"></span><span id="_CALLBACK__WITH_-ENV_DOS_WIN16_NOT_SUPPORTED_FOR__OI__USING__OS"></span>[callback] with -env dos/win16 not supported for /Oi, using /Os</dt> <dd> Callbacks in 16-bit environments can be handled only by <a href="-os.md"><strong>/Os</strong></a> optimization stubs. The stubs for this routine will be generated using <strong>/Os</strong> optimization.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2267"></span><span id="midl2267"></span><dl> <dt><strong>MIDL2267</strong></dt> </dl></td>
<td><dl> <dt><span id="float_double_not_supported_as_top-level_parameter_for__Oi_mode__using__Os"></span><span id="float_double_not_supported_as_top-level_parameter_for__oi_mode__using__os"></span><span id="FLOAT_DOUBLE_NOT_SUPPORTED_AS_TOP-LEVEL_PARAMETER_FOR__OI_MODE__USING__OS"></span>float/double not supported as top-level parameter for /Oi mode, using /Os</dt> <dd> The float and double types can only be handled as parameters by the <a href="-os.md"><strong>/Os</strong></a> optimization stubs. The stubs for this routine will be generated using <strong>/Os</strong> optimization. The float and double types within structures, arrays, or unions can still be handled with<strong>/Os</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2268"></span><span id="midl2268"></span><dl> <dt><strong>MIDL2268</strong></dt> </dl></td>
<td><dl> <dt><span id="pointers_to_context_handles_may_not_be_used_as_return_values"></span><span id="POINTERS_TO_CONTEXT_HANDLES_MAY_NOT_BE_USED_AS_RETURN_VALUES"></span>pointers to context handles may not be used as return values</dt> <dd> Context handles must be used as direct return values, not indirect return values.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2269"></span><span id="midl2269"></span><dl> <dt><strong>MIDL2269</strong></dt> </dl></td>
<td><dl> <dt><span id="procedures_in_an_object_interface_must_return_an_HRESULT"></span><span id="procedures_in_an_object_interface_must_return_an_hresult"></span><span id="PROCEDURES_IN_AN_OBJECT_INTERFACE_MUST_RETURN_AN_HRESULT"></span>procedures in an object interface must return an HRESULT</dt> <dd> All procedures in an object interface that do not have the-[<a href="local.md"><strong>local</strong></a>] attribute must return an <strong>HRESULT</strong>/<strong>SCODE</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2270"></span><span id="midl2270"></span><dl> <dt><strong>MIDL2270</strong></dt> </dl></td>
<td><dl> <dt><span id="duplicate_UUID"></span><span id="duplicate_uuid"></span><span id="DUPLICATE_UUID"></span>duplicate UUID</dt> <dd> Same as UUIDs must be unique.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2271"></span><span id="midl2271"></span><dl> <dt><strong>MIDL2271</strong></dt> </dl></td>
<td><dl> <dt><span id="_object__interfaces_must_derive_from_another__object__interface_such_as_IUnknown"></span><span id="_object__interfaces_must_derive_from_another__object__interface_such_as_iunknown"></span><span id="_OBJECT__INTERFACES_MUST_DERIVE_FROM_ANOTHER__OBJECT__INTERFACE_SUCH_AS_IUNKNOWN"></span>[object] interfaces must derive from another [object] interface such as IUnknown</dt> <dd> Interface inheritance is allowed only when you are using object interfaces.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2272"></span><span id="midl2272"></span><dl> <dt><strong>MIDL2272</strong></dt> </dl></td>
<td><dl> <dt><span id="_async__interface_must_derive_from_another__async__interface"></span><span id="_ASYNC__INTERFACE_MUST_DERIVE_FROM_ANOTHER__ASYNC__INTERFACE"></span>(async) interface must derive from another (async) interface</dt> <dd> Object interfaces, both synchronous and asynchronous, must derive from <a href="/windows/desktop/api/unknwn/nn-unknwn-iunknown"><strong>IUnknown</strong></a> or some other base OLE interface.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2273"></span><span id="midl2273"></span><dl> <dt><strong>MIDL2273</strong></dt> </dl></td>
<td><dl> <dt><span id="_IID_IS__expression_must_be_a_pointer_to_IID_structure"></span><span id="_iid_is__expression_must_be_a_pointer_to_iid_structure"></span><span id="_IID_IS__EXPRESSION_MUST_BE_A_POINTER_TO_IID_STRUCTURE"></span>[IID_IS] expression must be a pointer to IID structure</dt> <dd> The base type of the [<a href="iid-is.md"><strong>iid_is</strong></a>] expression must be a UUID/GUID/IID type.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2274"></span><span id="midl2274"></span><dl> <dt><strong>MIDL2274</strong></dt> </dl></td>
<td><dl> <dt><span id="_call_as__type_must_be_a__local__procedure"></span><span id="_CALL_AS__TYPE_MUST_BE_A__LOCAL__PROCEDURE"></span>[call_as] type must be a [local] procedure</dt> <dd> The target of a [<a href="call-as.md"><strong>call_as</strong></a>] type, if defined, must have [ <a href="local.md"><strong>local</strong></a>] applied.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2275"></span><span id="midl2275"></span><dl> <dt><strong>MIDL2275</strong></dt> </dl></td>
<td><dl> <dt><span id="undefined__call_as__must_not_be_used_in_an_object_interface"></span><span id="UNDEFINED__CALL_AS__MUST_NOT_BE_USED_IN_AN_OBJECT_INTERFACE"></span>undefined [call_as] must not be used in an object interface</dt> <dd> You must define the target of a [<a href="call-as.md"><strong>call_as</strong></a>] type. Make sure you have supplied <strong>call_as</strong> routines for both the calling and called applications.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2276"></span><span id="midl2276"></span><dl> <dt><strong>MIDL2276</strong></dt> </dl></td>
<td><dl> <dt><span id="_auto_handle__may_not_be_used_with__encode__or__decode_"></span><span id="_AUTO_HANDLE__MAY_NOT_BE_USED_WITH__ENCODE__OR__DECODE_"></span>[auto_handle] may not be used with [encode] or [decode]</dt> <dd> The [ <a href="encode.md"><strong>encode</strong></a>] and [ <a href="decode.md"><strong>decode</strong></a>] attributes can be used only with explicit handles or implicit handles.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2277"></span><span id="midl2277"></span><dl> <dt><strong>MIDL2277</strong></dt> </dl></td>
<td><dl> <dt><span id="normal_procedures_are_not_allowed_in_an_interface_with__encode__or__decode_"></span><span id="NORMAL_PROCEDURES_ARE_NOT_ALLOWED_IN_AN_INTERFACE_WITH__ENCODE__OR__DECODE_"></span>normal procedures are not allowed in an interface with [encode] or [decode]</dt> <dd> Interfaces containing [<a href="encode.md"><strong>encode</strong></a>] or [<a href="decode.md"><strong>decode</strong></a>] procedures cannot also have remote procedures.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2278"></span><span id="midl2278"></span><dl> <dt><strong>MIDL2278</strong></dt> </dl></td>
<td><dl> <dt><span id="top-level_conformance_or_variance_not_allowed_with__encode__or__decode_"></span><span id="TOP-LEVEL_CONFORMANCE_OR_VARIANCE_NOT_ALLOWED_WITH__ENCODE__OR__DECODE_"></span>top-level conformance or variance not allowed with [encode] or [decode]</dt> <dd> Types that have top-level conformance or variance cannot use type serialization, since there is no way to provide sizing/lengthening. Structures containing them are, however, allowed to use type serialization.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2279"></span><span id="midl2279"></span><dl> <dt><strong>MIDL2279</strong></dt> </dl></td>
<td><dl> <dt><span id="_out__parameters_may_not_have__const_"></span><span id="_OUT__PARAMETERS_MAY_NOT_HAVE__CONST_"></span>[out] parameters may not have &quot;const&quot;</dt> <dd> Since an [<a href="out-idl.md"><strong>out</strong></a>] parameter is altered, it must not be declared as sa constant.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2280"></span><span id="midl2280"></span><dl> <dt><strong>MIDL2280</strong></dt> </dl></td>
<td><dl> <dt><span id="return_values_may_not_have__const_"></span><span id="RETURN_VALUES_MAY_NOT_HAVE__CONST_"></span>return values may not have &quot;const&quot;</dt> <dd> Since a function value is set when the function returns, this value must not be declared as a constant.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2281"></span><span id="midl2281"></span><dl> <dt><strong>MIDL2281</strong></dt> </dl></td>
<td><dl> <dt><span id="invalid_use_of__retval__attribute"></span><span id="INVALID_USE_OF__RETVAL__ATTRIBUTE"></span>invalid use of &quot;retval&quot; attribute</dt> <dd> Check to make sure you have not used the [<a href="optional.md"><strong>optional</strong></a>] attribute and that the [<a href="retval.md"><strong>retval</strong></a>] parameter is the last parameter in the list.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2282"></span><span id="midl2282"></span><dl> <dt><strong>MIDL2282</strong></dt> </dl></td>
<td><dl> <dt><span id="multiple_calling_conventions_illegal"></span><span id="MULTIPLE_CALLING_CONVENTIONS_ILLEGAL"></span>multiple calling conventions illegal</dt> <dd> Only one calling convention can be applied to a single procedure.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2283"></span><span id="midl2283"></span><dl> <dt><strong>MIDL2283</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_illegal_on__object__procedure"></span><span id="ATTRIBUTE_ILLEGAL_ON__OBJECT__PROCEDURE"></span>attribute illegal on [object] procedure</dt> <dd> The above attribute only applies to procedures in interfaces that do not have the [<a href="object.md"><strong>object</strong></a>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2284"></span><span id="midl2284"></span><dl> <dt><strong>MIDL2284</strong></dt> </dl></td>
<td><dl> <dt><span id="_out__interface_pointers_must_use_double_indirection"></span><span id="_OUT__INTERFACE_POINTERS_MUST_USE_DOUBLE_INDIRECTION"></span>[out] interface pointers must use double indirection</dt> <dd> Since the altered value is the pointer to the interface, there must be another level of indirection above the pointer to allow it to be returned.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2285"></span><span id="midl2285"></span><dl> <dt><strong>MIDL2285</strong></dt> </dl></td>
<td><dl> <dt><span id="procedure_used_twice_as_the_caller_in__call_as_"></span><span id="PROCEDURE_USED_TWICE_AS_THE_CALLER_IN__CALL_AS_"></span>procedure used twice as the caller in [call_as]</dt> <dd> A given [<a href="local.md"><strong>local</strong></a>] procedure can be used only once as the target of a [<a href="call-as.md"><strong>call_as</strong></a>], in order to avoid name clashes.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2286"></span><span id="midl2286"></span><dl> <dt><strong>MIDL2286</strong></dt> </dl></td>
<td><dl> <dt><span id="_call_as__target_must_have__local__in_an_object_interface"></span><span id="_CALL_AS__TARGET_MUST_HAVE__LOCAL__IN_AN_OBJECT_INTERFACE"></span>[call_as] target must have [local] in an object interface</dt> <dd> The target of a [<a href="call-as.md"><strong>call_as</strong></a>] must be a defined [<a href="local.md"><strong>local</strong></a>] procedure in the current interface.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2287"></span><span id="midl2287"></span><dl> <dt><strong>MIDL2287</strong></dt> </dl></td>
<td><dl> <dt><span id="_code__and__nocode__may_not_be_used_together"></span><span id="_CODE__AND__NOCODE__MAY_NOT_BE_USED_TOGETHER"></span>[code] and [nocode] may not be used together</dt> <dd> These two attributes are contradictory and cannot be used together.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2288"></span><span id="midl2288"></span><dl> <dt><strong>MIDL2288</strong></dt> </dl></td>
<td><dl> <dt><span id="procedures_with__maybe__or__message__attributes_may_not_have__out__params__or_return_values_must_be_of_type_HRESULT_or_error_status_t"></span><span id="procedures_with__maybe__or__message__attributes_may_not_have__out__params__or_return_values_must_be_of_type_hresult_or_error_status_t"></span><span id="PROCEDURES_WITH__MAYBE__OR__MESSAGE__ATTRIBUTES_MAY_NOT_HAVE__OUT__PARAMS__OR_RETURN_VALUES_MUST_BE_OF_TYPE_HRESULT_OR_ERROR_STATUS_T"></span>procedures with [maybe] or [message] attributes may not have [out] params, or return values must be of type HRESULT or error_status_t</dt> <dd> Since [<a href="maybe.md"><strong>maybe</strong></a>] procedures never return, there is no way to get return values.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2289"></span><span id="midl2289"></span><dl> <dt><strong>MIDL2289</strong></dt> </dl></td>
<td><dl> <dt><span id="pointer_to_function_must_be_used"></span><span id="POINTER_TO_FUNCTION_MUST_BE_USED"></span>pointer to function must be used</dt> <dd> Although function-type definitions are allowed in <a href="-c-ext.md"><strong>/c_ext</strong></a> mode, they can only be used as pointers to functions. They can never be transmitted as a parameter or a return value of a remote procedure.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2290"></span><span id="midl2290"></span><dl> <dt><strong>MIDL2290</strong></dt> </dl></td>
<td><dl> <dt><span id="functions_may_not_be_passed_in_an_RPC_operation"></span><span id="functions_may_not_be_passed_in_an_rpc_operation"></span><span id="FUNCTIONS_MAY_NOT_BE_PASSED_IN_AN_RPC_OPERATION"></span>functions may not be passed in an RPC operation</dt> <dd> Functions and function pointers cannot be passed as parameters or return values of remote procedures.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2291"></span><span id="midl2291"></span><dl> <dt><strong>MIDL2291</strong></dt> </dl></td>
<td><dl> <dt><span id="hyper_double_not_supported_as_return_value_for__Oi_modes__using__Os"></span><span id="hyper_double_not_supported_as_return_value_for__oi_modes__using__os"></span><span id="HYPER_DOUBLE_NOT_SUPPORTED_AS_RETURN_VALUE_FOR__OI_MODES__USING__OS"></span>hyper/double not supported as return value for /Oi modes, using /Os</dt> <dd> Hyper and double return values can be handled only by <a href="-os.md"><strong>/Os</strong></a> optimization stubs. The stubs for this routine will be generated using <strong>/Os</strong> optimization.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2292"></span><span id="midl2292"></span><dl> <dt><strong>MIDL2292</strong></dt> </dl></td>
<td><dl> <dt><span id="_pragma_pack_pop__without_matching__pragma_pack_push_"></span><span id="_PRAGMA_PACK_POP__WITHOUT_MATCHING__PRAGMA_PACK_PUSH_"></span>#pragma pack(pop) without matching #pragma pack(push)</dt> <dd> #pragma pack(push) and #pragma pack(pop) must appear in matching pairs. At least one too many #pragma pack(push)s were specified.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2293"></span><span id="midl2293"></span><dl> <dt><strong>MIDL2293</strong></dt> </dl></td>
<td><dl> <dt><span id="stringable_structure_fields_must_be_byte_char_wchar_t"></span><span id="STRINGABLE_STRUCTURE_FIELDS_MUST_BE_BYTE_CHAR_WCHAR_T"></span>stringable structure fields must be byte/char/wchar_t</dt> <dd> The type [<a href="string.md"><strong>string</strong></a>] can only be applied to a structure whose fields are all of type byte, or a type definition equivalent to byte.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2294"></span><span id="midl2294"></span><dl> <dt><strong>MIDL2294</strong></dt> </dl></td>
<td><dl> <dt><span id="_notify__not_supported_for__Oi_modes__using__Os"></span><span id="_notify__not_supported_for__oi_modes__using__os"></span><span id="_NOTIFY__NOT_SUPPORTED_FOR__OI_MODES__USING__OS"></span>[notify] not supported for /Oi modes, using /Os</dt> <dd> The [<a href="notify.md"><strong>notify</strong></a>] attribute can be processed only by <a href="-os.md"><strong>/Os</strong></a> optimization stubs.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2295"></span><span id="midl2295"></span><dl> <dt><strong>MIDL2295</strong></dt> </dl></td>
<td><dl> <dt><span id="_handle_parameter_or_return_type_is_not_supported_on_a_procedure_in_an__object__interface"></span><span id="_HANDLE_PARAMETER_OR_RETURN_TYPE_IS_NOT_SUPPORTED_ON_A_PROCEDURE_IN_AN__OBJECT__INTERFACE"></span> handle parameter or return type is not supported on a procedure in an [object] interface</dt> <dd> Handles cannot be used with [ <a href="object.md"><strong>object</strong></a>] interfaces.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2296"></span><span id="midl2296"></span><dl> <dt><strong>MIDL2296</strong></dt> </dl></td>
<td><dl> <dt><span id="ANSI_C_only_allows_the_leftmost_array_bound_to_be_unspecified"></span><span id="ansi_c_only_allows_the_leftmost_array_bound_to_be_unspecified"></span><span id="ANSI_C_ONLY_ALLOWS_THE_LEFTMOST_ARRAY_BOUND_TO_BE_UNSPECIFIED"></span>ANSI C only allows the leftmost array bound to be unspecified</dt> <dd> In a conformant array, ANSI C allows only the leftmost (most significant) array bound to be unspecified. If multiple dimensions are conformant, MIDL will attempt to put a &quot;1&quot; in the other conformant dimensions. If the other dimensions are defined in a different type definition, this cannot be possible. Try putting all the array dimensions on the array declaration to avoid this. In any case, beware of the array-indexing calculations done by the compiler; you may need to do your own calculations using the actual sizes.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2297"></span><span id="midl2297"></span><dl> <dt><strong>MIDL2297</strong></dt> </dl></td>
<td><dl> <dt><span id="by-value_union_parameters_not_supported_for__Oi_modes__using__Os"></span><span id="by-value_union_parameters_not_supported_for__oi_modes__using__os"></span><span id="BY-VALUE_UNION_PARAMETERS_NOT_SUPPORTED_FOR__OI_MODES__USING__OS"></span>by-value union parameters not supported for /Oi modes, using /Os</dt> <dd> This action is not supported for fully-interpreted optimization. Switching to mixed-mode optimization.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2298"></span><span id="midl2298"></span><dl> <dt><strong>MIDL2298</strong></dt> </dl></td>
<td><dl> <dt><span id="_version__attribute_is_ignored_on_an__object__interface"></span><span id="_VERSION__ATTRIBUTE_IS_IGNORED_ON_AN__OBJECT__INTERFACE"></span>[version] attribute is ignored on an [object] interface</dt> <dd> The [<a href="object.md"><strong>object</strong></a>] attribute identifies a COM interface. An interface attribute list for a COM interface cannot include the [ <a href="version.md"><strong>version</strong></a>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2299"></span><span id="midl2299"></span><dl> <dt><strong>MIDL2299</strong></dt> </dl></td>
<td><dl> <dt><span id="_size_is__or__max_is__attribute_is_invalid_on_a_fixed_array"></span><span id="_SIZE_IS__OR__MAX_IS__ATTRIBUTE_IS_INVALID_ON_A_FIXED_ARRAY"></span>[size_is] or [max_is] attribute is invalid on a fixed array</dt> <dd> Arrays of fixed size can't use the <a href="size-is.md"><strong>size_is</strong></a> or <a href="max-is.md"><strong>max_is</strong></a> attributes.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2300"></span><span id="midl2300"></span><dl> <dt><strong>MIDL2300</strong></dt> </dl></td>
<td><dl> <dt><span id="_encode__or__decode__are_invalid_in_an__object__interface"></span><span id="_ENCODE__OR__DECODE__ARE_INVALID_IN_AN__OBJECT__INTERFACE"></span>[encode] or [decode] are invalid in an [object] interface</dt> <dd> The [<a href="object.md"><strong>object</strong></a>] attribute identifies a COM interface. The [<a href="encode.md"><strong>encode</strong></a>] and [ <a href="decode.md"><strong>decode</strong></a>] attributes enable serialization. That is, you can provide and control buffers for data marshal and unmarshal, however, you cannot perform serialization on COM interfaces.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2301"></span><span id="midl2301"></span><dl> <dt><strong>MIDL2301</strong></dt> </dl></td>
<td><dl> <dt><span id="_encode__or__decode__on_a_type_requires__ms_ext"></span><span id="_ENCODE__OR__DECODE__ON_A_TYPE_REQUIRES__MS_EXT"></span>[encode] or [decode] on a type requires /ms_ext</dt> <dd> Serialization is not part of the DCE-IDL specification. It is a Microsoft extension that requires the use of the <a href="-ms-ext.md"><strong>/ms_ext</strong></a> command-line switch.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2302"></span><span id="midl2302"></span><dl> <dt><strong>MIDL2302</strong></dt> </dl></td>
<td><dl> <dt><span id="int_not_supported_on__env_win16_or__env_dos"></span><span id="INT_NOT_SUPPORTED_ON__ENV_WIN16_OR__ENV_DOS"></span>int not supported on /env win16 or /env dos</dt> <dd> The 16-bit Microsoft platforms do not support the use of the <a href="int.md"><strong>int</strong></a> type in an IDL file. Qualify the <strong>int</strong> type with <a href="small.md"><strong>small</strong></a>, <a href="short.md"><strong>short</strong></a>, or <a href="long.md"><strong>long</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2303"></span><span id="midl2303"></span><dl> <dt><strong>MIDL2303</strong></dt> </dl></td>
<td><dl> <dt><span id="_bstring__may_only_be_applied_to_a_pointer_to__char__or__whchar_t_"></span><span id="_BSTRING__MAY_ONLY_BE_APPLIED_TO_A_POINTER_TO__CHAR__OR__WHCHAR_T_"></span>[bstring] may only be applied to a pointer to &quot;char&quot; or &quot;whchar_t&quot;</dt> <dd> This error is obsolete. It is provided only for backward compatibility.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2304"></span><span id="midl2304"></span><dl> <dt><strong>MIDL2304</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_invalid_on_a_procedure_in_an__object__interface"></span><span id="ATTRIBUTE_INVALID_ON_A_PROCEDURE_IN_AN__OBJECT__INTERFACE"></span>attribute invalid on a procedure in an [object] interface</dt> <dd> The specified attribute is not allowed on procedure in a COM interface.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2305"></span><span id="midl2305"></span><dl> <dt><strong>MIDL2305</strong></dt> </dl></td>
<td><dl> <dt><span id="attribute_invalid_on_an__object__interface"></span><span id="ATTRIBUTE_INVALID_ON_AN__OBJECT__INTERFACE"></span>attribute invalid on an [object] interface</dt> <dd> The specified attribute is not allowed in a COM interface.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2306"></span><span id="midl2306"></span><dl> <dt><strong>MIDL2306</strong></dt> </dl></td>
<td><dl> <dt><span id="too_many_parameters_or_stack_too_big_for__Oi_modes__using__Os"></span><span id="too_many_parameters_or_stack_too_big_for__oi_modes__using__os"></span><span id="TOO_MANY_PARAMETERS_OR_STACK_TOO_BIG_FOR__OI_MODES__USING__OS"></span>too many parameters or stack too big for /Oi modes, using /Os</dt> <dd> This warning is obsolete. It is provided only for backward compatibility. It indicates that the call to the remote procedure causes the stack to grow larger than 64 K.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2307"></span><span id="midl2307"></span><dl> <dt><strong>MIDL2307</strong></dt> </dl></td>
<td><dl> <dt><span id="no_attributes_on_ACF_file_typedef__so_no_effect"></span><span id="no_attributes_on_acf_file_typedef__so_no_effect"></span><span id="NO_ATTRIBUTES_ON_ACF_FILE_TYPEDEF__SO_NO_EFFECT"></span>no attributes on ACF file typedef, so no effect</dt> <dd> IDL file should contain all of the typedef statements that do not have attributes. They should not occur in ACF files. If they do, the MIDL compiler interprets them as redundant and ignores them.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2308"></span><span id="midl2308"></span><dl> <dt><strong>MIDL2308</strong></dt> </dl></td>
<td><dl> <dt><span id="calling_conventions_other_than___stdcall_or___cdecl_not_supported_for__Oi_modes__using__Os"></span><span id="calling_conventions_other_than___stdcall_or___cdecl_not_supported_for__oi_modes__using__os"></span><span id="CALLING_CONVENTIONS_OTHER_THAN___STDCALL_OR___CDECL_NOT_SUPPORTED_FOR__OI_MODES__USING__OS"></span>calling conventions other than __stdcall or __cdecl not supported for /Oi modes, using /Os</dt> <dd> Calling conventions such as <strong>__pascal</strong> or <strong>__fastcall</strong> change the format of the stack. The <a href="-oi.md"><strong>/Oi</strong></a> modes only support the <strong>__stdcall</strong> and <strong>__cdecl</strong> calling conventions. If you must use other calling conventions, use the <a href="-os.md"><strong>/Os</strong></a> mode.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2309"></span><span id="midl2309"></span><dl> <dt><strong>MIDL2309</strong></dt> </dl></td>
<td><dl> <dt><span id="Too_many_delegation_methods_in_the_interface__require_Windows_2000_or_greater"></span><span id="too_many_delegation_methods_in_the_interface__require_windows_2000_or_greater"></span><span id="TOO_MANY_DELEGATION_METHODS_IN_THE_INTERFACE__REQUIRE_WINDOWS_2000_OR_GREATER"></span>Too many delegation methods in the interface, require Windows 2000 or greater</dt> <dd> One interface can inherit from another. When it does, the methods of the base interface are considered delegated. No derived interface can contain more than 256 delegated methods.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2310"></span><span id="midl2310"></span><dl> <dt><strong>MIDL2310</strong></dt> </dl></td>
<td><dl> <dt><span id="auto_handles_not_supported_with__env_mac_or__env_powermac"></span><span id="AUTO_HANDLES_NOT_SUPPORTED_WITH__ENV_MAC_OR__ENV_POWERMAC"></span>auto handles not supported with /env mac or /env powermac</dt> <dd> When compiling your IDL file for a PowerMac, you cannot use automatic binding handles. You must specify explicit or implicit handles.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2311"></span><span id="midl2311"></span><dl> <dt><strong>MIDL2311</strong></dt> </dl></td>
<td><dl> <dt><span id="statements_outside_library_block_are_illegal_in_mktyplib_compatibility_mode"></span><span id="STATEMENTS_OUTSIDE_LIBRARY_BLOCK_ARE_ILLEGAL_IN_MKTYPLIB_COMPATIBILITY_MODE"></span>statements outside library block are illegal in mktyplib compatibility mode</dt> <dd> You may need to specify the <a href="-mktyplib203.md"><strong>/mktyplib203</strong></a> command-line switch when you compile your IDL file.<br/>
<blockquote>
[!Note]<br />
The Mktyplib.exe tool is obsolete. Use the MIDL compiler instead.
</blockquote>
<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2312"></span><span id="midl2312"></span><dl> <dt><strong>MIDL2312</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_syntax_unless_using_mktyplib_compatibility_mode"></span><span id="ILLEGAL_SYNTAX_UNLESS_USING_MKTYPLIB_COMPATIBILITY_MODE"></span>illegal syntax unless using mktyplib compatibility mode</dt> <dd> You may need to specify the <a href="-mktyplib203.md"><strong>/mktyplib203</strong></a> command-line switch when you compile your IDL file.<br/>
<blockquote>
[!Note]<br />
The Mktyplib.exe tool is obsolete. Use the MIDL compiler instead.
</blockquote>
<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2313"></span><span id="midl2313"></span><dl> <dt><strong>MIDL2313</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_definition__must_use_typedef_in_mktyplib_compatibility_mode"></span><span id="ILLEGAL_DEFINITION__MUST_USE_TYPEDEF_IN_MKTYPLIB_COMPATIBILITY_MODE"></span>illegal definition, must use typedef in mktyplib compatibility mode</dt> <dd> You may need to specify the <a href="-mktyplib203.md"><strong>/mktyplib203</strong></a> command-line switch when you compile your IDL file.<br/>
<blockquote>
[!Note]<br />
The Mktyplib.exe tool is obsolete. Use the MIDL compiler instead.
</blockquote>
<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2314"></span><span id="midl2314"></span><dl> <dt><strong>MIDL2314</strong></dt> </dl></td>
<td><dl> <dt><span id="explicit_pointer_attribute__ptr___ref__ignored_for_interface_pointers"></span><span id="EXPLICIT_POINTER_ATTRIBUTE__PTR___REF__IGNORED_FOR_INTERFACE_POINTERS"></span>explicit pointer attribute [ptr] [ref] ignored for interface pointers</dt> <dd> Pointers to interfaces cannot have IDL attributes.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2315"></span><span id="midl2315"></span><dl> <dt><strong>MIDL2315</strong></dt> </dl></td>
<td><a href="-oi.md"><strong>/Oi</strong></a> modes not implemented for PowerMac, switching to <a href="-os.md"><strong>/Os</strong></a><br/></td>
</tr>
<tr class="odd">
<td><span id="MIDL2316"></span><span id="midl2316"></span><dl> <dt><strong>MIDL2316</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_expression_type_used_in_attribute"></span><span id="ILLEGAL_EXPRESSION_TYPE_USED_IN_ATTRIBUTE"></span>illegal expression type used in attribute</dt> <dd> The default value for the pointer should be a constant.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2317"></span><span id="midl2317"></span><dl> <dt><strong>MIDL2317</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_type_used_in_pipe"></span><span id="ILLEGAL_TYPE_USED_IN_PIPE"></span>illegal type used in pipe</dt> <dd> Pipes are limited to basic IDL data types. For example, you cannot specify a pipe of arrays.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2318"></span><span id="midl2318"></span><dl> <dt><strong>MIDL2318</strong></dt> </dl></td>
<td><dl> <dt><span id="procedure_uses_pipes__using__Oicf"></span><span id="procedure_uses_pipes__using__oicf"></span><span id="PROCEDURE_USES_PIPES__USING__OICF"></span>procedure uses pipes, using /Oicf</dt> <dd> The mode you selected does not support pipes. The MIDL compiler detected the use of one or more pipes in your interface. Therefore, it is compiling your IDL file in <a href="-oi.md"><strong>/Oicf</strong></a> mode.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2319"></span><span id="midl2319"></span><dl> <dt><strong>MIDL2319</strong></dt> </dl></td>
<td><dl> <dt><span id="procedure_has_an_attribute_that_requires_use_of__Oif__switching_modes"></span><span id="procedure_has_an_attribute_that_requires_use_of__oif__switching_modes"></span><span id="PROCEDURE_HAS_AN_ATTRIBUTE_THAT_REQUIRES_USE_OF__OIF__SWITCHING_MODES"></span>procedure has an attribute that requires use of /Oif, switching modes</dt> <dd> You must compile [<a href="async.md"><strong>async</strong></a>] procedures in <a href="-oi.md"><strong>/Oif</strong></a> mode.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2320"></span><span id="midl2320"></span><dl> <dt><strong>MIDL2320</strong></dt> </dl></td>
<td><dl> <dt><span id="conflicting_optimization_requirements__cannot_optimize"></span><span id="CONFLICTING_OPTIMIZATION_REQUIREMENTS__CANNOT_OPTIMIZE"></span>conflicting optimization requirements, cannot optimize</dt> <dd> This error often indicates that you specified both <a href="-os.md"><strong>/Os</strong></a> and <a href="-oi.md"><strong>/Oi</strong></a> (or a variant of <strong>/Oi</strong>) MIDL compiler modes. It can also mean that the features you specified in your IDL and ACL files require the use of both modes. You must select one mode or the other to optimize.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2321"></span><span id="midl2321"></span><dl> <dt><strong>MIDL2321</strong></dt> </dl></td>
<td><dl> <dt><span id="pipes_cannot_be_array_elements__or_members_of_structures_or_unions"></span><span id="PIPES_CANNOT_BE_ARRAY_ELEMENTS__OR_MEMBERS_OF_STRUCTURES_OR_UNIONS"></span>pipes cannot be array elements, or members of structures or unions</dt> <dd> Pipe data types can only be top-level parameters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2322"></span><span id="midl2322"></span><dl> <dt><strong>MIDL2322</strong></dt> </dl></td>
<td><dl> <dt><span id="invalid_pipe_usage"></span><span id="INVALID_PIPE_USAGE"></span>invalid pipe usage</dt> <dd> You cannot use pipes with the [<a href="transmit-as.md"><strong>transmit_as</strong></a>], [<a href="represent-as.md"><strong>represent_as</strong></a>], or [<a href="user-marshal.md"><strong>user_marshal</strong></a>] attributes. In addition, pipes cannot be used as return types.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2323"></span><span id="midl2323"></span><dl> <dt><strong>MIDL2323</strong></dt> </dl></td>
<td><dl> <dt><span id="feature_requires_the_advanced_interpreted_optimization_option__use_-Oicf"></span><span id="feature_requires_the_advanced_interpreted_optimization_option__use_-oicf"></span><span id="FEATURE_REQUIRES_THE_ADVANCED_INTERPRETED_OPTIMIZATION_OPTION__USE_-OICF"></span>feature requires the advanced interpreted optimization option; use -Oicf</dt> <dd> This error indicates that MIDL compiler command-line switches such as <a href="-robust.md"><strong>/robust</strong></a> require the use of <a href="-oi.md"><strong>/Oicf</strong></a> mode.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2324"></span><span id="midl2324"></span><dl> <dt><strong>MIDL2324</strong></dt> </dl></td>
<td><dl> <dt><span id="feature_requires_the_advanced_interpreted_optimization_option__use_-Oicf"></span><span id="feature_requires_the_advanced_interpreted_optimization_option__use_-oicf"></span><span id="FEATURE_REQUIRES_THE_ADVANCED_INTERPRETED_OPTIMIZATION_OPTION__USE_-OICF"></span>feature requires the advanced interpreted optimization option; use -Oicf</dt> <dd> This warning indicates that MIDL compiler command-line switches such as <a href="-robust.md"><strong>/robust</strong></a> require the use of <a href="-oi.md"><strong>/Oicf</strong></a> mode.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2329"></span><span id="midl2329"></span><dl> <dt><strong>MIDL2329</strong></dt> </dl></td>
<td><dl> <dt><span id="the_optimization_option_is_being_phased_out__use_-Oic"></span><span id="the_optimization_option_is_being_phased_out__use_-oic"></span><span id="THE_OPTIMIZATION_OPTION_IS_BEING_PHASED_OUT__USE_-OIC"></span>the optimization option is being phased out, use -Oic</dt> <dd> The <a href="-oi.md"><strong>/Oi1</strong></a> optimization mode was specified on the MIDL command line. This mode is no longer supported and <strong>/Oicf</strong> should be used instead.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2330"></span><span id="midl2330"></span><dl> <dt><strong>MIDL2330</strong></dt> </dl></td>
<td><dl> <dt><span id="the_optimization_option_is_being_phased_out__use_-Oicf"></span><span id="the_optimization_option_is_being_phased_out__use_-oicf"></span><span id="THE_OPTIMIZATION_OPTION_IS_BEING_PHASED_OUT__USE_-OICF"></span>the optimization option is being phased out, use -Oicf</dt> <dd> The <a href="-oi.md"><strong>/Oi2</strong></a> optimization mode was specified on the MIDL command line. This mode is no longer supported and <strong>/Oicf</strong> should be used instead.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2331"></span><span id="midl2331"></span><dl> <dt><strong>MIDL2331</strong></dt> </dl></td>
<td><dl> <dt><span id="the_optimization_option_is_being_phased_out__use_-ic"></span><span id="THE_OPTIMIZATION_OPTION_IS_BEING_PHASED_OUT__USE_-IC"></span>the optimization option is being phased out, use -ic</dt> <dd> The i1 optimization mode was specified in an [optimize] ACF attribute. This mode is no longer supported and icf should be used instead.<br/> Example ACF file:<br/>
<pre class="syntax" data-space="preserve"><code>[optimize(&quot;i1&quot;)] roo();    //MIDL 2331</code></pre>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2332"></span><span id="midl2332"></span><dl> <dt><strong>MIDL2332</strong></dt> </dl></td>
<td><dl> <dt><span id="the_optimization_option_is_being_phased_out__use_-icf"></span><span id="THE_OPTIMIZATION_OPTION_IS_BEING_PHASED_OUT__USE_-ICF"></span>the optimization option is being phased out, use -icf</dt> <dd> The i2 optimization mode was specified in an [optimize] ACF attribute. This mode is no longer supported and icf should be used instead.<br/> Example ACF file:<br/>
<pre class="syntax" data-space="preserve"><code>[optimize(&quot;i2&quot;)] roo();    //MIDL 2332</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2333"></span><span id="midl2333"></span><dl> <dt><strong>MIDL2333</strong></dt> </dl></td>
<td><dl> <dt><span id="the_-old_and_-new_switches_are_obsolete__use_-oldtlb_and_-newtlb"></span><span id="THE_-OLD_AND_-NEW_SWITCHES_ARE_OBSOLETE__USE_-OLDTLB_AND_-NEWTLB"></span>the -old and -new switches are obsolete, use -oldtlb and -newtlb</dt> <dd> This message is obsolete and is no longer omitted by MIDL.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2334"></span><span id="midl2334"></span><dl> <dt><strong>MIDL2334</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_argument_value"></span><span id="ILLEGAL_ARGUMENT_VALUE"></span>illegal argument value</dt> <dd> The allowed variants of the /O command-line switch include <a href="-os.md"><strong>/Os</strong></a>, <a href="-oi.md"><strong>/Oi</strong></a>, <strong>/Oic</strong>, <strong>/Oicf</strong>, and <strong>/Oif</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2335"></span><span id="midl2335"></span><dl> <dt><strong>MIDL2335</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_expression_type_in_constant"></span><span id="ILLEGAL_EXPRESSION_TYPE_IN_CONSTANT"></span>illegal expression type in constant</dt> <dd> The expression does not evaluate to a constant.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2336"></span><span id="midl2336"></span><dl> <dt><strong>MIDL2336</strong></dt> </dl></td>
<td><dl> <dt><span id="illegal_expression_type_in_enum"></span><span id="ILLEGAL_EXPRESSION_TYPE_IN_ENUM"></span>illegal expression type in enum</dt> <dd> An enumerated value in an <a href="enum.md"><strong>enum</strong></a> definition does not evaluate to an integral type.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2337"></span><span id="midl2337"></span><dl> <dt><strong>MIDL2337</strong></dt> </dl></td>
<td><dl> <dt><span id="unsatisfied_forward_declaration"></span><span id="UNSATISFIED_FORWARD_DECLARATION"></span>unsatisfied forward declaration</dt> <dd> The MIDL compiler could not resolve the definition of a forward declaration.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2338"></span><span id="midl2338"></span><dl> <dt><strong>MIDL2338</strong></dt> </dl></td>
<td><dl> <dt><span id="switches_are_contradictory"></span><span id="SWITCHES_ARE_CONTRADICTORY"></span>switches are contradictory</dt> <dd> You cannot use both the <a href="-osf.md"><strong>/osf</strong></a> and <a href="-ms-ext.md"><strong>/ms_ext</strong></a> command-line switches when you compile an IDL file. You must choose one or the other.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2339"></span><span id="midl2339"></span><dl> <dt><strong>MIDL2339</strong></dt> </dl></td>
<td><dl> <dt><span id="MIDL_cannot_generate_HOOKOLE_information_for_the_non-rpc-able_union"></span><span id="midl_cannot_generate_hookole_information_for_the_non-rpc-able_union"></span><span id="MIDL_CANNOT_GENERATE_HOOKOLE_INFORMATION_FOR_THE_NON-RPC-ABLE_UNION"></span>MIDL cannot generate HOOKOLE information for the non-rpc-able union</dt> <dd> This error is obsolete. It is provided strictly for backward compatibility.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2340"></span><span id="midl2340"></span><dl> <dt><strong>MIDL2340</strong></dt> </dl></td>
<td><dl> <dt><span id="no_case_expression_found_for_union"></span><span id="NO_CASE_EXPRESSION_FOUND_FOR_UNION"></span>no case expression found for union</dt> <dd> Each field of a union must have a case statement with a constant expression.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2341"></span><span id="midl2341"></span><dl> <dt><strong>MIDL2341</strong></dt> </dl></td>
<td><dl> <dt><span id="_user_marshal__and__wire_marshal__not_supported_with_-Oi_and_-Oic_flags__use_-Os_or_-Oicf"></span><span id="_user_marshal__and__wire_marshal__not_supported_with_-oi_and_-oic_flags__use_-os_or_-oicf"></span><span id="_USER_MARSHAL__AND__WIRE_MARSHAL__NOT_SUPPORTED_WITH_-OI_AND_-OIC_FLAGS__USE_-OS_OR_-OICF"></span>[user_marshal] and [wire_marshal] not supported with -Oi and -Oic flags, use -Os or -Oicf</dt> <dd> The [<a href="user-marshal.md"><strong>user_marshal</strong></a>] and [<a href="wire-marshal.md"><strong>wire_marshal</strong></a>] attributes require the specific optimization features available only in <a href="-oi.md"><strong>/Oicf</strong></a> (codeless proxy with fast format strings) or <a href="-os.md"><strong>/Os</strong></a> (mixed mode marshaling).<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2342"></span><span id="midl2342"></span><dl> <dt><strong>MIDL2342</strong></dt> </dl></td>
<td><dl> <dt><span id="pipes_can_t_be_used_with_data_serialization__i.e.__encode__and_or__decode_"></span><span id="PIPES_CAN_T_BE_USED_WITH_DATA_SERIALIZATION__I.E.__ENCODE__AND_OR__DECODE_"></span>pipes can't be used with data serialization, i.e. [encode] and/or [decode]</dt> <dd> You cannot pass pipes as parameters to procedures that have the [<a href="encode.md"><strong>encode</strong></a>] or [<a href="decode.md"><strong>decode</strong></a>] attributes.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2343"></span><span id="midl2343"></span><dl> <dt><strong>MIDL2343</strong></dt> </dl></td>
<td><dl> <dt><span id="all_pipe_interface_pointers_must_use_single_indirection"></span><span id="ALL_PIPE_INTERFACE_POINTERS_MUST_USE_SINGLE_INDIRECTION"></span>all pipe interface pointers must use single indirection</dt> <dd> You cannot use a pointer to a pointer to a pipe interface in this manner.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2344"></span><span id="midl2344"></span><dl> <dt><strong>MIDL2344</strong></dt> </dl></td>
<td><dl> <dt><span id="_iid_is____cannot_be_used_with_a_pipe_interface_pointer"></span><span id="_IID_IS____CANNOT_BE_USED_WITH_A_PIPE_INTERFACE_POINTER"></span>[iid_is()] cannot be used with a pipe interface pointer</dt> <dd> This message is obsolete. This message is no longer used by the compiler.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2345"></span><span id="midl2345"></span><dl> <dt><strong>MIDL2345</strong></dt> </dl></td>
<td><dl> <dt><span id="invalid_or_inapplicable_-lcid_switch"></span><span id="INVALID_OR_INAPPLICABLE_-LCID_SWITCH"></span>invalid or inapplicable -lcid switch</dt> <dd> The local identifier (LCID) that you specified is not valid.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2346"></span><span id="midl2346"></span><dl> <dt><strong>MIDL2346</strong></dt> </dl></td>
<td><dl> <dt><span id="the_specified_lcid_is_different_from_previous_specification"></span><span id="THE_SPECIFIED_LCID_IS_DIFFERENT_FROM_PREVIOUS_SPECIFICATION"></span>the specified lcid is different from previous specification</dt> <dd> The values specified in /lcid and [<a href="lcid.md"><strong>lcid</strong></a>] are different. The MIDL compiler will use the last one defined.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2347"></span><span id="midl2347"></span><dl> <dt><strong>MIDL2347</strong></dt> </dl></td>
<td><dl> <dt><span id="importlib_is_not_allowed_outside_of_a_library_block"></span><span id="IMPORTLIB_IS_NOT_ALLOWED_OUTSIDE_OF_A_LIBRARY_BLOCK"></span>importlib is not allowed outside of a library block</dt> <dd> All [<a href="importlib.md"><strong>importlib</strong></a>] statements should occur in a [<a href="library.md"><strong>library</strong></a>] block.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2348"></span><span id="midl2348"></span><dl> <dt><strong>MIDL2348</strong></dt> </dl></td>
<td><dl> <dt><span id="invalid_floating_point_value"></span><span id="INVALID_FLOATING_POINT_VALUE"></span>invalid floating point value</dt> <dd> This error should not be emitted by MIDL. If you see this error please report a bug to Microsoft providing all files needed to reproduce the error, including your IDL files, ACF files, headers, etc.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2349"></span><span id="midl2349"></span><dl> <dt><strong>MIDL2349</strong></dt> </dl></td>
<td><dl> <dt><span id="invalid_member"></span><span id="INVALID_MEMBER"></span>invalid member</dt> <dd> Procedures cannot be members of a library.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2350"></span><span id="midl2350"></span><dl> <dt><strong>MIDL2350</strong></dt> </dl></td>
<td><dl> <dt><span id="possible_invalid_member"></span><span id="POSSIBLE_INVALID_MEMBER"></span>possible invalid member</dt> <dd> To be a valid member of a library, the library element must be a module, a dispinterface, a coclass, an if statement, a structure, a union, an enumeration, or a forward declaration.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2351"></span><span id="midl2351"></span><dl> <dt><strong>MIDL2351</strong></dt> </dl></td>
<td><dl> <dt><span id="mismatch_in_pipe_and_interface_types"></span><span id="MISMATCH_IN_PIPE_AND_INTERFACE_TYPES"></span>mismatch in pipe and interface types</dt> <dd> This message is obsolete.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2352"></span><span id="midl2352"></span><dl> <dt><strong>MIDL2352</strong></dt> </dl></td>
<td><dl> <dt><span id="string__varying_array__conformant_array_and_full_pointer_parameters_may_be_incompatible_with_pipe_parameters_during_run_time"></span><span id="STRING__VARYING_ARRAY__CONFORMANT_ARRAY_AND_FULL_POINTER_PARAMETERS_MAY_BE_INCOMPATIBLE_WITH_PIPE_PARAMETERS_DURING_RUN_TIME"></span>string, varying array, conformant array and full pointer parameters may be incompatible with pipe parameters during run time</dt> <dd> A method combining one or more [in] strings, varying arrays, conformant arrays and full pointer parameters and any [in] pipe parameter result in generation of a stub that runs only on <strong>ncacn_*</strong> and <a href="ncalrpc.md"><strong>ncalrpc</strong></a> protocol sequences on Windows computers. Using the stub to make calls on <strong>ncadg_*</strong> protocol sequences or accepting calls from other OSF DCE RPC vendors may generate faults on the server during run time. This error occurs starting with Windows Server 2003.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2353"></span><span id="midl2353"></span><dl> <dt><strong>MIDL2353</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_must_be_in"></span><span id="PARAMETER_MUST_BE_IN"></span>parameter must be in</dt> <dd> Asynchronous handles must be [<a href="in.md"><strong>in</strong></a>] parameters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2354"></span><span id="midl2354"></span><dl> <dt><strong>MIDL2354</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_type_of_an__async__object_must_be_a_double_pointer_to_an_interface"></span><span id="PARAMETER_TYPE_OF_AN__ASYNC__OBJECT_MUST_BE_A_DOUBLE_POINTER_TO_AN_INTERFACE"></span>parameter type of an [async] object must be a double pointer to an interface</dt> <dd> The parameter must be of type <strong>IAsyncManager</strong> **.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2355"></span><span id="midl2355"></span><dl> <dt><strong>MIDL2355</strong></dt> </dl></td>
<td><dl> <dt><span id="incorrect_async_handle_type"></span><span id="INCORRECT_ASYNC_HANDLE_TYPE"></span>incorrect async handle type</dt> <dd> The handle type should be <strong>IAsyncManager</strong> or a type derived from <strong>IAsyncManager</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2356"></span><span id="midl2356"></span><dl> <dt><strong>MIDL2356</strong></dt> </dl></td>
<td><dl> <dt><span id="the__internal__switch_enables_unsupported_features__use_with_caution"></span><span id="THE__INTERNAL__SWITCH_ENABLES_UNSUPPORTED_FEATURES__USE_WITH_CAUTION"></span>the &quot;internal&quot; switch enables unsupported features, use with caution</dt> <dd> Avoid using this switch.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2357"></span><span id="midl2357"></span><dl> <dt><strong>MIDL2357</strong></dt> </dl></td>
<td><dl> <dt><span id="async_procedures_cannot_use_auto_handle"></span><span id="ASYNC_PROCEDURES_CANNOT_USE_AUTO_HANDLE"></span>async procedures cannot use auto handle</dt> <dd> Procedures with the [<a href="async.md"><strong>async</strong></a>] attribute require explicit handles.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2358"></span><span id="midl2358"></span><dl> <dt><strong>MIDL2358</strong></dt> </dl></td>
<td><dl> <dt><span id="error_status_t_should_have_both__comm_status__and__fault_status_"></span><span id="ERROR_STATUS_T_SHOULD_HAVE_BOTH__COMM_STATUS__AND__FAULT_STATUS_"></span>error_status_t should have both [comm_status] and [fault_status]</dt> <dd> A procedure was specified with the IDL attributes [maybe] or [message] but the return type only has the ACF attributes [comm_status] or [fault_status]. Both ACF attributes are required.<br/> Example ACF file:<br/>
<pre class="syntax" data-space="preserve"><code>[comm_status] roo();    //MIDL 2358
[fault_status] bar();    //MIDL 2358
[comm_status, fault_status] baz();    //OK</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2359"></span><span id="midl2359"></span><dl> <dt><strong>MIDL2359</strong></dt> </dl></td>
<td><dl> <dt><span id="this_construct_is_only_allowed_within_a_library_block"></span><span id="THIS_CONSTRUCT_IS_ONLY_ALLOWED_WITHIN_A_LIBRARY_BLOCK"></span>this construct is only allowed within a library block</dt> <dd> A module can occur only within a library block.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2360"></span><span id="midl2360"></span><dl> <dt><strong>MIDL2360</strong></dt> </dl></td>
<td><dl> <dt><span id="invalid_type_redefinition"></span><span id="INVALID_TYPE_REDEFINITION"></span>invalid type redefinition</dt> <dd> A new type was recursively defined on a nonexisting type.<br/> Example:<br/>
<pre class="syntax" data-space="preserve"><code>typedef roo roo[10];    //MIDL 2360</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2361"></span><span id="midl2361"></span><dl> <dt><strong>MIDL2361</strong></dt> </dl></td>
<td><dl> <dt><span id="procedures_with_a__vararg__attribute_must_have_a_SAFEARRAY_VARIANT__parameter__param_order_is__vararg____lcid____retval_"></span><span id="procedures_with_a__vararg__attribute_must_have_a_safearray_variant__parameter__param_order_is__vararg____lcid____retval_"></span><span id="PROCEDURES_WITH_A__VARARG__ATTRIBUTE_MUST_HAVE_A_SAFEARRAY_VARIANT__PARAMETER__PARAM_ORDER_IS__VARARG____LCID____RETVAL_"></span>procedures with a [vararg] attribute must have a SAFEARRAY(VARIANT) parameter; param order is [vararg], [lcid], [retval]</dt> <dd> Most of the parameters for procedures with the [<a href="vararg.md"><strong>vararg</strong></a>] attribute must occur before the <strong>SAFEARRAY(VARIANT)</strong> parameter. The <strong>SAFEARRAY(VARIANT)</strong> parameter must be present. If the parameter list contains a parameter with the [ <a href="lcid.md"><strong>lcid</strong></a>] attribute, it must follow the <strong>SAFEARRAY(VARIANT)</strong> parameter. If the parameter list contains a parameter with the [<a href="retval.md"><strong>retval</strong></a>] attribute, it must occur after the parameter with the [<strong>lcid</strong>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2363"></span><span id="midl2363"></span><dl> <dt><strong>MIDL2363</strong></dt> </dl></td>
<td><dl> <dt><span id="too_many_methods_in_the_interface__requires_Windows_2000_or_greater"></span><span id="too_many_methods_in_the_interface__requires_windows_2000_or_greater"></span><span id="TOO_MANY_METHODS_IN_THE_INTERFACE__REQUIRES_WINDOWS_2000_OR_GREATER"></span>too many methods in the interface, requires Windows 2000 or greater</dt> <dd> The MIDL compiler does not allow more than 1024 methods in an interface when you are compiling in <a href="-oi.md"><strong>/Oicf</strong></a> mode.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2364"></span><span id="midl2364"></span><dl> <dt><strong>MIDL2364</strong></dt> </dl></td>
<td><dl> <dt><span id="switch_is_being_phased_out"></span><span id="SWITCH_IS_BEING_PHASED_OUT"></span>switch is being phased out</dt> <dd> The following switches are obsolete: /<strong>hookole</strong>, /<strong>env win16</strong>, and /<strong>env</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2365"></span><span id="midl2365"></span><dl> <dt><strong>MIDL2365</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_derive_from_IAdviseSink__IAdviseSink2__or_IAdviseSinkEx"></span><span id="cannot_derive_from_iadvisesink__iadvisesink2__or_iadvisesinkex"></span><span id="CANNOT_DERIVE_FROM_IADVISESINK__IADVISESINK2__OR_IADVISESINKEX"></span>cannot derive from IAdviseSink, IAdviseSink2, or IAdviseSinkEx</dt> <dd> These interfaces cannot be extended.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2366"></span><span id="midl2366"></span><dl> <dt><strong>MIDL2366</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_assign_a_default_value"></span><span id="CANNOT_ASSIGN_A_DEFAULT_VALUE"></span>cannot assign a default value</dt> <dd> Assigning a default value to a parameter is allowed in Visual Basic, but not in C++. If you are using C++, the default value is ignored.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2367"></span><span id="midl2367"></span><dl> <dt><strong>MIDL2367</strong></dt> </dl></td>
<td><dl> <dt><span id="type_library_generation_for_DOS_Win16_MAC_is_not_supported"></span><span id="type_library_generation_for_dos_win16_mac_is_not_supported"></span><span id="TYPE_LIBRARY_GENERATION_FOR_DOS_WIN16_MAC_IS_NOT_SUPPORTED"></span>type library generation for DOS/Win16/MAC is not supported</dt> <dd> MIDL does not support 16-bit type libraries.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2368"></span><span id="midl2368"></span><dl> <dt><strong>MIDL2368</strong></dt> </dl></td>
<td><dl> <dt><span id="error_generating_type_library__ignored"></span><span id="ERROR_GENERATING_TYPE_LIBRARY__IGNORED"></span>error generating type library, ignored</dt> <dd> A nonfatal error occurred while generating the type library.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2369"></span><span id="midl2369"></span><dl> <dt><strong>MIDL2369</strong></dt> </dl></td>
<td><dl> <dt><span id="exceeded_stack_size_for__Oi__using__Os"></span><span id="exceeded_stack_size_for__oi__using__os"></span><span id="EXCEEDED_STACK_SIZE_FOR__OI__USING__OS"></span>exceeded stack size for /Oi, using /Os</dt> <dd> The -Oi optimization mode is limited to 128 bytes of stack space for parameters. The compiler has automatically switched to the Os optimization mode to work around this limitation.<br/> To avoid this warning, use the -Oicf or -Os optimization modes. The optimization mode may be changed on the command line by specifying -Oicf or -Os instead of -Oi or by adding an [optimize9&quot;icf&quot;)] or optimize[(&quot;s&quot;)] attribute to the function in the ACF file.<br/> This warning typically happens when passing large structures as parameters by value. The required stack size can be lowered by passing a pointer to the structure instead.<br/> Example:<br/>
<pre class="syntax" data-space="preserve"><code>typedef struct
{
char a[127];
}
large;
//This function has a stack size of 132 (x86) or 136 (alpha) on 32-bit systems
void roo(large s, int a);    //MIDL 2360
// workaround: pass by reference
void bar (large *s, int a);</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2370"></span><span id="midl2370"></span><dl> <dt><strong>MIDL2370</strong></dt> </dl></td>
<td><dl> <dt><span id="use_of__robust_requires__Oicf__switching_modes"></span><span id="use_of__robust_requires__oicf__switching_modes"></span><span id="USE_OF__ROBUST_REQUIRES__OICF__SWITCHING_MODES"></span>use of /robust requires /Oicf, switching modes</dt> <dd> You must compile in <a href="-oi.md"><strong>/Oicf</strong></a> mode when you specify the <a href="-robust.md"><strong>/robust</strong></a> switch on the command line.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2371"></span><span id="midl2371"></span><dl> <dt><strong>MIDL2371</strong></dt> </dl></td>
<td><dl> <dt><span id="incorrect_range_specified"></span><span id="INCORRECT_RANGE_SPECIFIED"></span>incorrect range specified</dt> <dd> The highest value specified in a [<a href="range.md"><strong>range</strong></a>] attribute is less than the lowest value.<br/> Example:<br/>
<pre class="syntax" data-space="preserve"><code>void roo([range(3,2)] int a);    //MIDL 2371</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2372"></span><span id="midl2372"></span><dl> <dt><strong>MIDL2372</strong></dt> </dl></td>
<td><dl> <dt><span id="_invalid_combination_of__in__only_and__out__parameters_for__async_uuid__interface"></span><span id="_INVALID_COMBINATION_OF__IN__ONLY_AND__OUT__PARAMETERS_FOR__ASYNC_UUID__INTERFACE"></span> invalid combination of [in] only and [out] parameters for [async_uuid] interface</dt> <dd> Only simple combinations of attributes with [<a href="in.md"><strong>in</strong></a>] or [<a href="out-idl.md"><strong>out</strong></a>] parameters are allowed for this type of interface.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2373"></span><span id="midl2373"></span><dl> <dt><strong>MIDL2373</strong></dt> </dl></td>
<td><dl> <dt><span id="DOS__Win16_and_MAC_platforms_are_not_supported_with__robust"></span><span id="dos__win16_and_mac_platforms_are_not_supported_with__robust"></span><span id="DOS__WIN16_AND_MAC_PLATFORMS_ARE_NOT_SUPPORTED_WITH__ROBUST"></span>DOS, Win16 and MAC platforms are not supported with /robust</dt> <dd> MIDL supports the <a href="-robust.md"><strong>/robust</strong></a> switch on Microsoft Windows 2000 or later.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2374"></span><span id="midl2374"></span><dl> <dt><strong>MIDL2374</strong></dt> </dl></td>
<td><dl> <dt><span id="support_for_NT_3.51_style_stubless_proxies_for_object_interfaces_will_be_phased_out__use__Oif."></span><span id="support_for_nt_3.51_style_stubless_proxies_for_object_interfaces_will_be_phased_out__use__oif."></span><span id="SUPPORT_FOR_NT_3.51_STYLE_STUBLESS_PROXIES_FOR_OBJECT_INTERFACES_WILL_BE_PHASED_OUT__USE__OIF."></span>support for NT 3.51 style stubless proxies for object interfaces will be phased out; use /Oif.</dt> <dd> This mode is obsolete. Use <a href="-oi.md"><strong>/Oif</strong></a> or <strong>/Oicf</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2375"></span><span id="midl2375"></span><dl> <dt><strong>MIDL2375</strong></dt> </dl></td>
<td><dl> <dt><span id="_encode__or__decode__with__robust_requires__Oicf"></span><span id="_encode__or__decode__with__robust_requires__oicf"></span><span id="_ENCODE__OR__DECODE__WITH__ROBUST_REQUIRES__OICF"></span>[encode] or [decode] with /robust requires /Oicf</dt> <dd> Serialization cannot be performed when the <a href="-robust.md"><strong>/robust</strong></a> switch is specified.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2377"></span><span id="midl2377"></span><dl> <dt><strong>MIDL2377</strong></dt> </dl></td>
<td><dl> <dt><span id="conflicting_attributes_specified"></span><span id="CONFLICTING_ATTRIBUTES_SPECIFIED"></span>conflicting attributes specified</dt> <dd> Both [<a href="context-handle-serialize.md"><strong>context_handle_serialize</strong></a>] and [<a href="context-handle-noserialize.md"><strong>context_handle_noserialize</strong></a>] were specified.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2378"></span><span id="midl2378"></span><dl> <dt><strong>MIDL2378</strong></dt> </dl></td>
<td><dl> <dt><span id="_serialize____noserialize__can_be_applied_to_context_handles"></span><span id="_SERIALIZE____NOSERIALIZE__CAN_BE_APPLIED_TO_CONTEXT_HANDLES"></span>[serialize], [noserialize] can be applied to context_handles</dt> <dd> The ACF attributes [context_handle_serialize] or [context_handle_noserialize] can only be applied to types that are context handles.<br/> Example IDL file:<br/>
<pre class="syntax" data-space="preserve"><code>typedef /*[context_handle] */ void *PV;    //Note: PV is *not* a context handle.</code></pre>
Example ACF file:<br/>
<pre class="syntax" data-space="preserve"><code>typedef [context_handle_serialize] PV;    //MIDL 2378</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2379"></span><span id="midl2379"></span><dl> <dt><strong>MIDL2379</strong></dt> </dl></td>
<td><dl> <dt><span id="The_compiler_reached_a_limit_for_a_format_string_representation._See_documentation_for_advice."></span><span id="the_compiler_reached_a_limit_for_a_format_string_representation._see_documentation_for_advice."></span><span id="THE_COMPILER_REACHED_A_LIMIT_FOR_A_FORMAT_STRING_REPRESENTATION._SEE_DOCUMENTATION_FOR_ADVICE."></span>The compiler reached a limit for a format string representation. See documentation for advice.</dt> <dd> The MIDL compiler has a 64 KB limit for format strings. This error generally occurs when IDL files include other IDL files. The composite IDL file generated by all of the include statements exceeds the limits of the type representation tables of the marshaling engine interpreter. Try using the import directive rather than the include directive in your IDL files. For more information, see <a href="importing-system-header-files.md">Importing System Header Files</a>, <a href="include.md"><strong>include</strong></a>, and <a href="import.md"><strong>import</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2380"></span><span id="midl2380"></span><dl> <dt><strong>MIDL2380</strong></dt> </dl></td>
<td><dl> <dt><span id="wire_format_may_be_incorrect__you_may_need_to_use_-ms_conf_struct__see_documentation_for_advice"></span><span id="WIRE_FORMAT_MAY_BE_INCORRECT__YOU_MAY_NEED_TO_USE_-MS_CONF_STRUCT__SEE_DOCUMENTATION_FOR_ADVICE"></span>wire format may be incorrect, you may need to use -ms_conf_struct, see documentation for advice</dt> <dd> The MIDL compiler could not generate a transmissible format for the data. One common way to get this error is to define an <strong>ms_conf_struct</strong> inside a complex structure.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2381"></span><span id="midl2381"></span><dl> <dt><strong>MIDL2381</strong></dt> </dl></td>
<td><dl> <dt><span id="a_stack_size_or_an_offset_bigger_than_64_K_limit._See_documentation_for_advice."></span><span id="a_stack_size_or_an_offset_bigger_than_64_k_limit._see_documentation_for_advice."></span><span id="A_STACK_SIZE_OR_AN_OFFSET_BIGGER_THAN_64_K_LIMIT._SEE_DOCUMENTATION_FOR_ADVICE."></span>a stack size or an offset bigger than 64 K limit. See documentation for advice.</dt> <dd> The call results in a stack that is larger than 64 KB. Try passing the data in smaller blocks.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2382"></span><span id="midl2382"></span><dl> <dt><strong>MIDL2382</strong></dt> </dl></td>
<td><dl> <dt><span id="an_interpreter_mode_forced_for_64-bit_platform_"></span><span id="AN_INTERPRETER_MODE_FORCED_FOR_64-BIT_PLATFORM_"></span>an interpreter mode forced for 64-bit platform </dt> <dd> 64-bit platforms require the /Oicf compilation mode.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2383"></span><span id="midl2383"></span><dl> <dt><strong>MIDL2383</strong></dt> </dl></td>
<td><dl> <dt><span id="The_array_element_size_is_bigger_than_64_KB_limit."></span><span id="the_array_element_size_is_bigger_than_64_kb_limit."></span><span id="THE_ARRAY_ELEMENT_SIZE_IS_BIGGER_THAN_64_KB_LIMIT."></span>The array element size is bigger than 64 KB limit.</dt> <dd> All array elements must be less than 64 KB in size.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2384"></span><span id="midl2384"></span><dl> <dt><strong>MIDL2384</strong></dt> </dl></td>
<td><dl> <dt><span id="there_can_be_only_one__Icid__parameter_in_a_method__and_it_should_be_last_or_second_to_last_if_last_parameter_has__retval_"></span><span id="there_can_be_only_one__icid__parameter_in_a_method__and_it_should_be_last_or_second_to_last_if_last_parameter_has__retval_"></span><span id="THERE_CAN_BE_ONLY_ONE__ICID__PARAMETER_IN_A_METHOD__AND_IT_SHOULD_BE_LAST_OR_SECOND_TO_LAST_IF_LAST_PARAMETER_HAS__RETVAL_"></span>there can be only one [Icid] parameter in a method, and it should be last or second to last if last parameter has [retval]</dt> <dd> A parameter with the [<a href="lcid.md"><strong>lcid</strong></a>] attribute must occur last. The only exception is when there is also a parameter with the [<a href="retval.md"><strong>retval</strong></a>] attribute. When both occur, the second to the last parameter in the parameter list must have the [ <strong>lcid</strong>] attribute. The last parameter must have the [<strong>retval</strong>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2385"></span><span id="midl2385"></span><dl> <dt><strong>MIDL2385</strong></dt> </dl></td>
<td><dl> <dt><span id="incorrect_syntax_for_midl_pragma"></span><span id="INCORRECT_SYNTAX_FOR_MIDL_PRAGMA"></span>incorrect syntax for midl_pragma</dt> <dd> The MIDL compiler detected an unknown syntax error in a midl_pragma statement.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2386"></span><span id="midl2386"></span><dl> <dt><strong>MIDL2386</strong></dt> </dl></td>
<td><dl> <dt><span id="__int3264_is_not_supported_in__osf_mode"></span><span id="__INT3264_IS_NOT_SUPPORTED_IN__OSF_MODE"></span>__int3264 is not supported in /osf mode</dt> <dd> If you need to use __int3264, compile in /ms-ext mode.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2387"></span><span id="midl2387"></span><dl> <dt><strong>MIDL2387</strong></dt> </dl></td>
<td><dl> <dt><span id="unresolved_symbol_in_type_library"></span><span id="UNRESOLVED_SYMBOL_IN_TYPE_LIBRARY"></span>unresolved symbol in type library</dt> <dd> The compiler could not resolve a formal declaration or referenced type in the type library.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2388"></span><span id="midl2388"></span><dl> <dt><strong>MIDL2388</strong></dt> </dl></td>
<td><dl> <dt><span id="async_pipes_cannot_be_passed_by_value"></span><span id="ASYNC_PIPES_CANNOT_BE_PASSED_BY_VALUE"></span>async pipes cannot be passed by value</dt> <dd> Asynchronous pipes should be passed by reference or by address.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2389"></span><span id="midl2389"></span><dl> <dt><strong>MIDL2389</strong></dt> </dl></td>
<td><dl> <dt><span id="parameter_offset_exceed_64-KB_limit_for_interpreted_procedures"></span><span id="parameter_offset_exceed_64-kb_limit_for_interpreted_procedures"></span><span id="PARAMETER_OFFSET_EXCEED_64-KB_LIMIT_FOR_INTERPRETED_PROCEDURES"></span>parameter offset exceed 64-KB limit for interpreted procedures</dt> <dd> This error typically means that a procedure has too many parameters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2390"></span><span id="midl2390"></span><dl> <dt><strong>MIDL2390</strong></dt> </dl></td>
<td><dl> <dt><span id="invalid_array_element"></span><span id="INVALID_ARRAY_ELEMENT"></span>invalid array element</dt> <dd> Pipes cannot be used as array elements.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2391"></span><span id="midl2391"></span><dl> <dt><strong>MIDL2391</strong></dt> </dl></td>
<td><dl> <dt><span id="dispinterface_members_must_be_methods__properties_or_interfaces"></span><span id="DISPINTERFACE_MEMBERS_MUST_BE_METHODS__PROPERTIES_OR_INTERFACES"></span>dispinterface members must be methods, properties or interfaces</dt> <dd> A dispinterface cannot contain type definitions, structures, enumerations, or unions.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2392"></span><span id="midl2392"></span><dl> <dt><strong>MIDL2392</strong></dt> </dl></td>
<td><dl> <dt><span id="_local__procedure_without__call_as_"></span><span id="_LOCAL__PROCEDURE_WITHOUT__CALL_AS_"></span>[local] procedure without [call_as]</dt> <dd> Object procedures that have the [<a href="local.md"><strong>local</strong></a>] attribute also require the [<a href="call-as.md"><strong>call_as</strong></a>] attribute.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2393"></span><span id="midl2393"></span><dl> <dt><strong>MIDL2393</strong></dt> </dl></td>
<td><dl> <dt><span id="multi_dimensional_vector__switching_to__Oicf"></span><span id="multi_dimensional_vector__switching_to__oicf"></span><span id="MULTI_DIMENSIONAL_VECTOR__SWITCHING_TO__OICF"></span>multi dimensional vector, switching to /Oicf</dt> <dd> The <a href="-os.md"><strong>/Os</strong></a> optimization mode does not support multidimensional nonfixed size arrays. The compiler has automatically switched the optimization mode to /<strong>Oicf</strong> for this function. <br/> This warning can be suppressed globally by changing the compiler mode by specifying /<strong>Oicf</strong> on the MIDL command line or by using <strong>midl_pragma</strong> warning (disable: 2393) in the IDL file. The optimization mode can be changed for an individual function by adding the [<strong>optimize(&quot;icf&quot;)</strong>] attribute to the function in the ACF file.<br/> The following example demonstrates this warning:<br/>
<pre class="syntax" data-space="preserve"><code>void roo(long s1, [size_is(s1)] long a[][30];    //MIDL2393
void bar(long s1, long s2, [size_is(s1,s2) long **a);//MIDL2393</code></pre>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2395"></span><span id="midl2395"></span><dl> <dt><strong>MIDL2395</strong></dt> </dl></td>
<td><dl> <dt><span id="type_or_construct_not_supported_in_a_library_block_because_Oleaut32.dll_support_for_64-KB_polymorphic_types_is_missing"></span><span id="type_or_construct_not_supported_in_a_library_block_because_oleaut32.dll_support_for_64-kb_polymorphic_types_is_missing"></span><span id="TYPE_OR_CONSTRUCT_NOT_SUPPORTED_IN_A_LIBRARY_BLOCK_BECAUSE_OLEAUT32.DLL_SUPPORT_FOR_64-KB_POLYMORPHIC_TYPES_IS_MISSING"></span>type or construct not supported in a library block because Oleaut32.dll support for 64-KB polymorphic types is missing</dt> <dd> OLE automation does not support polymorphic types (such as _int3264, INT_PTR, etc). These types have incompatible data representations between 32-bit and 64-bit platforms. The remote call will fail at run time on 64-bit platforms.<br/>
<blockquote>
[!Note]<br />
Note that as of Windows 2000 release, 64-bit TLB files are supported by OLE Automation by converting 32-bit TLB information at run time. Therefore, only 32-bit TLB generation is supported by MIDL.
</blockquote>
<br/> If MIDL is being used just to generate a header file, the <a href="-notlb.md"><strong>/notlb</strong></a> switch will suppress generation of the TLB file.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2396"></span><span id="midl2396"></span><dl> <dt><strong>MIDL2396</strong></dt> </dl></td>
<td><dl> <dt><span id="old_interpreter_code_being_generated_for_64b"></span><span id="OLD_INTERPRETER_CODE_BEING_GENERATED_FOR_64B"></span>old interpreter code being generated for 64b</dt> <dd> This error is obsolete. If you see this error, please report a bug to Microsoft giving your IDL files, ACF files, and full MIDL-command line.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2397"></span><span id="midl2397"></span><dl> <dt><strong>MIDL2397</strong></dt> </dl></td>
<td><dl> <dt><span id="the_compiler_switch_is_not_supported_anymore"></span><span id="THE_COMPILER_SWITCH_IS_NOT_SUPPORTED_ANYMORE"></span>the compiler switch is not supported anymore</dt> <dd> The specified switch or switches are no longer supported.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2398"></span><span id="midl2398"></span><dl> <dt><strong>MIDL2398</strong></dt> </dl></td>
<td><dl> <dt><span id="cannot_execute_MIDL_engine"></span><span id="cannot_execute_midl_engine"></span><span id="CANNOT_EXECUTE_MIDL_ENGINE"></span>cannot execute MIDL engine</dt> <dd> As of the Windows 2000 release (MIDL version 5.03.279), the MIDL compiler is implemented using two executable files: Midl.exe (the driver), and Midlc.exe (the compiler engine). This error indicates the Midl.exe is unable to launch Midlc.exe. Make sure that Midlc.exe is in the same directory as Midl.exe, and that they are the same version.<br/> The error may have been caused by copying Midl.exe but not Midlx.exe from the latest distribution. Run <strong>midl</strong> and/or <strong>midlc</strong> at the command line without any parameters to see the version number of the executable.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2399"></span><span id="midl2399"></span><dl> <dt><strong>MIDL2399</strong></dt> </dl></td>
<td><dl> <dt><span id="bad_commands_from_driver"></span><span id="BAD_COMMANDS_FROM_DRIVER"></span>bad commands from driver</dt> <dd> As of the Windows 2000 release (MIDL version 5.03.279), the MIDL compiler is implemented using two executable files: Midl.exe (the driver), and Midlc.exe (the compiler engine). This error indicates that the temporary file used to pass commands from Midl.exe to Midlc.exe is missing or corrupt. Make sure that Midlc.exe is in the same directory as Midl.exe, and that they are the same version.<br/> The error may have been caused by attempting to run Midlc.exe directly or by copying Midl.exe but not Midlc.exe from the latest distribution. Run <strong>midl</strong> and/or <strong>midlc</strong> at the command line without any parameters to see the version number of the executable.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2400"></span><span id="midl2400"></span><dl> <dt><strong>MIDL2400</strong></dt> </dl></td>
<td><dl> <dt><span id="for_ole_automation__optional_parameters_should_be_VARIANT_or_VARIANT__"></span><span id="for_ole_automation__optional_parameters_should_be_variant_or_variant__"></span><span id="FOR_OLE_AUTOMATION__OPTIONAL_PARAMETERS_SHOULD_BE_VARIANT_OR_VARIANT__"></span>for ole automation, optional parameters should be VARIANT or VARIANT *</dt> <dd> OLE Automation requires that all [optional] parameters be of type <strong>VARIANT</strong> or <strong>VARIANT*</strong>.<br/> In OLE automation, using non-VARIANT parameters may cause the call to fail at run time or to pass undefined data for the [<a href="optional.md"><strong>optional</strong></a>] parameters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2401"></span><span id="midl2401"></span><dl> <dt><strong>MIDL2401</strong></dt> </dl></td>
<td><dl> <dt><span id="_defaultvalue__is_applied_to_a_non-VARIANT_and__optional_._Please_remove__optional_"></span><span id="_defaultvalue__is_applied_to_a_non-variant_and__optional_._please_remove__optional_"></span><span id="_DEFAULTVALUE__IS_APPLIED_TO_A_NON-VARIANT_AND__OPTIONAL_._PLEASE_REMOVE__OPTIONAL_"></span>[defaultvalue] is applied to a non-VARIANT and [optional]. Please remove [optional]</dt> <dd> The [<a href="defaultvalue.md"><strong>defaultvalue</strong></a>] attribute implies [<a href="optional.md"><strong>optional</strong></a>]. The [ <strong>optional</strong>] attribute is not necessary.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2402"></span><span id="midl2402"></span><dl> <dt><strong>MIDL2402</strong></dt> </dl></td>
<td><dl> <dt><span id="_optional__attribute_is_inapplicable_outside_of_a_library_block"></span><span id="_OPTIONAL__ATTRIBUTE_IS_INAPPLICABLE_OUTSIDE_OF_A_LIBRARY_BLOCK"></span>[optional] attribute is inapplicable outside of a library block</dt> <dd> The functionality implied by the [ <a href="optional.md"><strong>optional</strong></a>] attribute is not applicable to proxies generated for an interface outside of a library block.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2403"></span><span id="midl2403"></span><dl> <dt><strong>MIDL2403</strong></dt> </dl></td>
<td><dl> <dt><span id="The_data_type_of_the__Icid__parameter_must_be_long"></span><span id="the_data_type_of_the__icid__parameter_must_be_long"></span><span id="THE_DATA_TYPE_OF_THE__ICID__PARAMETER_MUST_BE_LONG"></span>The data type of the [Icid] parameter must be long</dt> <dd> OLE Automation requires that parameters with the [<strong>Icid</strong>] attribute must be of type <a href="long.md"><strong>long</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2404"></span><span id="midl2404"></span><dl> <dt><strong>MIDL2404</strong></dt> </dl></td>
<td><dl> <dt><span id="procedures_with__propput____propget__or__propref__can_t_have_more_than_one_required_parameter_after__optional__one"></span><span id="PROCEDURES_WITH__PROPPUT____PROPGET__OR__PROPREF__CAN_T_HAVE_MORE_THAN_ONE_REQUIRED_PARAMETER_AFTER__OPTIONAL__ONE"></span>procedures with [propput], [propget] or [propref] can't have more than one required parameter after [optional] one</dt> <dd> There cannot be more than one parameter without [<a href="optional.md"><strong>optional</strong></a>] after the last parameter with [<strong>optional</strong>] when using [<a href="propput.md"><strong>propput</strong></a>], [<a href="propget.md"><strong>propget</strong></a>], or [ <a href="propputref.md"><strong>propputref</strong></a>].<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2405"></span><span id="midl2405"></span><dl> <dt><strong>MIDL2405</strong></dt> </dl></td>
<td><dl> <dt><span id="_comm_status__or__fault_status__with_pickling_requires_-Oicf"></span><span id="_comm_status__or__fault_status__with_pickling_requires_-oicf"></span><span id="_COMM_STATUS__OR__FAULT_STATUS__WITH_PICKLING_REQUIRES_-OICF"></span>[comm_status] or [fault_status] with pickling requires -Oicf</dt> <dd> The old -<strong>Oi</strong> optimization mode does not support procedures or parameters with [ <a href="comm-status.md"><strong>comm_status</strong></a>] or [ <a href="fault-status.md"><strong>fault_status</strong></a>] with pickling (that is, using [ <a href="encode.md"><strong>encode</strong></a>] and/or [ <a href="decode.md"><strong>decode</strong></a>]).<br/> This warning can be suppressed globally by specifying -<strong>Oicf</strong> on the MIDL command line or for an individual function by adding the [optimize(&quot;icf:)] attribute to the function in the ACF file.<br/> In general, the -<strong>Oicf</strong> optimization mode is recommended over -<strong>Oi</strong> mode.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2406"></span><span id="midl2406"></span><dl> <dt><strong>MIDL2406</strong></dt> </dl></td>
<td><dl> <dt><span id="midl_driver_and_compiler_version_mismatch"></span><span id="MIDL_DRIVER_AND_COMPILER_VERSION_MISMATCH"></span>midl driver and compiler version mismatch</dt> <dd> As of the Windows 2000 release (MIDL version 5.03.279) the MIDL compiler is implemented using two executable files: Midl.exe (the driver), and Midlc.exe (the compiler engine). This error indicates that the version of Midl.exe does not match the version of Midlc.exe.<br/> The error may have been caused by copying Midl.exe but not Midlc.exe from the latest distribution. Run <strong>midl</strong> and/or <strong>midlc</strong> at the command line without any parameters to see the version number of the executable.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2407"></span><span id="midl2407"></span><dl> <dt><strong>MIDL2407</strong></dt> </dl></td>
<td><dl> <dt><span id="no_intermediate_file_specified__use_Midl.exe"></span><span id="no_intermediate_file_specified__use_midl.exe"></span><span id="NO_INTERMEDIATE_FILE_SPECIFIED__USE_MIDL.EXE"></span>no intermediate file specified: use Midl.exe</dt> <dd> As of the Windows 2000 release (MIDL version 5.03.279), the MIDL compiler is implemented using two executable files: Midl.exe (the driver), and Midlc.exe (the compiler engine). This error indicates that Midlc.exe was run directly instead of using Midl.exe.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2408"></span><span id="midl2408"></span><dl> <dt><strong>MIDL2408</strong></dt> </dl></td>
<td><dl> <dt><span id="processing_problem_with_a_parameter_in_a_procedure"></span><span id="PROCESSING_PROBLEM_WITH_A_PARAMETER_IN_A_PROCEDURE"></span>processing problem with a parameter in a procedure</dt> <dd> This error may be seen when importing data from a TLB and when a procedure has an invalid parameter. <br/> If you see this error, report a bug to Microsoft. Specify your IDL files, ACF files, TLB file, and full MIDL-command line.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2409"></span><span id="midl2409"></span><dl> <dt><strong>MIDL2409</strong></dt> </dl></td>
<td><dl> <dt><span id="processing_problem_with_a_field_in_a_structure"></span><span id="PROCESSING_PROBLEM_WITH_A_FIELD_IN_A_STRUCTURE"></span>processing problem with a field in a structure</dt> <dd> This error may be seen when importing data from a TLB and when a structure has an invalid structure or union field.<br/> If you see this error, report a bug to Microsoft. Specify your IDL files, ACF files, TLB file, and full MIDL-command line.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2410"></span><span id="midl2410"></span><dl> <dt><strong>MIDL2410</strong></dt> </dl></td>
<td><dl> <dt><span id="internal_compiler_inconsistency_detected__the_format_string_offset_is_invalid._See_the_documentation_for_more_information."></span><span id="internal_compiler_inconsistency_detected__the_format_string_offset_is_invalid._see_the_documentation_for_more_information."></span><span id="INTERNAL_COMPILER_INCONSISTENCY_DETECTED__THE_FORMAT_STRING_OFFSET_IS_INVALID._SEE_THE_DOCUMENTATION_FOR_MORE_INFORMATION."></span>internal compiler inconsistency detected: the format string offset is invalid. See the documentation for more information.</dt> <dd> The MIDL compiler detected an invalid value in its internal data structures. This may be caused by structures that are recursive or by compiler breaching its own limits of representation for internal data. To identify and/or work around the problem, try to simplify the IDL file. You can do this by simplifying complex parameters and recursive data structures or making the IDL file smaller by splitting it. This message may be accompanied by a diagnostic printout with additional information about the problem.<br/> If you see this error, report a bug to Microsoft. Specify your IDL files, ACF files, full MIDL command line, and diagnostic output, if any.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2411"></span><span id="midl2411"></span><dl> <dt><strong>MIDL2411</strong></dt> </dl></td>
<td><dl> <dt><span id="internal_compiler_inconsistency_detected__the_type_offset_is_invalid._See_the_documentation_for_more_information."></span><span id="internal_compiler_inconsistency_detected__the_type_offset_is_invalid._see_the_documentation_for_more_information."></span><span id="INTERNAL_COMPILER_INCONSISTENCY_DETECTED__THE_TYPE_OFFSET_IS_INVALID._SEE_THE_DOCUMENTATION_FOR_MORE_INFORMATION."></span>internal compiler inconsistency detected: the type offset is invalid. See the documentation for more information.</dt> <dd> The MIDL compiler detected an invalid value in its internal data structures. This may be caused by structures that are recursive or by the compiler breaching its own limits of representation for internal data. To identify and/or work around the problem try to simplify the IDL file. You can do this by simplifying complex parameters and recursive data structures or by making the IDL file smaller by splitting it. This message may be accompanied by a diagnostic printout with additional information about the problem.<br/> If yoiu see this error, report a bug to Microsoft. Specify your IDL files, ACF files, full MIDL command line, and diagnostic output, if any.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2412"></span><span id="midl2412"></span><dl> <dt><strong>MIDL2412</strong></dt> </dl></td>
<td><dl> <dt><span id="SAFEARRAY_roo__syntax_is_not_supported_outside_of_the_library_block__use_LPSAFEARRAY_for_proxy"></span><span id="safearray_roo__syntax_is_not_supported_outside_of_the_library_block__use_lpsafearray_for_proxy"></span><span id="SAFEARRAY_ROO__SYNTAX_IS_NOT_SUPPORTED_OUTSIDE_OF_THE_LIBRARY_BLOCK__USE_LPSAFEARRAY_FOR_PROXY"></span>SAFEARRAY(roo) syntax is not supported outside of the library block, use LPSAFEARRAY for proxy</dt> <dd> Explicitly-typed SAFEARRAYs are not allowed outside of a library block. Use LPSAFEARRAY instead.<br/> The following example demonstrates this error:<br/>
<pre class="syntax" data-space="preserve"><code>void roo(SAFEARRAY(long) *a); //MIDL2412 when outside a library block
void roo(LPSAFEAEEAY a);         //OK</code></pre>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2413"></span><span id="midl2413"></span><dl> <dt><strong>MIDL2413</strong></dt> </dl></td>
<td><dl> <dt><span id="bit_fields_are_not_supported"></span><span id="BIT_FIELDS_ARE_NOT_SUPPORTED"></span>bit fields are not supported</dt> <dd> C-style bit fields are not supported by MIDL. This applies to proxy generation as well as TLB generation.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2414"></span><span id="midl2414"></span><dl> <dt><strong>MIDL2414</strong></dt> </dl></td>
<td><dl> <dt><span id="floating_point_or_complex_return_types_with__decode__are_not_supported_in_-Oicf__using_-OI"></span><span id="floating_point_or_complex_return_types_with__decode__are_not_supported_in_-oicf__using_-oi"></span><span id="FLOATING_POINT_OR_COMPLEX_RETURN_TYPES_WITH__DECODE__ARE_NOT_SUPPORTED_IN_-OICF__USING_-OI"></span>floating point or complex return types with [decode] are not supported in -Oicf, using -OI</dt> <dd> Procedures with floating point or structure/union return types are not supported in the -Oicf style pickling. A work around for 32-bit is to use the -Oi optimization mode when serializing data (using [encode] and/or [decode]). However, as the old -Oi style interpreter and pickling support are slated to be phased out after the Windows 2000 release, using pointers is strongly suggested as the work around for this problem. Also note that typically, changing an interface method to use an [out, ref] pointer instead of the return value causing the problem is fully backward-compatible on wire and can be easily hidden from the app layer. <br/> This warning can be suppressed globally by specifying -Oi on the MIDL command line or for an individual function by adding the [optimize(&quot;i&quot;)] attribute to the function in the ACF file.<br/> The following example demonstrates the issue:<br/> roo.idl: <br/>
<pre class="syntax" data-space="preserve"><code>double GetDouble();</code></pre>
roo.acf: <br/>
<pre class="syntax" data-space="preserve"><code>[decode] GetDouble();</code></pre>
One option to work around this limitation would be to pass an [out] parameter to hold the result instead of using a return value:<br/> roo.idl: <br/>
<pre class="syntax" data-space="preserve"><code>void GetDouble([out] double *result); //top level pointer is a [ref] pointer</code></pre>
roo.acf: <br/>
<pre class="syntax" data-space="preserve"><code>[decode] GetDouble();</code></pre>
As mentioned earlier, the solution described above is good not only for the new interfaces but also as a work-around for the old ones. The wire representation for the new &quot;out&quot; argument is the same as for the return value (notice void as the new return value).<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2415"></span><span id="midl2415"></span><dl> <dt><strong>MIDL2415</strong></dt> </dl></td>
<td><dl> <dt><span id="the_return_type_is_not_supported_for_64-bit_when_using__decode_"></span><span id="THE_RETURN_TYPE_IS_NOT_SUPPORTED_FOR_64-BIT_WHEN_USING__DECODE_"></span>the return type is not supported for 64-bit when using [decode]</dt> <dd> Procedures with floating point or structure/union return types are not supported in 64-bit mode when performing data serialization (using [ <a href="encode.md"><strong>encode</strong></a>] and/or [ <a href="decode.md"><strong>decode</strong></a>]). This is related to the old style -Oi interpreter and data serializer not being supported on 64-bit platform. Please see the description of MIDL2414 for more information. <br/> The following example demonstrates this error:<br/> roo.idl: <br/>
<pre class="syntax" data-space="preserve"><code>double GetDouble();</code></pre>
roo.acf: <br/>
<pre class="syntax" data-space="preserve"><code>[decode] GetDouble();</code></pre>
The following is advised as a work-around for both new and old interfaces. Use an [out] parameter to hold the result instead of using a return value:<br/> roo.idl: <br/>
<pre class="syntax" data-space="preserve"><code>void GetDouble([out] double *result); //top level pointer is a [ref] pointer.</code></pre>
roo.acf: <br/>
<pre class="syntax" data-space="preserve"><code>[decode] GetDouble();</code></pre>
Note that this solution is fully backward-compatible on wire, as the wire representation of a [ref, out] pointer or a double is the same as that of a double.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2416"></span><span id="midl2416"></span><dl> <dt><strong>MIDL2416</strong></dt> </dl></td>
<td><dl> <dt><span id="transmitted_type_may_not_contain_a_full_pointer_for_either__wire_marshal__or__user_marshal_"></span><span id="TRANSMITTED_TYPE_MAY_NOT_CONTAIN_A_FULL_POINTER_FOR_EITHER__WIRE_MARSHAL__OR__USER_MARSHAL_"></span>transmitted type may not contain a full pointer for either [wire_marshal] or [user_marshal]</dt> <dd> Types with [ <a href="wire-marshal.md"><strong>wire_marshal</strong></a>] or [ <a href="user-marshal.md"><strong>user_marshal</strong></a>] attributes may not contain full ([ <strong>ptr</strong>]) pointers. Use [ <a href="unique.md"><strong>unique</strong></a>] or [ <a href="ref.md"><strong>ref</strong></a>] instead.<br/> The following example demonstrates this error:<br/>
<pre class="syntax" data-space="preserve"><code>typedef struct
{
    [ptr] long *a;    //Should use [ref] or [unique] instead
}
st1;
typedef [wire_marshal(st1)] struct
{
    long a;
}
st2:
void roo(st2 *s);    //MIDL2416</code></pre>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2417"></span><span id="midl2417"></span><dl> <dt><strong>MIDL2417</strong></dt> </dl></td>
<td><dl> <dt><span id="transmitted_type_must_either_be_a_pointer_or_have_a_constant_size_for__wire_marshal__and__user_marshal_"></span><span id="TRANSMITTED_TYPE_MUST_EITHER_BE_A_POINTER_OR_HAVE_A_CONSTANT_SIZE_FOR__WIRE_MARSHAL__AND__USER_MARSHAL_"></span>transmitted type must either be a pointer or have a constant size for [wire_marshal] and [user_marshal]</dt> <dd> Top-level types with [ <a href="wire-marshal.md"><strong>wire_marshal</strong></a>] or [ <a href="user-marshal.md"><strong>user_marshal</strong></a>] attributes must have a well-defined size at compile time. They cannot be or contain conformant or varying-sized arrays.<br/> The following example demonstrates this error:<br/>
<pre class="syntax" data-space="preserve"><code>typedef struct        //Type contains variable-sized array
{
    long s;
    [size_is(s)] char a[];
}
st1;
typedef [wire_marshal(st1)] struct
{
    long a;
}
st2;
void roo(st2 *s);        //MIDL2417</code></pre>
</dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2418"></span><span id="midl2418"></span><dl> <dt><strong>MIDL2418</strong></dt> </dl></td>
<td><dl> <dt><span id="procedures_with__propget__must_have_at_least_one_parameter_or_a_return_value"></span><span id="PROCEDURES_WITH__PROPGET__MUST_HAVE_AT_LEAST_ONE_PARAMETER_OR_A_RETURN_VALUE"></span>procedures with [propget] must have at least one parameter or a return value</dt> <dd> Procedures with the [propget] attribute must have some means of returning the property value. They must have at least one [<a href="-out.md"><strong>out</strong></a>] parameter or a return value.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL2461"></span><span id="midl2461"></span><dl> <dt><strong>MIDL2461</strong></dt> </dl></td>
<td><dl> <dt><span id="The__readonly__attribute_was_applied_at_the_method_level."></span><span id="the__readonly__attribute_was_applied_at_the_method_level."></span><span id="THE__READONLY__ATTRIBUTE_WAS_APPLIED_AT_THE_METHOD_LEVEL."></span>The [readonly] attribute was applied at the method level.</dt> <dd> The [readonly] attribute can only be applied at the parameter level.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="MIDL2465"></span><span id="midl2465"></span><dl> <dt><strong>MIDL2465</strong></dt> </dl></td>
<td><dl> <dt><span id="Structures_containing_conformant_arrays_must_be_passed_by_reference"></span><span id="structures_containing_conformant_arrays_must_be_passed_by_reference"></span><span id="STRUCTURES_CONTAINING_CONFORMANT_ARRAYS_MUST_BE_PASSED_BY_REFERENCE"></span>Structures containing conformant arrays must be passed by reference</dt> <dd> Top level parameters in RPC must have a well-defined size at compile time. They cannot be, nor contain conformant or varying-sized array. In addition, users cannot encode/decode a type without well-defined size. Applications need to pass conformant struct/conformant varying struct by reference.<br/> The following example demonstrates this error:<br/>
<pre class="syntax" data-space="preserve"><code>typedef struct        //Type contains variable-sized array
{
    long s;
    [size_is(s)] char a[];
}
st1;
void roo(st1 s);        //MIDL2465
 
on .acf file
typedef [encode,decode] st1; //MIDL2465</code></pre>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="MIDL9008"></span><span id="midl9008"></span><dl> <dt><strong>MIDL9008</strong></dt> </dl></td>
<td><dl> <dt><span id="_internal_compiler_problem__system_error_code__-_the_compiler_cannot_continue_for_an_unknown_reason._See_documentation_for_a_workaround."></span><span id="_internal_compiler_problem__system_error_code__-_the_compiler_cannot_continue_for_an_unknown_reason._see_documentation_for_a_workaround."></span><span id="_INTERNAL_COMPILER_PROBLEM__SYSTEM_ERROR_CODE__-_THE_COMPILER_CANNOT_CONTINUE_FOR_AN_UNKNOWN_REASON._SEE_DOCUMENTATION_FOR_A_WORKAROUND."></span> internal compiler problem <system error code> - the compiler cannot continue for an unknown reason. See documentation for a workaround.</dt> <dd> The compiler could not continue and the cause of the error is unknown. The hexadecimal error number is a system-error identifier. The compile may have failed because of an external problem, such as an out-of-memory condition. In that case, you can find more information in Winerror.h or Ntstatus.h. <br/> There are two situations that usually generate this error:<br/>
<ul>
<li>The MIDL compiler failed to recover after detecting an error in the IDL file. If MIDL returned any error messages about your IDL file, try fixing them and recompiling. If there are no error messages, the compiler may have failed before it could report an error. Look for a syntax error on the line for which the internal compiler error is reported.</li>
<li>The MIDL compiler could not generate correct code under a specified optimization option. Try changing compiler modes, compiling in mixed-mode optimization (/<a href="-os.md"><strong>Os</strong></a>), or removing all optimizations. Or, recompile using the /NO_FORMAT_OPT flag to suppress MIDL's default optimization of procedure and type descriptors.</li>
</ul>
Occasionally this error occurs even when the IDL file is correct and no optimization options are being used. If this is the case, try rewriting the section of code in the vicinity of where the error was reported by removing any recent modifications, simplifying or rearranging data types, changing prototypes, or else begin to comment out portions of the IDL file to locate the problem code.<br/> If none of these options works, or if you think the problem may be related to a bug in Midl.exe, please notify Microsoft, giving all the relevant details.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



 

