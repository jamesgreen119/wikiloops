library(igraph)
library(GGally)
library(ggplot2)

setwd("Documents/wikiloopr") ##change to directory where files are output
data=read.csv("pairs.txt",sep="|",header = FALSE)
data=data[-(5494:5495),]
data$V3[data$V3 %in% c("Science","Knowledge","Awareness","Consciousness","Quality (philosophy)","Philosophy","Pre-Socratic philosophy","Ancient Greek philosophy","Hellenistic period","Ancient Greece","Civilization","Complex society","Anthropology","Human","Homo","Genus","Taxonomy (biology)")]="Science"

data=unique(data)

g <- graph_from_edgelist(as.matrix(data[,1:2]), directed = TRUE)
numVertices <- vcount(g)
numEdges <- ecount(g)

comps = clusters(g)

ggnet2(g,node.size=2,edge.size=0.2,color=comps$membership)+ggtitle("Graph of Wiki Loops")


##plot(g,layout=layout.fruchterman.reingold,vertex.size=2,edge.arrow.size=0.1,vertex.label=NA) # you can play with the vertex and edge sizes to get a better viz

##tkplot(g)

cluster<-cluster_walktrap(g)
membership(cluster)
table(membership(cluster))





data2=read.csv("loopPairs.txt",sep="|",header = FALSE)

g2<- graph_from_edgelist(as.matrix(data2[,1:2]),directed=TRUE)
comps2=clusters(g2)


ggnet2(g2,node.size=2,edge.size=0.2,color=comps2$membership,arrow.size=6)+ggtitle("Graph of Wiki Loops")+ geom_text(aes(label = names(V(g2)),fontface = "bold"),vjust="outward",hjust="inward")


