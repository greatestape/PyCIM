# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

""" This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.
"""

from cim15v01.iec61968.common import Document
from cim15v01.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimAssetModels"

ns_uri = "http://iec.ch/TC57/CIM-generic#AssetModels"

class AssetModel(Document):
    """ Documentation for a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model.
    """
    # <<< asset_model
    # @generated
    def __init__(self, corporate_standard_kind='other', usage_kind='distribution_underground', model_number='', weight_total=0.0, model_version='', erp_inventory_counts=None, type_asset=None, asset_model_catalogue_items=None, *args, **kw_args):
        """ Initialises a new 'AssetModel' instance.

        @param corporate_standard_kind: Kind of corporate standard for this asset model. Values are: "other", "under_evaluation", "experimental", "standard"
        @param usage_kind: Intended usage for this asset model. Values are: "distribution_underground", "other", "streetlight", "customer_substation", "unknown", "distribution_overhead", "substation", "transmission"
        @param model_number: Manufacturer's model number. 
        @param weight_total: Total manufactured weight of asset. 
        @param model_version: Version number for product model, which indicates vintage of the product. 
        @param erp_inventory_counts:
        @param type_asset: A type of asset may be satisified with many different types of asset models.
        @param asset_model_catalogue_items:
        """
        # Kind of corporate standard for this asset model. Values are: "other", "under_evaluation", "experimental", "standard"
        self.corporate_standard_kind = corporate_standard_kind

        # Intended usage for this asset model. Values are: "distribution_underground", "other", "streetlight", "customer_substation", "unknown", "distribution_overhead", "substation", "transmission"
        self.usage_kind = usage_kind

        # Manufacturer's model number. 
        self.model_number = model_number

        # Total manufactured weight of asset. 
        self.weight_total = weight_total

        # Version number for product model, which indicates vintage of the product. 
        self.model_version = model_version


        self._erp_inventory_counts = []
        if erp_inventory_counts is not None:
            self.erp_inventory_counts = erp_inventory_counts
        else:
            self.erp_inventory_counts = []

        self._type_asset = None
        self.type_asset = type_asset

        self._asset_model_catalogue_items = []
        if asset_model_catalogue_items is not None:
            self.asset_model_catalogue_items = asset_model_catalogue_items
        else:
            self.asset_model_catalogue_items = []


        super(AssetModel, self).__init__(*args, **kw_args)
    # >>> asset_model

    # <<< erp_inventory_counts
    # @generated
    def get_erp_inventory_counts(self):
        """ 
        """
        return self._erp_inventory_counts

    def set_erp_inventory_counts(self, value):
        for x in self._erp_inventory_counts:
            x._asset_model = None
        for y in value:
            y._asset_model = self
        self._erp_inventory_counts = value

    erp_inventory_counts = property(get_erp_inventory_counts, set_erp_inventory_counts)

    def add_erp_inventory_counts(self, *erp_inventory_counts):
        for obj in erp_inventory_counts:
            obj._asset_model = self
            self._erp_inventory_counts.append(obj)

    def remove_erp_inventory_counts(self, *erp_inventory_counts):
        for obj in erp_inventory_counts:
            obj._asset_model = None
            self._erp_inventory_counts.remove(obj)
    # >>> erp_inventory_counts

    # <<< type_asset
    # @generated
    def get_type_asset(self):
        """ A type of asset may be satisified with many different types of asset models.
        """
        return self._type_asset

    def set_type_asset(self, value):
        if self._type_asset is not None:
            filtered = [x for x in self.type_asset.asset_models if x != self]
            self._type_asset._asset_models = filtered

        self._type_asset = value
        if self._type_asset is not None:
            self._type_asset._asset_models.append(self)

    type_asset = property(get_type_asset, set_type_asset)
    # >>> type_asset

    # <<< asset_model_catalogue_items
    # @generated
    def get_asset_model_catalogue_items(self):
        """ 
        """
        return self._asset_model_catalogue_items

    def set_asset_model_catalogue_items(self, value):
        for x in self._asset_model_catalogue_items:
            x._asset_model = None
        for y in value:
            y._asset_model = self
        self._asset_model_catalogue_items = value

    asset_model_catalogue_items = property(get_asset_model_catalogue_items, set_asset_model_catalogue_items)

    def add_asset_model_catalogue_items(self, *asset_model_catalogue_items):
        for obj in asset_model_catalogue_items:
            obj._asset_model = self
            self._asset_model_catalogue_items.append(obj)

    def remove_asset_model_catalogue_items(self, *asset_model_catalogue_items):
        for obj in asset_model_catalogue_items:
            obj._asset_model = None
            self._asset_model_catalogue_items.remove(obj)
    # >>> asset_model_catalogue_items



class DistributionWindingTest(IdentifiedObject):
    """ Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.
    """
    # <<< distribution_winding_test
    # @generated
    def __init__(self, from_tap_step=0, from_winding=None, *args, **kw_args):
        """ Initialises a new 'DistributionWindingTest' instance.

        @param from_tap_step: Tap step number for the 'from' winding of the test pair. 
        @param from_winding: Winding that voltage or current is applied to during the test.
        """
        # Tap step number for the 'from' winding of the test pair. 
        self.from_tap_step = from_tap_step


        self._from_winding = None
        self.from_winding = from_winding


        super(DistributionWindingTest, self).__init__(*args, **kw_args)
    # >>> distribution_winding_test

    # <<< from_winding
    # @generated
    def get_from_winding(self):
        """ Winding that voltage or current is applied to during the test.
        """
        return self._from_winding

    def set_from_winding(self, value):
        if self._from_winding is not None:
            filtered = [x for x in self.from_winding.winding_tests if x != self]
            self._from_winding._winding_tests = filtered

        self._from_winding = value
        if self._from_winding is not None:
            self._from_winding._winding_tests.append(self)

    from_winding = property(get_from_winding, set_from_winding)
    # >>> from_winding



