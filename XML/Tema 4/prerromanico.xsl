<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="5.0" encoding="utf-8" indent="yes"/>
    <xsl:template match="monuments">
        <xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html></xsl:text>
        <html lang="es">
            <head>
                <link rel="stylesheet" type="text/css" href="style.css"/>
                <title>Monumentos del Prerrománico</title>
            </head>
            <body>
                <header>
                    <h1>Monumentos del Prerrománico</h1>
                </header>
                <main>
                    <xsl:for-each select="monument">
                      <section>
                        <section>
                          <h2>
                            <xsl:value-of select="name"/>
                          </h2>
                          <h3>Datos del monumento</h3>
                          <ul>
                            <li>Tipo: <xsl:value-of select="type"/>
                            </li>
                            <li>Año: <xsl:value-of select="year"/>
                            </li>
                            <xsl:for-each select="builders">
                              <li>Constructor: <xsl:value-of select="builder"/>
                              </li>
                            </xsl:for-each>
                            <li>Estado: <xsl:value-of select="status"/>
                            </li>
                            <li>Valoraciones: <xsl:value-of select="rating"/>
                            </li>
                          </ul>
                          </section>
                          <section>
                          <h3>Localización</h3>
                          <table>
                            <tbody>
                              <tr>
                                <td>Municipio:</td>
                                <td>
                                  <xsl:value-of select="location/municipality"/>
                                </td>
                              </tr>
                              <tr>
                                <td>Dirección:</td>
                                <td>
                                  <xsl:value-of select="location/address"/>
                                </td>
                              </tr>
                              <tr>
                                <td>Coordenates:</td>
                                <td>
                                  <xsl:element name="a">
                                    <xsl:attribute name="href">
                                      https://maps.google.com?q=<xsl:value-of select="location/coordenates/latitude"/>,<xsl:value-of select="location/coordenates/longitude"/>
                                    </xsl:attribute>
                                    https://maps.google.com?q=<xsl:value-of select="location/coordenates/latitude"/>,<xsl:value-of select="location/coordenates/longitude"/> Altitude: <xsl:value-of select="location/coordenates/altitude"/>
                                  </xsl:element>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                          </section>
                          <section>
                            <h3>Visitas</h3>
                            <xsl:for-each select="visit/period">
                              <table>
                                <tbody>
                                    <tr>
                                      <td>Periodo:</td>
                                      <td>
                                        De <xsl:value-of select="@start"/> a <xsl:value-of select="@end"/>
                                      </td>
                                    </tr>
                                    <xsl:for-each select="day">
                                      <tr>
                                        <td>Días:</td>
                                        <td>
                                          De <xsl:value-of select="@start"/> a <xsl:value-of select="@end"/>
                                        </td>
                                      </tr>
                                      <xsl:for-each select="hour">
                                        <td>Horas de visita:</td>
                                        <td>
                                          De <xsl:value-of select="@start"/> a <xsl:value-of select="@end"/>
                                        </td>
                                      </xsl:for-each>
                                    </xsl:for-each>
                                </tbody>
                              </table>
                            </xsl:for-each>
                          </section>
                          <xsl:for-each select="gallery">
                            <section>
                              <h3>Galeria:</h3>
                              <ul class="gallery">
                                <xsl:for-each select="photo">
                                  <li>
                                    <xsl:element name="img">
                                      <xsl:attribute name="src">
                                          <xsl:value-of select="@uri"/>
                                      </xsl:attribute>
                                      <xsl:attribute name="alt">
                                          <xsl:value-of select="@name"/>
                                      </xsl:attribute>
                                    </xsl:element>
                                  </li>
                                </xsl:for-each>
                                <xsl:for-each select="video">
                                  <li>
                                    <xsl:element name="iframe">
                                      <xsl:attribute name="src">
                                          <xsl:value-of select="@uri"/>
                                      </xsl:attribute>
                                    </xsl:element>
                                  </li>
                                </xsl:for-each>
                              </ul>
                            </section>
                          </xsl:for-each>
                          <section>
                            <h3>Referencias:</h3>
                            <ol>
                              <xsl:for-each select="bibliography/website">
                                <li>
                                  <xsl:element name="a">
                                    <xsl:attribute name="href">
                                        <xsl:value-of select="."/>
                                    </xsl:attribute>
                                    <xsl:value-of select="."/>
                                  </xsl:element>
                                </li>
                              </xsl:for-each>
                            </ol>
                        </section>
                      </section>
					          </xsl:for-each>
                </main>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>