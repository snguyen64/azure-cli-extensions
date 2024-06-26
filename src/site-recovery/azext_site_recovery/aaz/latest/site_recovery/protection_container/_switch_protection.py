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
    "site-recovery protection-container switch-protection",
)
class SwitchProtection(AAZCommand):
    """Operation to switch protection from one container to another or one replication provider to another.

    :example: protection-container switch-protection for A2A
        az site-recovery protection-container switch-protection --fabric-name fabric1_name -n container1_name --protected-item protected_item_name -g rg --vault-name vault_name --provider-details '{a2a:{policy-id:policy_id,recovery-container-id:container1_id,recovery-resource-group-id:vm_rg_id,vm-managed-disks:[{disk-id:recovery_os_disk,primary-staging-azure-storage-account-id:storage2_id,recovery-resource-group-id:vm_rg_id}]}}'
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.recoveryservices/vaults/{}/replicationfabrics/{}/replicationprotectioncontainers/{}/switchprotection", "2022-08-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

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
        _args_schema.fabric_name = AAZStrArg(
            options=["--fabric-name"],
            help="Unique fabric name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.protection_container_name = AAZStrArg(
            options=["-n", "--protection-container-name"],
            help="The name of the protection container.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vault_name = AAZStrArg(
            options=["--vault-name"],
            help="The name of the recovery services vault.",
            required=True,
            id_part="name",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.provider_specific_details = AAZObjectArg(
            options=["--provider-details", "--provider-specific-details"],
            arg_group="Properties",
            help="Provider specific switch protection input.",
        )
        _args_schema.replication_protected_item_name = AAZStrArg(
            options=["--protected-item", "--replication-protected-item-name"],
            arg_group="Properties",
            help="The unique replication protected item name.",
        )

        provider_specific_details = cls._args_schema.provider_specific_details
        provider_specific_details.a2a = AAZObjectArg(
            options=["a2a"],
            help="A2A",
        )

        a2a = cls._args_schema.provider_specific_details.a2a
        a2a.disk_encryption_info = AAZObjectArg(
            options=["disk-encryption-info"],
            help="The recovery disk encryption information.",
        )
        cls._build_args_disk_encryption_info_create(a2a.disk_encryption_info)
        a2a.policy_id = AAZStrArg(
            options=["policy-id"],
            help="The Policy Id.",
        )
        a2a.recovery_availability_set_id = AAZStrArg(
            options=["recovery-availability-set-id"],
            help="The recovery availability set.",
        )
        a2a.recovery_availability_zone = AAZStrArg(
            options=["recovery-availability-zone"],
            help="The recovery availability zone.",
        )
        a2a.recovery_boot_diag_storage_account_id = AAZStrArg(
            options=["recovery-boot-diag-storage-account-id"],
            help="The boot diagnostic storage account.",
        )
        a2a.recovery_capacity_reservation_group_id = AAZStrArg(
            options=["recovery-capacity-reservation-group-id"],
            help="The recovery capacity reservation group Id.",
        )
        a2a.recovery_cloud_service_id = AAZStrArg(
            options=["recovery-cloud-service-id"],
            help="The recovery cloud service Id. Valid for V1 scenarios.",
        )
        a2a.recovery_container_id = AAZStrArg(
            options=["recovery-container-id"],
            help="The recovery container Id.",
        )
        a2a.recovery_proximity_placement_group_id = AAZStrArg(
            options=["recovery-proximity-placement-group-id"],
            help="The recovery proximity placement group Id.",
        )
        a2a.recovery_resource_group_id = AAZStrArg(
            options=["recovery-resource-group-id"],
            help="The recovery resource group Id. Valid for V2 scenarios.",
        )
        a2a.recovery_virtual_machine_scale_set_id = AAZStrArg(
            options=["recovery-virtual-machine-scale-set-id"],
            help="The virtual machine scale set id.",
        )
        a2a.vm_disks = AAZListArg(
            options=["vm-disks"],
            help="The list of vm disk details.",
        )
        a2a.vm_managed_disks = AAZListArg(
            options=["vm-managed-disks"],
            help="The list of vm managed disk details.",
        )

        vm_disks = cls._args_schema.provider_specific_details.a2a.vm_disks
        vm_disks.Element = AAZObjectArg()

        _element = cls._args_schema.provider_specific_details.a2a.vm_disks.Element
        _element.disk_uri = AAZStrArg(
            options=["disk-uri"],
            help="The disk Uri.",
            required=True,
        )
        _element.primary_staging_azure_storage_account_id = AAZStrArg(
            options=["primary-staging-azure-storage-account-id"],
            help="The primary staging storage account Id.",
            required=True,
        )
        _element.recovery_azure_storage_account_id = AAZStrArg(
            options=["recovery-azure-storage-account-id"],
            help="The recovery VHD storage account Id.",
            required=True,
        )

        vm_managed_disks = cls._args_schema.provider_specific_details.a2a.vm_managed_disks
        vm_managed_disks.Element = AAZObjectArg()

        _element = cls._args_schema.provider_specific_details.a2a.vm_managed_disks.Element
        _element.disk_encryption_info = AAZObjectArg(
            options=["disk-encryption-info"],
            help="The recovery disk encryption information (for one / single pass flows).",
        )
        cls._build_args_disk_encryption_info_create(_element.disk_encryption_info)
        _element.disk_id = AAZStrArg(
            options=["disk-id"],
            help="The disk Id.",
            required=True,
        )
        _element.primary_staging_azure_storage_account_id = AAZStrArg(
            options=["primary-staging-azure-storage-account-id"],
            help="The primary staging storage account Arm Id.",
            required=True,
        )
        _element.recovery_disk_encryption_set_id = AAZStrArg(
            options=["recovery-disk-encryption-set-id"],
            help="The recovery disk encryption set Id.",
        )
        _element.recovery_replica_disk_account_type = AAZStrArg(
            options=["recovery-replica-disk-account-type"],
            help="The replica disk type. Its an optional value and will be same as source disk type if not user provided.",
        )
        _element.recovery_resource_group_id = AAZStrArg(
            options=["recovery-resource-group-id"],
            help="The target resource group Arm Id.",
            required=True,
        )
        _element.recovery_target_disk_account_type = AAZStrArg(
            options=["recovery-target-disk-account-type"],
            help="The target disk type after failover. Its an optional value and will be same as source disk type if not user provided.",
        )
        return cls._args_schema

    _args_disk_encryption_info_create = None

    @classmethod
    def _build_args_disk_encryption_info_create(cls, _schema):
        if cls._args_disk_encryption_info_create is not None:
            _schema.disk_encryption_key_info = cls._args_disk_encryption_info_create.disk_encryption_key_info
            _schema.key_encryption_key_info = cls._args_disk_encryption_info_create.key_encryption_key_info
            return

        cls._args_disk_encryption_info_create = AAZObjectArg()

        disk_encryption_info_create = cls._args_disk_encryption_info_create
        disk_encryption_info_create.disk_encryption_key_info = AAZObjectArg(
            options=["disk-encryption-key-info"],
            help="The recovery KeyVault reference for secret.",
        )
        disk_encryption_info_create.key_encryption_key_info = AAZObjectArg(
            options=["key-encryption-key-info"],
            help="The recovery KeyVault reference for key.",
        )

        disk_encryption_key_info = cls._args_disk_encryption_info_create.disk_encryption_key_info
        disk_encryption_key_info.key_vault_resource_arm_id = AAZStrArg(
            options=["key-vault-resource-arm-id"],
            help="The KeyVault resource ARM id for secret.",
        )
        disk_encryption_key_info.secret_identifier = AAZStrArg(
            options=["secret-identifier"],
            help="The secret url / identifier.",
        )

        key_encryption_key_info = cls._args_disk_encryption_info_create.key_encryption_key_info
        key_encryption_key_info.key_identifier = AAZStrArg(
            options=["key-identifier"],
            help="The key URL / identifier.",
        )
        key_encryption_key_info.key_vault_resource_arm_id = AAZStrArg(
            options=["key-vault-resource-arm-id"],
            help="The KeyVault resource ARM Id for key.",
        )

        _schema.disk_encryption_key_info = cls._args_disk_encryption_info_create.disk_encryption_key_info
        _schema.key_encryption_key_info = cls._args_disk_encryption_info_create.key_encryption_key_info

    def _execute_operations(self):
        self.pre_operations()
        yield self.ReplicationProtectionContainersSwitchProtection(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ReplicationProtectionContainersSwitchProtection(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/switchprotection",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "fabricName", self.ctx.args.fabric_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "protectionContainerName", self.ctx.args.protection_container_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.vault_name,
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
                    "api-version", "2022-08-01",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("providerSpecificDetails", AAZObjectType, ".provider_specific_details")
                properties.set_prop("replicationProtectedItemName", AAZStrType, ".replication_protected_item_name")

            provider_specific_details = _builder.get(".properties.providerSpecificDetails")
            if provider_specific_details is not None:
                provider_specific_details.set_const("instanceType", "A2A", AAZStrType, ".a2a", typ_kwargs={"flags": {"required": True}})
                provider_specific_details.discriminate_by("instanceType", "A2A")

            disc_a2_a = _builder.get(".properties.providerSpecificDetails{instanceType:A2A}")
            if disc_a2_a is not None:
                _SwitchProtectionHelper._build_schema_disk_encryption_info_create(disc_a2_a.set_prop("diskEncryptionInfo", AAZObjectType, ".a2a.disk_encryption_info"))
                disc_a2_a.set_prop("policyId", AAZStrType, ".a2a.policy_id")
                disc_a2_a.set_prop("recoveryAvailabilitySetId", AAZStrType, ".a2a.recovery_availability_set_id")
                disc_a2_a.set_prop("recoveryAvailabilityZone", AAZStrType, ".a2a.recovery_availability_zone")
                disc_a2_a.set_prop("recoveryBootDiagStorageAccountId", AAZStrType, ".a2a.recovery_boot_diag_storage_account_id")
                disc_a2_a.set_prop("recoveryCapacityReservationGroupId", AAZStrType, ".a2a.recovery_capacity_reservation_group_id")
                disc_a2_a.set_prop("recoveryCloudServiceId", AAZStrType, ".a2a.recovery_cloud_service_id")
                disc_a2_a.set_prop("recoveryContainerId", AAZStrType, ".a2a.recovery_container_id")
                disc_a2_a.set_prop("recoveryProximityPlacementGroupId", AAZStrType, ".a2a.recovery_proximity_placement_group_id")
                disc_a2_a.set_prop("recoveryResourceGroupId", AAZStrType, ".a2a.recovery_resource_group_id")
                disc_a2_a.set_prop("recoveryVirtualMachineScaleSetId", AAZStrType, ".a2a.recovery_virtual_machine_scale_set_id")
                disc_a2_a.set_prop("vmDisks", AAZListType, ".a2a.vm_disks")
                disc_a2_a.set_prop("vmManagedDisks", AAZListType, ".a2a.vm_managed_disks")

            vm_disks = _builder.get(".properties.providerSpecificDetails{instanceType:A2A}.vmDisks")
            if vm_disks is not None:
                vm_disks.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.providerSpecificDetails{instanceType:A2A}.vmDisks[]")
            if _elements is not None:
                _elements.set_prop("diskUri", AAZStrType, ".disk_uri", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("primaryStagingAzureStorageAccountId", AAZStrType, ".primary_staging_azure_storage_account_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("recoveryAzureStorageAccountId", AAZStrType, ".recovery_azure_storage_account_id", typ_kwargs={"flags": {"required": True}})

            vm_managed_disks = _builder.get(".properties.providerSpecificDetails{instanceType:A2A}.vmManagedDisks")
            if vm_managed_disks is not None:
                vm_managed_disks.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.providerSpecificDetails{instanceType:A2A}.vmManagedDisks[]")
            if _elements is not None:
                _SwitchProtectionHelper._build_schema_disk_encryption_info_create(_elements.set_prop("diskEncryptionInfo", AAZObjectType, ".disk_encryption_info"))
                _elements.set_prop("diskId", AAZStrType, ".disk_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("primaryStagingAzureStorageAccountId", AAZStrType, ".primary_staging_azure_storage_account_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("recoveryDiskEncryptionSetId", AAZStrType, ".recovery_disk_encryption_set_id")
                _elements.set_prop("recoveryReplicaDiskAccountType", AAZStrType, ".recovery_replica_disk_account_type")
                _elements.set_prop("recoveryResourceGroupId", AAZStrType, ".recovery_resource_group_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("recoveryTargetDiskAccountType", AAZStrType, ".recovery_target_disk_account_type")

            return self.serialize_content(_content_value)

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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.fabric_friendly_name = AAZStrType(
                serialized_name="fabricFriendlyName",
            )
            properties.fabric_specific_details = AAZObjectType(
                serialized_name="fabricSpecificDetails",
            )
            properties.fabric_type = AAZStrType(
                serialized_name="fabricType",
            )
            properties.friendly_name = AAZStrType(
                serialized_name="friendlyName",
            )
            properties.pairing_status = AAZStrType(
                serialized_name="pairingStatus",
            )
            properties.protected_item_count = AAZIntType(
                serialized_name="protectedItemCount",
            )
            properties.role = AAZStrType()

            fabric_specific_details = cls._schema_on_200.properties.fabric_specific_details
            fabric_specific_details.instance_type = AAZStrType(
                serialized_name="instanceType",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _SwitchProtectionHelper:
    """Helper class for SwitchProtection"""

    @classmethod
    def _build_schema_disk_encryption_info_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("diskEncryptionKeyInfo", AAZObjectType, ".disk_encryption_key_info")
        _builder.set_prop("keyEncryptionKeyInfo", AAZObjectType, ".key_encryption_key_info")

        disk_encryption_key_info = _builder.get(".diskEncryptionKeyInfo")
        if disk_encryption_key_info is not None:
            disk_encryption_key_info.set_prop("keyVaultResourceArmId", AAZStrType, ".key_vault_resource_arm_id")
            disk_encryption_key_info.set_prop("secretIdentifier", AAZStrType, ".secret_identifier")

        key_encryption_key_info = _builder.get(".keyEncryptionKeyInfo")
        if key_encryption_key_info is not None:
            key_encryption_key_info.set_prop("keyIdentifier", AAZStrType, ".key_identifier")
            key_encryption_key_info.set_prop("keyVaultResourceArmId", AAZStrType, ".key_vault_resource_arm_id")


__all__ = ["SwitchProtection"]