class WindingInfo(IdentifiedObject):
    """ Winding data.
    """
    # <<< winding_info
    # @generated
    def __init__(self, connection_kind='y', short_term_s=0.0, insulation_u=0.0, sequence_number=0, phase_angle=0, emergency_s=0.0, rated_u=0.0, r=0.0, rated_s=0.0, transformer_info=None, winding_tests=None, windings=None, to_winding_specs=None, *args, **kw_args):
        """ Initialises a new 'WindingInfo' instance.

        @param connection_kind: Kind of connection of this winding. Values are: "y", "yn", "zn", "i", "a", "d", "z"
        @param short_term_s: Apparent power that this winding can carry for a short period of time. 
        @param insulation_u: Basic insulation level voltage rating. 
        @param sequence_number: Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'. 
        @param phase_angle: Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11. 
        @param emergency_s: Apparent power that the winding can carry under emergency conditions. 
        @param rated_u: Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. 
        @param r: DC resistance of this winding. 
        @param rated_s: Normal apparent power rating of this winding. 
        @param transformer_info: Transformer data that this winding description is part of.
        @param winding_tests: All winding tests during which voltage or current was applied to this winding.
        @param windings: All windings described by this winding data.
        @param to_winding_specs: Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.
        """
        # Kind of connection of this winding. Values are: "y", "yn", "zn", "i", "a", "d", "z"
        self.connection_kind = connection_kind

        # Apparent power that this winding can carry for a short period of time. 
        self.short_term_s = short_term_s

        # Basic insulation level voltage rating. 
        self.insulation_u = insulation_u

        # Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'. 
        self.sequence_number = sequence_number

        # Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11. 
        self.phase_angle = phase_angle

        # Apparent power that the winding can carry under emergency conditions. 
        self.emergency_s = emergency_s

        # Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. 
        self.rated_u = rated_u

        # DC resistance of this winding. 
        self.r = r

        # Normal apparent power rating of this winding. 
        self.rated_s = rated_s


        self._transformer_info = None
        self.transformer_info = transformer_info

        self._winding_tests = []
        if winding_tests is not None:
            self.winding_tests = winding_tests
        else:
            self.winding_tests = []

        self._windings = []
        if windings is not None:
            self.windings = windings
        else:
            self.windings = []

        self._to_winding_specs = []
        if to_winding_specs is not None:
            self.to_winding_specs = to_winding_specs
        else:
            self.to_winding_specs = []


        super(WindingInfo, self).__init__(*args, **kw_args)
    # >>> winding_info

    # <<< transformer_info
    # @generated
    def get_transformer_info(self):
        """ Transformer data that this winding description is part of.
        """
        return self._transformer_info

    def set_transformer_info(self, value):
        if self._transformer_info is not None:
            filtered = [x for x in self.transformer_info.winding_infos if x != self]
            self._transformer_info._winding_infos = filtered

        self._transformer_info = value
        if self._transformer_info is not None:
            self._transformer_info._winding_infos.append(self)

    transformer_info = property(get_transformer_info, set_transformer_info)
    # >>> transformer_info

    # <<< winding_tests
    # @generated
    def get_winding_tests(self):
        """ All winding tests during which voltage or current was applied to this winding.
        """
        return self._winding_tests

    def set_winding_tests(self, value):
        for x in self._winding_tests:
            x._from_winding = None
        for y in value:
            y._from_winding = self
        self._winding_tests = value

    winding_tests = property(get_winding_tests, set_winding_tests)

    def add_winding_tests(self, *winding_tests):
        for obj in winding_tests:
            obj._from_winding = self
            self._winding_tests.append(obj)

    def remove_winding_tests(self, *winding_tests):
        for obj in winding_tests:
            obj._from_winding = None
            self._winding_tests.remove(obj)
    # >>> winding_tests

    # <<< windings
    # @generated
    def get_windings(self):
        """ All windings described by this winding data.
        """
        return self._windings

    def set_windings(self, value):
        for x in self._windings:
            x._winding_info = None
        for y in value:
            y._winding_info = self
        self._windings = value

    windings = property(get_windings, set_windings)

    def add_windings(self, *windings):
        for obj in windings:
            obj._winding_info = self
            self._windings.append(obj)

    def remove_windings(self, *windings):
        for obj in windings:
            obj._winding_info = None
            self._windings.remove(obj)
    # >>> windings

    # <<< to_winding_specs
    # @generated
    def get_to_winding_specs(self):
        """ Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.
        """
        return self._to_winding_specs

    def set_to_winding_specs(self, value):
        for x in self._to_winding_specs:
            x._to_winding = None
        for y in value:
            y._to_winding = self
        self._to_winding_specs = value

    to_winding_specs = property(get_to_winding_specs, set_to_winding_specs)

    def add_to_winding_specs(self, *to_winding_specs):
        for obj in to_winding_specs:
            obj._to_winding = self
            self._to_winding_specs.append(obj)

    def remove_to_winding_specs(self, *to_winding_specs):
        for obj in to_winding_specs:
            obj._to_winding = None
            self._to_winding_specs.remove(obj)
    # >>> to_winding_specs



