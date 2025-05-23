# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "playwright-testing workspace update",
)
class Update(AAZCommand):
    """Update Microsoft Azure Playwright Testing service Workspace resource

    :example: Update Playwright Testing Workspace_Disable Regional Affinity
        az playwright-testing workspace update --resource-group SampleRG --workspace-name myPlaywrightWorkspace --regional-affinity Disabled
    """

    _aaz_info = {
        "version": "2024-12-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.azureplaywrightservice/accounts/{}", "2024-12-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.workspace_name = AAZStrArg(
            options=["-n", "--name", "--workspace-name"],
            help="Name of Microsoft Azure Playwright Testing service workspace.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z]{1}[a-zA-Z0-9]{2,63}$",
                max_length=64,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of Azure resource group",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.local_auth = AAZStrArg(
            options=["--local-auth"],
            arg_group="Properties",
            help="When enabled, this feature allows the workspace to use local auth(through access key) for authentication of test runs.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.regional_affinity = AAZStrArg(
            options=["--regional-affinity"],
            arg_group="Properties",
            help="This property sets the connection region for Playwright client workers to cloud-hosted browsers. If enabled, workers connect to browsers in the closest Azure region, ensuring lower latency. If disabled, workers connect to browsers in the Azure region in which the workspace was initially created.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.reporting = AAZStrArg(
            options=["--reporting"],
            arg_group="Properties",
            help="When enabled, this feature allows the workspace to upload and display test results, including artifacts like traces and screenshots, in the Playwright portal. This enables faster and more efficient troubleshooting.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.scalable_execution = AAZStrArg(
            options=["--scalable-execution"],
            arg_group="Properties",
            help="When enabled, Playwright client workers can connect to cloud-hosted browsers. This can increase the number of parallel workers for a test run, significantly minimizing test completion durations.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AccountsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.AccountsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AccountsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzurePlaywrightService/accounts/{accountName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accountName", self.ctx.args.workspace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-12-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_account_read(cls._schema_on_200)

            return cls._schema_on_200

    class AccountsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzurePlaywrightService/accounts/{accountName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accountName", self.ctx.args.workspace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-12-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_account_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("localAuth", AAZStrType, ".local_auth")
                properties.set_prop("regionalAffinity", AAZStrType, ".regional_affinity")
                properties.set_prop("reporting", AAZStrType, ".reporting")
                properties.set_prop("scalableExecution", AAZStrType, ".scalable_execution")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_account_read = None

    @classmethod
    def _build_schema_account_read(cls, _schema):
        if cls._schema_account_read is not None:
            _schema.id = cls._schema_account_read.id
            _schema.location = cls._schema_account_read.location
            _schema.name = cls._schema_account_read.name
            _schema.properties = cls._schema_account_read.properties
            _schema.system_data = cls._schema_account_read.system_data
            _schema.tags = cls._schema_account_read.tags
            _schema.type = cls._schema_account_read.type
            return

        cls._schema_account_read = _schema_account_read = AAZObjectType()

        account_read = _schema_account_read
        account_read.id = AAZStrType(
            flags={"read_only": True},
        )
        account_read.location = AAZStrType(
            flags={"required": True},
        )
        account_read.name = AAZStrType(
            flags={"read_only": True},
        )
        account_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        account_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        account_read.tags = AAZDictType()
        account_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_account_read.properties
        properties.dashboard_uri = AAZStrType(
            serialized_name="dashboardUri",
            flags={"read_only": True},
        )
        properties.local_auth = AAZStrType(
            serialized_name="localAuth",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.regional_affinity = AAZStrType(
            serialized_name="regionalAffinity",
        )
        properties.reporting = AAZStrType()
        properties.scalable_execution = AAZStrType(
            serialized_name="scalableExecution",
        )

        system_data = _schema_account_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_account_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_account_read.id
        _schema.location = cls._schema_account_read.location
        _schema.name = cls._schema_account_read.name
        _schema.properties = cls._schema_account_read.properties
        _schema.system_data = cls._schema_account_read.system_data
        _schema.tags = cls._schema_account_read.tags
        _schema.type = cls._schema_account_read.type


__all__ = ["Update"]
