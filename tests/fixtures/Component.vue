<template>
  <div>
    <UsedComponent/>
    <componentusedinlowercase/>
    <component-used-in-kebab-case/>
  </div>
</template>

<script>
import Vue from 'vue';
import _ from 'lodash';

import { mapGetters } from 'vuex';

import UsedComponent from './UsedComponent';
import UnusedComponent from './UnusedComponent';
import SomeMixin from './Mixins/SomeMixin';

import ComponentUsedInLowercase from './ComponentUsedInLowercase';
import ComponentUsedInKebabCase from './ComponentUsedInKebabCase';

export default {
  components: {
    UsedComponent,
    UnusedComponent,
  },
  mixins: [SomeMixin],
};
</script>