class ConductorInfo(IdentifiedObject):
    """ Conductor data.
    """
    # <<< conductor_info
    # @generated
    def __init__(self, usage='secondary', insulation_material='high_pressure_fluid_filled', phase_count=0, insulated=False, insulation_thickness=0.0, conductor_segments=None, conductor_asset_model=None, wire_arrangements=None, *args, **kw_args):
        """ Initialises a new 'ConductorInfo' instance.

        @param usage: Usage of this conductor. Values are: "secondary", "transmission", "other", "distribution"
        @param insulation_material: (if insulated conductor) Material used for insulation. Values are: "high_pressure_fluid_filled", "low_capacitance_rubber", "crosslinked_polyethylene", "ozone_resistant_rubber", "high_molecular_weight_polyethylene", "tree_retardant_crosslinked_polyethylene", "oil_paper", "butyl", "belted_pilc", "rubber", "ethylene_propylene_rubber", "varnished_cambric_cloth", "asbestos_and_varnished_cambric", "tree_resistant_high_molecular_weight_polyethylene", "other", "silicon_rubber", "unbelted_pilc", "varnished_dacron_glass"
        @param phase_count: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        @param insulated: True if conductor is insulated. 
        @param insulation_thickness: (if insulated conductor) Thickness of the insulation. 
        @param conductor_segments: All conductor segments described by this conductor data.
        @param conductor_asset_model:
        @param wire_arrangements: All wire arrangements (single wires) that make this conductor.
        """
        # Usage of this conductor. Values are: "secondary", "transmission", "other", "distribution"
        self.usage = usage

        # (if insulated conductor) Material used for insulation. Values are: "high_pressure_fluid_filled", "low_capacitance_rubber", "crosslinked_polyethylene", "ozone_resistant_rubber", "high_molecular_weight_polyethylene", "tree_retardant_crosslinked_polyethylene", "oil_paper", "butyl", "belted_pilc", "rubber", "ethylene_propylene_rubber", "varnished_cambric_cloth", "asbestos_and_varnished_cambric", "tree_resistant_high_molecular_weight_polyethylene", "other", "silicon_rubber", "unbelted_pilc", "varnished_dacron_glass"
        self.insulation_material = insulation_material

        # Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        self.phase_count = phase_count

        # True if conductor is insulated. 
        self.insulated = insulated

        # (if insulated conductor) Thickness of the insulation. 
        self.insulation_thickness = insulation_thickness


        self._conductor_segments = []
        if conductor_segments is not None:
            self.conductor_segments = conductor_segments
        else:
            self.conductor_segments = []

        self._conductor_asset_model = None
        self.conductor_asset_model = conductor_asset_model

        self._wire_arrangements = []
        if wire_arrangements is not None:
            self.wire_arrangements = wire_arrangements
        else:
            self.wire_arrangements = []


        super(ConductorInfo, self).__init__(*args, **kw_args)
    # >>> conductor_info

    # <<< conductor_segments
    # @generated
    def get_conductor_segments(self):
        """ All conductor segments described by this conductor data.
        """
        return self._conductor_segments

    def set_conductor_segments(self, value):
        for x in self._conductor_segments:
            x._conductor_info = None
        for y in value:
            y._conductor_info = self
        self._conductor_segments = value

    conductor_segments = property(get_conductor_segments, set_conductor_segments)

    def add_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._conductor_info = self
            self._conductor_segments.append(obj)

    def remove_conductor_segments(self, *conductor_segments):
        for obj in conductor_segments:
            obj._conductor_info = None
            self._conductor_segments.remove(obj)
    # >>> conductor_segments

    # <<< conductor_asset_model
    # @generated
    def get_conductor_asset_model(self):
        """ 
        """
        return self._conductor_asset_model

    def set_conductor_asset_model(self, value):
        if self._conductor_asset_model is not None:
            self._conductor_asset_model._conductor_info = None

        self._conductor_asset_model = value
        if self._conductor_asset_model is not None:
            self._conductor_asset_model._conductor_info = self

    conductor_asset_model = property(get_conductor_asset_model, set_conductor_asset_model)
    # >>> conductor_asset_model

    # <<< wire_arrangements
    # @generated
    def get_wire_arrangements(self):
        """ All wire arrangements (single wires) that make this conductor.
        """
        return self._wire_arrangements

    def set_wire_arrangements(self, value):
        for x in self._wire_arrangements:
            x._conductor_info = None
        for y in value:
            y._conductor_info = self
        self._wire_arrangements = value

    wire_arrangements = property(get_wire_arrangements, set_wire_arrangements)

    def add_wire_arrangements(self, *wire_arrangements):
        for obj in wire_arrangements:
            obj._conductor_info = self
            self._wire_arrangements.append(obj)

    def remove_wire_arrangements(self, *wire_arrangements):
        for obj in wire_arrangements:
            obj._conductor_info = None
            self._wire_arrangements.remove(obj)
    # >>> wire_arrangements



