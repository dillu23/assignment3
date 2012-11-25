(function() {
  packages = {

    // Lazily construct the package hierarchy from class names.
    root: function(classes) {
      var map = {};

      function find(name, data) {
        var node = map[name], i;
        if (!node) {
          node = map[name] = data || {name: name, children: []};
          if (name.length) {
			var k=name.lastIndexOf(".");
			var k1=name.substring(0,k).lastIndexOf(".");
			if(name.charAt(0)=='0'){
				k1=name.indexOf(".");
				k=name.substring(k1+1,name.length).indexOf(".")
			}
            node.parent = find(name.substring(k1+1,k+k1+1));
            //var i1=name.substring(i).lastIndexOf(".");
            node.parent.children.push(node);
            node.key = name.substring(k1+1);
          }
        }
        return node;
      }

      classes.forEach(function(d) {
        find(d.name, d);
      });

      return map[""];
    },


    // Return a list of imports for the given array of nodes.
    imports: function(nodes) {
      var map = {},
          imports = [];

      // Compute a map from name to node.
      nodes.forEach(function(d) {
        map[d.data.name] = d;
      });

      // For each import, construct a link from the source to target node.
      nodes.forEach(function(d) {
        if (d.data.imports) d.data.imports.forEach(function(i) {
	    imports.push({source: map[d.data.name], target: map[i]});
          //imports.key=5;
        });
      });

      return imports;
    },
    
// Return a list of imports for the given array of nodes.
    // Return a list of imports for the given array of nodes.
    imports1: function(nodes,classes) {
      var map = {},
          imports = [];

      // Compute a map from name to node.
      nodes.forEach(function(d) {
        map[d.data.name] = d;
      });

      // For each import, construct a link from the source to target node.
      classes.forEach(function(d) {     
          imports.push({source: map[d.source], target: map[d.target], weight: d.weight});
          //imports.weight=d.weight;
          //imports.key=5;
      });

      return imports;
    },

    weight:function(imports,classes) {
      var map = {},
          weight = [];

      // Compute a map from name to node.
      imports.forEach(function(d) {
        map[d.source] = d;
      });

      // For each import, construct a link from the source to target node.
      classes.forEach(function(d) {     
          imports.push({source: map[d.source], target: map[d.target]});
          //imports.weight=d.weight;
          //imports.key=5;
      });

      return imports;
    }

    

  };
})();