class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a Conductor, with reference to their type.
    """
    # <<< wire_arrangement
    # @generated
    def __init__(self, position=0, mounting_point_y=0.0, mounting_point_x=0.0, wire_type=None, conductor_info=None, *args, **kw_args):
        """ Initialises a new 'WireArrangement' instance.

        @param position: Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC. 
        @param mounting_point_y: Height above ground of the first wire. 
        @param mounting_point_x: Signed horizontal distance from the first wire to a common reference point. 
        @param wire_type: Wire type used for this wire arrangement.
        @param conductor_info: Conductor data this wire arrangement belongs to.
        """
        # Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC. 
        self.position = position

        # Height above ground of the first wire. 
        self.mounting_point_y = mounting_point_y

        # Signed horizontal distance from the first wire to a common reference point. 
        self.mounting_point_x = mounting_point_x


        self._wire_type = None
        self.wire_type = wire_type

        self._conductor_info = None
        self.conductor_info = conductor_info


        super(WireArrangement, self).__init__(*args, **kw_args)
    # >>> wire_arrangement

    # <<< wire_type
    # @generated
    def get_wire_type(self):
        """ Wire type used for this wire arrangement.
        """
        return self._wire_type

    def set_wire_type(self, value):
        if self._wire_type is not None:
            filtered = [x for x in self.wire_type.wire_arrangements if x != self]
            self._wire_type._wire_arrangements = filtered

        self._wire_type = value
        if self._wire_type is not None:
            self._wire_type._wire_arrangements.append(self)

    wire_type = property(get_wire_type, set_wire_type)
    # >>> wire_type

    # <<< conductor_info
    # @generated
    def get_conductor_info(self):
        """ Conductor data this wire arrangement belongs to.
        """
        return self._conductor_info

    def set_conductor_info(self, value):
        if self._conductor_info is not None:
            filtered = [x for x in self.conductor_info.wire_arrangements if x != self]
            self._conductor_info._wire_arrangements = filtered

        self._conductor_info = value
        if self._conductor_info is not None:
            self._conductor_info._wire_arrangements.append(self)

    conductor_info = property(get_conductor_info, set_conductor_info)
    # >>> conductor_info



class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """
    # <<< wire_type
    # @generated
    def __init__(self, material='aluminum', strand_count=0, r_ac25=0.0, core_strand_count=0, rated_current=0.0, size_description='', gmr=0.0, r_ac75=0.0, radius=0.0, r_dc20=0.0, r_ac50=0.0, core_radius=0.0, wire_arrangements=None, concentric_neutral_cable_infos=None, *args, **kw_args):
        """ Initialises a new 'WireType' instance.

        @param material: Wire material. Values are: "aluminum", "steel", "other", "copper", "acsr"
        @param strand_count: Number of strands in the wire. 
        @param r_ac25: AC resistance per unit length of the conductor at 25 degrees C. 
        @param core_strand_count: (if used) Number of strands in the steel core. 
        @param rated_current: Current carrying capacity of the wire under stated thermal conditions. 
        @param size_description: Describes the wire guage or cross section (e.g., 4/0, #2, 336.5). 
        @param gmr: Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor. 
        @param r_ac75: AC resistance per unit length of the conductor at 75 degrees C. 
        @param radius: Outside radius of the wire. 
        @param r_dc20: DC resistance per unit length of the conductor at 20 degrees C. 
        @param r_ac50: AC resistance per unit length of the conductor at 50 degrees C. 
        @param core_radius: (if there is a different core material) Radius of the central core. 
        @param wire_arrangements: All wire arrangements using this wire type.
        @param concentric_neutral_cable_infos: All concentric neutral cables using this wire type.
        """
        # Wire material. Values are: "aluminum", "steel", "other", "copper", "acsr"
        self.material = material

        # Number of strands in the wire. 
        self.strand_count = strand_count

        # AC resistance per unit length of the conductor at 25 degrees C. 
        self.r_ac25 = r_ac25

        # (if used) Number of strands in the steel core. 
        self.core_strand_count = core_strand_count

        # Current carrying capacity of the wire under stated thermal conditions. 
        self.rated_current = rated_current

        # Describes the wire guage or cross section (e.g., 4/0, #2, 336.5). 
        self.size_description = size_description

        # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor. 
        self.gmr = gmr

        # AC resistance per unit length of the conductor at 75 degrees C. 
        self.r_ac75 = r_ac75

        # Outside radius of the wire. 
        self.radius = radius

        # DC resistance per unit length of the conductor at 20 degrees C. 
        self.r_dc20 = r_dc20

        # AC resistance per unit length of the conductor at 50 degrees C. 
        self.r_ac50 = r_ac50

        # (if there is a different core material) Radius of the central core. 
        self.core_radius = core_radius


        self._wire_arrangements = []
        if wire_arrangements is not None:
            self.wire_arrangements = wire_arrangements
        else:
            self.wire_arrangements = []

        self._concentric_neutral_cable_infos = []
        if concentric_neutral_cable_infos is not None:
            self.concentric_neutral_cable_infos = concentric_neutral_cable_infos
        else:
            self.concentric_neutral_cable_infos = []


        super(WireType, self).__init__(*args, **kw_args)
    # >>> wire_type

    # <<< wire_arrangements
    # @generated
    def get_wire_arrangements(self):
        """ All wire arrangements using this wire type.
        """
        return self._wire_arrangements

    def set_wire_arrangements(self, value):
        for x in self._wire_arrangements:
            x._wire_type = None
        for y in value:
            y._wire_type = self
        self._wire_arrangements = value

    wire_arrangements = property(get_wire_arrangements, set_wire_arrangements)

    def add_wire_arrangements(self, *wire_arrangements):
        for obj in wire_arrangements:
            obj._wire_type = self
            self._wire_arrangements.append(obj)

    def remove_wire_arrangements(self, *wire_arrangements):
        for obj in wire_arrangements:
            obj._wire_type = None
            self._wire_arrangements.remove(obj)
    # >>> wire_arrangements

    # <<< concentric_neutral_cable_infos
    # @generated
    def get_concentric_neutral_cable_infos(self):
        """ All concentric neutral cables using this wire type.
        """
        return self._concentric_neutral_cable_infos

    def set_concentric_neutral_cable_infos(self, value):
        for x in self._concentric_neutral_cable_infos:
            x._wire_type = None
        for y in value:
            y._wire_type = self
        self._concentric_neutral_cable_infos = value

    concentric_neutral_cable_infos = property(get_concentric_neutral_cable_infos, set_concentric_neutral_cable_infos)

    def add_concentric_neutral_cable_infos(self, *concentric_neutral_cable_infos):
        for obj in concentric_neutral_cable_infos:
            obj._wire_type = self
            self._concentric_neutral_cable_infos.append(obj)

    def remove_concentric_neutral_cable_infos(self, *concentric_neutral_cable_infos):
        for obj in concentric_neutral_cable_infos:
            obj._wire_type = None
            self._concentric_neutral_cable_infos.remove(obj)
    # >>> concentric_neutral_cable_infos



class TransformerInfo(IdentifiedObject):
    """ Set of transformer data, from an equipment library.
    """
    # <<< transformer_info
    # @generated
    def __init__(self, transformers=None, transformer_assets=None, winding_infos=None, transformer_asset_models=None, *args, **kw_args):
        """ Initialises a new 'TransformerInfo' instance.

        @param transformers: All transformers that can be described with this transformer data.
        @param transformer_assets:
        @param winding_infos: Data for all the windings described by this transformer data.
        @param transformer_asset_models:
        """

        self._transformers = []
        if transformers is not None:
            self.transformers = transformers
        else:
            self.transformers = []

        self._transformer_assets = []
        if transformer_assets is not None:
            self.transformer_assets = transformer_assets
        else:
            self.transformer_assets = []

        self._winding_infos = []
        if winding_infos is not None:
            self.winding_infos = winding_infos
        else:
            self.winding_infos = []

        self._transformer_asset_models = []
        if transformer_asset_models is not None:
            self.transformer_asset_models = transformer_asset_models
        else:
            self.transformer_asset_models = []


        super(TransformerInfo, self).__init__(*args, **kw_args)
    # >>> transformer_info

    # <<< transformers
    # @generated
    def get_transformers(self):
        """ All transformers that can be described with this transformer data.
        """
        return self._transformers

    def set_transformers(self, value):
        for x in self._transformers:
            x._transformer_info = None
        for y in value:
            y._transformer_info = self
        self._transformers = value

    transformers = property(get_transformers, set_transformers)

    def add_transformers(self, *transformers):
        for obj in transformers:
            obj._transformer_info = self
            self._transformers.append(obj)

    def remove_transformers(self, *transformers):
        for obj in transformers:
            obj._transformer_info = None
            self._transformers.remove(obj)
    # >>> transformers

    # <<< transformer_assets
    # @generated
    def get_transformer_assets(self):
        """ 
        """
        return self._transformer_assets

    def set_transformer_assets(self, value):
        for x in self._transformer_assets:
            x._transformer_info = None
        for y in value:
            y._transformer_info = self
        self._transformer_assets = value

    transformer_assets = property(get_transformer_assets, set_transformer_assets)

    def add_transformer_assets(self, *transformer_assets):
        for obj in transformer_assets:
            obj._transformer_info = self
            self._transformer_assets.append(obj)

    def remove_transformer_assets(self, *transformer_assets):
        for obj in transformer_assets:
            obj._transformer_info = None
            self._transformer_assets.remove(obj)
    # >>> transformer_assets

    # <<< winding_infos
    # @generated
    def get_winding_infos(self):
        """ Data for all the windings described by this transformer data.
        """
        return self._winding_infos

    def set_winding_infos(self, value):
        for x in self._winding_infos:
            x._transformer_info = None
        for y in value:
            y._transformer_info = self
        self._winding_infos = value

    winding_infos = property(get_winding_infos, set_winding_infos)

    def add_winding_infos(self, *winding_infos):
        for obj in winding_infos:
            obj._transformer_info = self
            self._winding_infos.append(obj)

    def remove_winding_infos(self, *winding_infos):
        for obj in winding_infos:
            obj._transformer_info = None
            self._winding_infos.remove(obj)
    # >>> winding_infos

    # <<< transformer_asset_models
    # @generated
    def get_transformer_asset_models(self):
        """ 
        """
        return self._transformer_asset_models

    def set_transformer_asset_models(self, value):
        for x in self._transformer_asset_models:
            x._transformer_info = None
        for y in value:
            y._transformer_info = self
        self._transformer_asset_models = value

    transformer_asset_models = property(get_transformer_asset_models, set_transformer_asset_models)

    def add_transformer_asset_models(self, *transformer_asset_models):
        for obj in transformer_asset_models:
            obj._transformer_info = self
            self._transformer_asset_models.append(obj)

    def remove_transformer_asset_models(self, *transformer_asset_models):
        for obj in transformer_asset_models:
            obj._transformer_info = None
            self._transformer_asset_models.remove(obj)
    # >>> transformer_asset_models



class ToWindingSpec(IdentifiedObject):
    """ For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.
    """
    # <<< to_winding_spec
    # @generated
    def __init__(self, voltage=0.0, to_tap_step=0, phase_shift=0.0, open_circuit_tests=None, short_circuit_tests=None, to_winding=None, *args, **kw_args):
        """ Initialises a new 'ToWindingSpec' instance.

        @param voltage: (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        @param to_tap_step: Tap step number for the 'to' winding of the test pair. 
        @param phase_shift: (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        @param open_circuit_tests: All open-circuit tests in which this winding was measured.
        @param short_circuit_tests: All short-circuit tests in which this winding was short-circuited.
        @param to_winding: Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
        """
        # (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        self.voltage = voltage

        # Tap step number for the 'to' winding of the test pair. 
        self.to_tap_step = to_tap_step

        # (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        self.phase_shift = phase_shift


        self._open_circuit_tests = []
        if open_circuit_tests is not None:
            self.open_circuit_tests = open_circuit_tests
        else:
            self.open_circuit_tests = []

        self._short_circuit_tests = []
        if short_circuit_tests is not None:
            self.short_circuit_tests = short_circuit_tests
        else:
            self.short_circuit_tests = []

        self._to_winding = None
        self.to_winding = to_winding


        super(ToWindingSpec, self).__init__(*args, **kw_args)
    # >>> to_winding_spec

    # <<< open_circuit_tests
    # @generated
    def get_open_circuit_tests(self):
        """ All open-circuit tests in which this winding was measured.
        """
        return self._open_circuit_tests

    def set_open_circuit_tests(self, value):
        for p in self._open_circuit_tests:
            filtered = [q for q in p.measured_winding_specs if q != self]
            self._open_circuit_tests._measured_winding_specs = filtered
        for r in value:
            if self not in r._measured_winding_specs:
                r._measured_winding_specs.append(self)
        self._open_circuit_tests = value

    open_circuit_tests = property(get_open_circuit_tests, set_open_circuit_tests)

    def add_open_circuit_tests(self, *open_circuit_tests):
        for obj in open_circuit_tests:
            if self not in obj._measured_winding_specs:
                obj._measured_winding_specs.append(self)
            self._open_circuit_tests.append(obj)

    def remove_open_circuit_tests(self, *open_circuit_tests):
        for obj in open_circuit_tests:
            if self in obj._measured_winding_specs:
                obj._measured_winding_specs.remove(self)
            self._open_circuit_tests.remove(obj)
    # >>> open_circuit_tests

    # <<< short_circuit_tests
    # @generated
    def get_short_circuit_tests(self):
        """ All short-circuit tests in which this winding was short-circuited.
        """
        return self._short_circuit_tests

    def set_short_circuit_tests(self, value):
        for p in self._short_circuit_tests:
            filtered = [q for q in p.shorted_winding_specs if q != self]
            self._short_circuit_tests._shorted_winding_specs = filtered
        for r in value:
            if self not in r._shorted_winding_specs:
                r._shorted_winding_specs.append(self)
        self._short_circuit_tests = value

    short_circuit_tests = property(get_short_circuit_tests, set_short_circuit_tests)

    def add_short_circuit_tests(self, *short_circuit_tests):
        for obj in short_circuit_tests:
            if self not in obj._shorted_winding_specs:
                obj._shorted_winding_specs.append(self)
            self._short_circuit_tests.append(obj)

    def remove_short_circuit_tests(self, *short_circuit_tests):
        for obj in short_circuit_tests:
            if self in obj._shorted_winding_specs:
                obj._shorted_winding_specs.remove(self)
            self._short_circuit_tests.remove(obj)
    # >>> short_circuit_tests

    # <<< to_winding
    # @generated
    def get_to_winding(self):
        """ Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
        """
        return self._to_winding

    def set_to_winding(self, value):
        if self._to_winding is not None:
            filtered = [x for x in self.to_winding.to_winding_specs if x != self]
            self._to_winding._to_winding_specs = filtered

        self._to_winding = value
        if self._to_winding is not None:
            self._to_winding._to_winding_specs.append(self)

    to_winding = property(get_to_winding, set_to_winding)
    # >>> to_winding



class CableInfo(ConductorInfo):
    """ Cable data.
    """
    # <<< cable_info
    # @generated
    def __init__(self, construction_kind='compacted', shield_material='other', outer_jacket_kind='linear_low_density_polyethylene', diameter_over_core=0.0, is_strand_fill=False, diameter_over_insulation=0.0, diameter_over_jacket=0.0, nominal_temperature=0.0, sheath_as_neutral=False, diameter_over_screen=0.0, *args, **kw_args):
        """ Initialises a new 'CableInfo' instance.

        @param construction_kind: Kind of construction of this cable. Values are: "compacted", "sector", "segmental", "solid", "stranded", "other", "compressed"
        @param shield_material: Material of the shield. Values are: "other", "aluminum", "steel", "lead", "copper"
        @param outer_jacket_kind: Kind of outer jacket of this cable. Values are: "linear_low_density_polyethylene", "semiconducting", "none", "other", "pvc", "insulating", "polyethylene"
        @param diameter_over_core: Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
        @param is_strand_fill: True if wire strands are extruded in a way to fill the voids in the cable. 
        @param diameter_over_insulation: Diameter over the insulating layer, excluding outer screen. 
        @param diameter_over_jacket: Diameter over the outermost jacketing layer. 
        @param nominal_temperature: Maximum nominal design operating temperature. 
        @param sheath_as_neutral: True if sheath / shield is used as a neutral (i.e., bonded). 
        @param diameter_over_screen: Diameter over the outer screen; should be the shield's inside diameter.. 
        """
        # Kind of construction of this cable. Values are: "compacted", "sector", "segmental", "solid", "stranded", "other", "compressed"
        self.construction_kind = construction_kind

        # Material of the shield. Values are: "other", "aluminum", "steel", "lead", "copper"
        self.shield_material = shield_material

        # Kind of outer jacket of this cable. Values are: "linear_low_density_polyethylene", "semiconducting", "none", "other", "pvc", "insulating", "polyethylene"
        self.outer_jacket_kind = outer_jacket_kind

        # Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
        self.diameter_over_core = diameter_over_core

        # True if wire strands are extruded in a way to fill the voids in the cable. 
        self.is_strand_fill = is_strand_fill

        # Diameter over the insulating layer, excluding outer screen. 
        self.diameter_over_insulation = diameter_over_insulation

        # Diameter over the outermost jacketing layer. 
        self.diameter_over_jacket = diameter_over_jacket

        # Maximum nominal design operating temperature. 
        self.nominal_temperature = nominal_temperature

        # True if sheath / shield is used as a neutral (i.e., bonded). 
        self.sheath_as_neutral = sheath_as_neutral

        # Diameter over the outer screen; should be the shield's inside diameter.. 
        self.diameter_over_screen = diameter_over_screen



        super(CableInfo, self).__init__(*args, **kw_args)
    # >>> cable_info



class ConcentricNeutralCableInfo(CableInfo):
    """ Concentric neutral cable data.
    """
    # <<< concentric_neutral_cable_info
    # @generated
    def __init__(self, neutral_strand_count=0, diameter_over_neutral=0.0, wire_type=None, *args, **kw_args):
        """ Initialises a new 'ConcentricNeutralCableInfo' instance.

        @param neutral_strand_count: Number of concentric neutral strands. 
        @param diameter_over_neutral: Diameter over the concentric neutral strands. 
        @param wire_type: Wire type used for this concentric neutral cable.
        """
        # Number of concentric neutral strands. 
        self.neutral_strand_count = neutral_strand_count

        # Diameter over the concentric neutral strands. 
        self.diameter_over_neutral = diameter_over_neutral


        self._wire_type = None
        self.wire_type = wire_type


        super(ConcentricNeutralCableInfo, self).__init__(*args, **kw_args)
    # >>> concentric_neutral_cable_info

    # <<< wire_type
    # @generated
    def get_wire_type(self):
        """ Wire type used for this concentric neutral cable.
        """
        return self._wire_type

    def set_wire_type(self, value):
        if self._wire_type is not None:
            filtered = [x for x in self.wire_type.concentric_neutral_cable_infos if x != self]
            self._wire_type._concentric_neutral_cable_infos = filtered

        self._wire_type = value
        if self._wire_type is not None:
            self._wire_type._concentric_neutral_cable_infos.append(self)

    wire_type = property(get_wire_type, set_wire_type)
    # >>> wire_type



class ShortCircuitTest(DistributionWindingTest):
    """ Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.
    """
    # <<< short_circuit_test
    # @generated
    def __init__(self, load_loss=0.0, load_loss_zero=0.0, leakage_impedance_zero=0.0, leakage_impedance=0.0, shorted_winding_specs=None, *args, **kw_args):
        """ Initialises a new 'ShortCircuitTest' instance.

        @param load_loss: Load losses from a positive-sequence or single-phase short-circuit test. 
        @param load_loss_zero: Load losses from a zero-sequence short-circuit test. 
        @param leakage_impedance_zero: Leakage impedance measured from a zero-sequence short-circuit test. 
        @param leakage_impedance: Leakage impedance measured from a positive-sequence or single-phase short-circuit test. 
        @param shorted_winding_specs: All windings short-circuited during this test.
        """
        # Load losses from a positive-sequence or single-phase short-circuit test. 
        self.load_loss = load_loss

        # Load losses from a zero-sequence short-circuit test. 
        self.load_loss_zero = load_loss_zero

        # Leakage impedance measured from a zero-sequence short-circuit test. 
        self.leakage_impedance_zero = leakage_impedance_zero

        # Leakage impedance measured from a positive-sequence or single-phase short-circuit test. 
        self.leakage_impedance = leakage_impedance


        self._shorted_winding_specs = []
        if shorted_winding_specs is not None:
            self.shorted_winding_specs = shorted_winding_specs
        else:
            self.shorted_winding_specs = []


        super(ShortCircuitTest, self).__init__(*args, **kw_args)
    # >>> short_circuit_test

    # <<< shorted_winding_specs
    # @generated
    def get_shorted_winding_specs(self):
        """ All windings short-circuited during this test.
        """
        return self._shorted_winding_specs

    def set_shorted_winding_specs(self, value):
        for p in self._shorted_winding_specs:
            filtered = [q for q in p.short_circuit_tests if q != self]
            self._shorted_winding_specs._short_circuit_tests = filtered
        for r in value:
            if self not in r._short_circuit_tests:
                r._short_circuit_tests.append(self)
        self._shorted_winding_specs = value

    shorted_winding_specs = property(get_shorted_winding_specs, set_shorted_winding_specs)

    def add_shorted_winding_specs(self, *shorted_winding_specs):
        for obj in shorted_winding_specs:
            if self not in obj._short_circuit_tests:
                obj._short_circuit_tests.append(self)
            self._shorted_winding_specs.append(obj)

    def remove_shorted_winding_specs(self, *shorted_winding_specs):
        for obj in shorted_winding_specs:
            if self in obj._short_circuit_tests:
                obj._short_circuit_tests.remove(self)
            self._shorted_winding_specs.remove(obj)
    # >>> shorted_winding_specs



class OverheadConductorInfo(ConductorInfo):
    """ Overhead conductor data.
    """
    # <<< overhead_conductor_info
    # @generated
    def __init__(self, neutral_insulation_thickness=0.0, phase_conductor_count=0, phase_conductor_spacing=0.0, *args, **kw_args):
        """ Initialises a new 'OverheadConductorInfo' instance.

        @param neutral_insulation_thickness: (if applicable) Insulation thickness of the neutral conductor. 
        @param phase_conductor_count: Number of conductor strands in the symmetrical bundle (1-12). 
        @param phase_conductor_spacing: Distance between conductor strands in a symmetrical bundle. 
        """
        # (if applicable) Insulation thickness of the neutral conductor. 
        self.neutral_insulation_thickness = neutral_insulation_thickness

        # Number of conductor strands in the symmetrical bundle (1-12). 
        self.phase_conductor_count = phase_conductor_count

        # Distance between conductor strands in a symmetrical bundle. 
        self.phase_conductor_spacing = phase_conductor_spacing



        super(OverheadConductorInfo, self).__init__(*args, **kw_args)
    # >>> overhead_conductor_info



class OpenCircuitTest(DistributionWindingTest):
    """ Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.
    """
    # <<< open_circuit_test
    # @generated
    def __init__(self, no_load_loss=0.0, exciting_current_zero=0.0, exciting_current=0.0, no_load_loss_zero=0.0, measured_winding_specs=None, *args, **kw_args):
        """ Initialises a new 'OpenCircuitTest' instance.

        @param no_load_loss: Losses measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        @param exciting_current_zero: Exciting current measured from a zero-sequence open-circuit (excitation) test. 
        @param exciting_current: Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        @param no_load_loss_zero: Losses measured from a zero-sequence open-circuit (excitation) test. 
        @param measured_winding_specs: All other windings measured during this test.
        """
        # Losses measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        self.no_load_loss = no_load_loss

        # Exciting current measured from a zero-sequence open-circuit (excitation) test. 
        self.exciting_current_zero = exciting_current_zero

        # Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        self.exciting_current = exciting_current

        # Losses measured from a zero-sequence open-circuit (excitation) test. 
        self.no_load_loss_zero = no_load_loss_zero


        self._measured_winding_specs = []
        if measured_winding_specs is not None:
            self.measured_winding_specs = measured_winding_specs
        else:
            self.measured_winding_specs = []


        super(OpenCircuitTest, self).__init__(*args, **kw_args)
    # >>> open_circuit_test

    # <<< measured_winding_specs
    # @generated
    def get_measured_winding_specs(self):
        """ All other windings measured during this test.
        """
        return self._measured_winding_specs

    def set_measured_winding_specs(self, value):
        for p in self._measured_winding_specs:
            filtered = [q for q in p.open_circuit_tests if q != self]
            self._measured_winding_specs._open_circuit_tests = filtered
        for r in value:
            if self not in r._open_circuit_tests:
                r._open_circuit_tests.append(self)
        self._measured_winding_specs = value

    measured_winding_specs = property(get_measured_winding_specs, set_measured_winding_specs)

    def add_measured_winding_specs(self, *measured_winding_specs):
        for obj in measured_winding_specs:
            if self not in obj._open_circuit_tests:
                obj._open_circuit_tests.append(self)
            self._measured_winding_specs.append(obj)

    def remove_measured_winding_specs(self, *measured_winding_specs):
        for obj in measured_winding_specs:
            if self in obj._open_circuit_tests:
                obj._open_circuit_tests.remove(self)
            self._measured_winding_specs.remove(obj)
    # >>> measured_winding_specs



class TapeShieldCableInfo(CableInfo):
    """ Tape shield cable data.
    """
    # <<< tape_shield_cable_info
    # @generated
    def __init__(self, tape_thickness=0.0, tape_lap=0.0, *args, **kw_args):
        """ Initialises a new 'TapeShieldCableInfo' instance.

        @param tape_thickness: Thickness of the tape shield, before wrapping. 
        @param tape_lap: Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%. 
        """
        # Thickness of the tape shield, before wrapping. 
        self.tape_thickness = tape_thickness

        # Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%. 
        self.tape_lap = tape_lap



        super(TapeShieldCableInfo, self).__init__(*args, **kw_args)
    # >>> tape_shield_cable_info



class EndDeviceModel(AssetModel):
    """ Documentation for particular end device product model made by a manufacturer.
    """
    # <<< end_device_model
    # @generated
    def __init__(self, end_device_type_asset=None, end_device_assets=None, *args, **kw_args):
        """ Initialises a new 'EndDeviceModel' instance.

        @param end_device_type_asset:
        @param end_device_assets: All end device assets being of this model.
        """

        self._end_device_type_asset = None
        self.end_device_type_asset = end_device_type_asset

        self._end_device_assets = []
        if end_device_assets is not None:
            self.end_device_assets = end_device_assets
        else:
            self.end_device_assets = []


        super(EndDeviceModel, self).__init__(*args, **kw_args)
    # >>> end_device_model

    # <<< end_device_type_asset
    # @generated
    def get_end_device_type_asset(self):
        """ 
        """
        return self._end_device_type_asset

    def set_end_device_type_asset(self, value):
        if self._end_device_type_asset is not None:
            filtered = [x for x in self.end_device_type_asset.end_device_models if x != self]
            self._end_device_type_asset._end_device_models = filtered

        self._end_device_type_asset = value
        if self._end_device_type_asset is not None:
            self._end_device_type_asset._end_device_models.append(self)

    end_device_type_asset = property(get_end_device_type_asset, set_end_device_type_asset)
    # >>> end_device_type_asset

    # <<< end_device_assets
    # @generated
    def get_end_device_assets(self):
        """ All end device assets being of this model.
        """
        return self._end_device_assets

    def set_end_device_assets(self, value):
        for x in self._end_device_assets:
            x._end_device_model = None
        for y in value:
            y._end_device_model = self
        self._end_device_assets = value

    end_device_assets = property(get_end_device_assets, set_end_device_assets)

    def add_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            obj._end_device_model = self
            self._end_device_assets.append(obj)

    def remove_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            obj._end_device_model = None
            self._end_device_assets.remove(obj)
    # >>> end_device_assets



# <<< asset_models
# @generated
# >>> asset_models
